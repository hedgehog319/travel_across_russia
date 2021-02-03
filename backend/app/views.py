from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.db.models import QuerySet
from django.forms.models import model_to_dict
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView, \
    UpdateAPIView, GenericAPIView, ListAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status

from app.models import Tour, Country, City, Hotel, Airline, Insurance, Document, FavouriteTour, Tourist, BookedTour, \
    RatingTour, HotelPhoto
from app.permissions import IsAdminOrReadOnly, IsAdminOrCreateOnly, GetPatchPostForAuthUsers, IsAuthForGetOrCreateOnly
from app.serializers import TourSerializer, CountrySerializer, CitySerializer, HotelSerializer, AirlineSerializer, \
    InsuranceSerializer, DocumentSerializer, FavouriteTourSerializer, UserGetUpdateSerializer, TouristSerializer, \
    TourReceivingSerializer, HotelPhotoSerializer, BookedTourSerializer, RatingTourSerializer


# todo настроить allowed_hosts

def get_tour_rating(tour_id):
    marks = RatingTour.objects.all().filter(tour_id=tour_id).values_list('rating', flat=True)
    if not marks:
        return 0
    return sum(marks) / len(marks) / 2


class TourView(ModelViewSet):
    queryset = Tour.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TourReceivingSerializer
        return TourSerializer

    def filter_queryset(self, queryset):
        # GT >, LT <, GTE >=, LTE <=
        params = self.request.query_params
        if 'city' in params:
            queryset = queryset.filter(city__name=params['city'])

        elif 'country' in params:
            queryset = queryset.filter(city__country__name=params['country'])

        if 'count_days' in params:
            queryset = queryset.filter(count_days__lte=params['count_days'])

        if 'tour_id' in params:
            queryset = queryset.filter(id=params['tour_id'])

        if 'rating' in params:
            filters = []
            for tour in queryset:
                if get_tour_rating(tour.id) >= int(params['rating']) / 2:
                    filters.append(tour.id)
            queryset = queryset.filter(id__in=filters)

        if 'price' in params:
            start, end = map(int, params['price'].split(','))
            filters = []
            for tour in queryset:
                if start <= tour.price() <= end:
                    filters.append(tour.id)
            queryset = queryset.filter(id__in=filters)

            # queryset = queryset.filter(price__range=(start, end))

        if 'type_food' in params:
            types = list(params['type_food'].split(','))
            queryset = queryset.filter(hotel__type_of_food__in=types)

        return super().filter_queryset(queryset)


class FavouriteTourView(CreateModelMixin, ListModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = FavouriteTour.objects.all()
    serializer_class = FavouriteTourSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'tour_id'

    def filter_queryset(self, queryset):
        queryset = queryset.filter(user=self.request.user)
        return super().filter_queryset(queryset)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DocumentView(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [GetPatchPostForAuthUsers]

    def get_object(self):
        try:
            return Document.objects.get(user=self.request.user)
        except ObjectDoesNotExist:
            return None

    def patch(self, request, *args, **kwargs):
        if self.get_object() is None:
            return super().create(request, args, kwargs)
        return super().partial_update(request, args, kwargs)

    def create(self, request, *args, **kwargs):
        return self.patch(request, *args, **kwargs)

    def perform_create(self, serializer):
        document = serializer.save()
        if self.request.user.is_authenticated:
            self.request.user.document = document
            self.request.user.save()

    def filter_queryset(self, queryset):
        queryset = queryset.filter(user=self.request.user)
        return super().filter_queryset(queryset)


class CountryView(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAdminOrReadOnly]


class CityView(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['country', 'country__name']


class HotelView(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer  # todo возращает city_id вместо city_name. Это норм?
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['type_of_food']

    def filter_queryset(self, queryset):
        params = self.request.query_params
        if 'city' in params:
            queryset = queryset.filter(city__name=params['city'])
        elif 'country' in params:
            queryset = queryset.filter(city__country__name=params['country'])

        return super().filter_queryset(queryset)


class AirlineView(ModelViewSet):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer
    permission_classes = [IsAdminOrReadOnly]


class InsuranceView(ModelViewSet):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
    permission_classes = [IsAdminOrReadOnly]


class UserProfileView(RetrieveUpdateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserGetUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_user_model().objects.get(id=self.request.user.id)


class HotelPhotoView(ModelViewSet):
    queryset = HotelPhoto.objects.all().order_by('time_created')
    serializer_class = HotelPhotoSerializer
    permission_classes = [IsAdminOrReadOnly]

    def filter_queryset(self, queryset):
        if 'tour_id' in self.request.query_params:
            queryset = queryset.filter(hotel__tour__id=self.request.query_params['tour_id'])
        else:
            queryset = queryset.none()

        return queryset


@api_view(['GET'])
def document_types(request):
    return Response(status=status.HTTP_200_OK, data=dict(Document.TYPE_CHOICES))


@api_view(['GET'])
def access_types(request):
    return Response(status=status.HTTP_200_OK, data=dict(get_user_model().ACCESS_CHOICES))


@api_view(['GET'])
def food_types(request):
    return Response(status=status.HTTP_200_OK, data=dict(Hotel.FOOD_CHOICES))


class BookedTourView(ModelViewSet):
    queryset = BookedTour.objects.all()
    serializer_class = BookedTourSerializer
    permission_classes = [IsAuthForGetOrCreateOnly]
    lookup_field = 'tour_id'

    def filter_queryset(self, queryset):
        queryset = queryset.filter(owner=self.request.user)
        return queryset

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(owner=self.request.user)
            return
        serializer.save()


class RatingTourView(CreateAPIView):
    queryset = RatingTour.objects.all()
    serializer_class = RatingTourSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            mark = RatingTour.objects.get(user=request.user, tour_id=request.data['tour_id'])
            mark.delete()
            return super().create(request, *args, **kwargs)
        except:
            return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TopTourView(ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourReceivingSerializer

    def filter_queryset(self, queryset):
        if 'count' not in self.request.query_params:
            queryset = queryset.none()
            return queryset

        tours = []
        for tour in queryset:
            tours.append((tour.id, get_tour_rating(tour.id)))
        tours.sort(key=lambda i: i[1], reverse=True)
        tours = tours[:int(self.request.query_params['count'])]

        new_queryset = []
        for j in tours:
            new_queryset.append(queryset.get(id=j[0]))
        return new_queryset
