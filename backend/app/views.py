from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status

from app.models import Tour, Country, City, Hotel, Airline, Insurance, Document, FavouriteTour, Tourist, BookedTour, \
    RatingTour
from app.permissions import IsAdminOrReadOnly, IsAdminOrCreateOnly, GetPatchPostForAuthUsers
from app.serializers import TourSerializer, CountrySerializer, CitySerializer, HotelSerializer, AirlineSerializer, \
    InsuranceSerializer, DocumentSerializer, FavouriteTourSerializer, UserGetUpdateSerializer, TouristSerializer, \
    TourReceivingSerializer, FavouriteTourReceivingSerializer


# todo фото для отеля
# todo сдлеать так, чтобы можно было передевать тип документа текстом
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
            fav_tours = FavouriteTour.objects.all().filter(user=request.user)
            for tour in response.data:
                tour.update({'rating': get_tour_rating(tour.get('id'))})
                if fav_tours.filter(tour=tour.get('id')):
                    tour.update({'is_favourite': True})
                else:
                    tour.update({'is_favourite': False})
        return super().finalize_response(request, response, *args, **kwargs)

    def filter_queryset(self, queryset):
        params = self.request.query_params
        if 'city' in params:
            city = City.objects.get(name=params['city'])
            queryset = queryset.filter(city=city.id)
        elif 'country' in params:
            country = Country.objects.get(name=params['country'])
            cities = City.objects.all().filter(country=country.id)
            cities = cities.values_list('id', flat=True)
            queryset = queryset.filter(city__in=cities)
        if 'count_days' in params:
            queryset = queryset.filter(count_days__lte=params['count_days'])

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
                tour.update({'rating': get_tour_rating(tour.get('tour'))})
        return super().finalize_response(request, response, *args, **kwargs)

    def perform_create(self, serializer):
        fav_tour = FavouriteTour.objects.all().filter(user=self.request.user, tour=self.request.data['tour'])
        if not fav_tour:
            serializer.save(user=self.request.user)

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
    serializer_class = HotelSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['type_of_food']

    def filter_queryset(self, queryset):
        params = self.request.query_params
        if 'city' in params:
            city = City.objects.get(name=params['city'])
            queryset = queryset.filter(city=city.id)
        elif 'country' in params:
            country = Country.objects.get(name=params['country'])
            cities = City.objects.all().filter(country=country.id)
            cities = cities.values_list('id', flat=True)
            queryset = queryset.filter(city__in=cities)

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


class TouristView(ModelViewSet):
    queryset = Tourist.objects.all()
    serializer_class = TouristSerializer
    permission_classes = [IsAdminOrCreateOnly]

    def create(self, request, *args, **kwargs):
        booked_tour = request.data.get('booked_tour')
        for field in request.data:
            if 'tourist' in field:
                data = request.data.get(field)
                document_data = data.get('document')
                document = Document.objects.create(**document_data)

                Tourist.objects.create(document=document, booked_tour=BookedTour.objects.get(id=booked_tour),
                                       email=data.get('email'))
        return Response(status=status.HTTP_201_CREATED)

    def perform_destroy(self, instance):
        document = instance.document
        user = get_user_model().objects.all().filter(document=document)
        instance.delete()
        if not user:
            document.delete()
