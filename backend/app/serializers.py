from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, Serializer
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

from app.models import Tour, Country, City, Hotel, Airline, Insurance, Document, FavouriteTour, Tourist, HotelPhoto


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'is_staff',
                  'access_right', 'document', 'email')


class UserGetUpdateSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')


class TourSerializer(ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'


class TourReceivingSerializer(ModelSerializer):
    class Meta:
        model = Tour
        fields = ('tour_id', 'name', 'price', 'city_name', 'country_name', 'description')  # + rating, is_favourite


class FavouriteTourSerializer(ModelSerializer):
    class Meta:
        model = FavouriteTour
        fields = ['tour']


class FavouriteTourReceivingSerializer(ModelSerializer):
    class Meta:
        model = FavouriteTour
        fields = ('tour_id', 'name', 'price', 'city_name', 'country_name', 'description')  # + rating


class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
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


class TouristSerializer(ModelSerializer):
    class Meta:
        model = Tourist
        fields = ('booked_tour',)


class HotelPhotoSerializer(ModelSerializer):
    class Meta:
        model = HotelPhoto
        fields = '__all__'
