from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from app.models import Tour, Country, City, Hotel, Airline, Insurance
from app.permissions import IsAdminOrReadOnly
from app.serializers import TourSerializer, CountrySerializer, CitySerializer, HotelSerializer, AirlineSerializer, \
    InsuranceSerializer


# TODO туры(get, post, patch), документы(post, patch), отели(get)
# TODO для посика тура (страна, продолжительность)

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
            cities = list(cities.values_list('id', flat=True))
            queryset = queryset.filter(city__in=cities)
        if 'count_days' in params:
            queryset = queryset.filter(count_days__lte=params['count_days'])

        return queryset


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


class AirlineView(ModelViewSet):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer
    permission_classes = [IsAdminOrReadOnly]


class InsuranceView(ModelViewSet):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
    permission_classes = [IsAdminOrReadOnly]
