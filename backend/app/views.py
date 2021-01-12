from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response

from app.models import Tour, Country, City, Hotel, Airline, Insurance, Document, FavouriteTour
from app.permissions import IsAdminOrReadOnly, IsAdminOrCreateOnly
from app.serializers import TourSerializer, CountrySerializer, CitySerializer, HotelSerializer, AirlineSerializer, \
    InsuranceSerializer, DocumentSerializer, FavouriteTourSerializer


# TODO профиль

class TestView(ListCreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

    def list(self, request, *args, **kwargs):
        return Response('hello')


class TourView(ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [IsAdminOrReadOnly]

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
    serializer_class = FavouriteTourSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'tour'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def filter_queryset(self, queryset):
        queryset = queryset.filter(user=self.request.user)
        return super().filter_queryset(queryset)


class DocumentView(ModelViewSet):  # redo чтобы мог редактировать пользователь
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAdminOrCreateOnly]


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
