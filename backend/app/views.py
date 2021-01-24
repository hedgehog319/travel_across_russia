from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.forms.models import model_to_dict
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status

from app.models import Tour, Country, City, Hotel, Airline, Insurance, Document, FavouriteTour, Tourist, BookedTour, \
    RatingTour, HotelPhoto
from app.permissions import IsAdminOrReadOnly, IsAdminOrCreateOnly, GetPatchPostForAuthUsers
from app.serializers import TourSerializer, CountrySerializer, CitySerializer, HotelSerializer, AirlineSerializer, \
    InsuranceSerializer, DocumentSerializer, FavouriteTourSerializer, UserGetUpdateSerializer, TouristSerializer, \
    TourReceivingSerializer, FavouriteTourReceivingSerializer, HotelPhotoSerializer, BookedTourSerializer


# todo настроить allowed_hosts

def get_tour_rating(tour_id):
    marks = RatingTour.objects.all().filter(tour=tour_id).values_list('rating', flat=True)
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

    def finalize_response(self, request, response, *args, **kwargs):
        if request.method == 'GET':
            if request.user.is_authenticated:
                fav_tours = FavouriteTour.objects.all().filter(user=request.user)
            else:
                fav_tours = FavouriteTour.objects.none()

            for tour in response.data:
                print(type(response.data))
                tour.update({'rating': get_tour_rating(tour.get('tour_id'))})
                tour.update({'is_favourite': True if fav_tours.filter(tour=tour.get('tour_id')) else False})
        return super().finalize_response(request, response, *args, **kwargs)

    def filter_queryset(self, queryset):
        params = self.request.query_params
        if 'city' in params:
            queryset = queryset.filter(city__name=params['city'])

        elif 'country' in params:
            queryset = queryset.filter(city__country__name=params['country'])

        if 'count_days' in params:
            queryset = queryset.filter(count_days__lte=params['count_days'])

        if 'tour_id' in params:
            queryset = queryset.filter(id=params['tour_id'])

        return super().filter_queryset(queryset)


class FavouriteTourView(CreateModelMixin, ListModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = FavouriteTour.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'tour'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FavouriteTourReceivingSerializer
        return FavouriteTourSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        if request.method == 'GET':
            for tour in response.data:
                tour.update({'rating': get_tour_rating(tour.get('tour_id'))})
        return super().finalize_response(request, response, *args, **kwargs)

    def filter_queryset(self, queryset):
        queryset = queryset.filter(user=self.request.user)
        return super().filter_queryset(queryset)


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
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['hotel']

    def filter_queryset(self, queryset):
        if 'many' not in self.request.query_params:
            return queryset.none()

        queryset = super().filter_queryset(queryset)
        if self.request.query_params['many'].lower() == 'false':
            hotels = []
            filters = []
            for photo in queryset:
                if photo.hotel.id not in hotels:
                    filters.append(photo.id)
                    hotels.append(photo.hotel.id)

            queryset = queryset.filter(id__in=filters)

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
    permission_classes = [IsAdminOrCreateOnly]
    lookup_field = 'tour_id'
