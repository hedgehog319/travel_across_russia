from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, Serializer
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

from app.models import Tour, Country, City, Hotel, Airline, Insurance


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'is_staff',
                  'access_right', 'document', 'email')


class TourSerializer(ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class AirlineSerializer(ModelSerializer):
    class Meta:
        model = Airline
        fields = '__all__'


class InsuranceSerializer(ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'