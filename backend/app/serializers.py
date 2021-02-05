from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

import app.signals
from app.models import Tour, Country, City, Hotel, Airline, Insurance, Document, FavouriteTour, Tourist, HotelPhoto, \
    BookedTour, RatingTour


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'is_staff',
                  'access_right', 'document', 'email')


class UserGetUpdateSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')


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


class HotelPhotoSerializer(ModelSerializer):
    class Meta:
        model = HotelPhoto
        fields = ('hotel', 'photo')


class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = ('type', 'series', 'number', 'firstname', 'lastname', 'birthdate')


class TouristSerializer(ModelSerializer):
    document = DocumentSerializer()

    class Meta:
        model = Tourist
        fields = ['email', 'document']


class BookedTourSerializer(ModelSerializer):
    tourists = TouristSerializer(many=True, write_only=True)

    class Meta:
        model = BookedTour
        fields = ('tour_id', 'tourists')

    def create(self, validated_data):
        tourists_data = validated_data.pop('tourists')
        booked_tour = BookedTour.objects.create(**validated_data)
        for tourist_data in tourists_data:
            document_data = tourist_data.pop('document')
            document = Document.objects.create(**document_data)

            Tourist.objects.create(booked_tour=booked_tour, document=document, **tourist_data)
        return booked_tour


class TourSerializer(ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'


class TourReceivingSerializer(ModelSerializer):
    photo = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()
    is_favourite = serializers.SerializerMethodField(method_name='favourite')

    class Meta:
        model = Tour
        fields = (
            'tour_id', 'name', 'price', 'count_days', 'city_name', 'country_name',
            'description', 'food_type', 'rating', 'is_favourite', 'photo')

    def get_photo(self, obj):
        photos = HotelPhoto.objects.filter(hotel__tour__id=obj.id).order_by('time_created').first()
        request = self.context.get('request')

        if not photos:
            return ''
        return request.build_absolute_uri(photos.photo.url)

    def favourite(self, obj):
        user = self.context['request'].user
        if not user.is_authenticated:
            return False
        return True if obj.favourites.filter(user=user.id) else False

    def get_rating(self, obj):
        marks = RatingTour.objects.all().filter(tour_id=obj.id).values_list('rating', flat=True)
        if not marks:
            return 0
        return sum(marks) / len(marks) / 2


class FavouriteTourSerializer(ModelSerializer):
    rating = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()

    class Meta:
        model = FavouriteTour
        fields = ('tour_id', 'name', 'price', 'city_name', 'country_name', 'description', 'rating', 'photo')

    def get_rating(self, obj):
        marks = RatingTour.objects.all().filter(tour_id=obj.tour_id.id).values_list('rating', flat=True)
        if not marks:
            return 0
        return sum(marks) / len(marks) / 2

    def get_photo(self, obj):
        photos = HotelPhoto.objects.filter(hotel__tour__id=obj.tour_id.id).order_by('time_created').first()
        request = self.context.get('request')

        if not photos:
            return ''
        return request.build_absolute_uri(photos.photo.url)


class RatingTourSerializer(ModelSerializer):
    class Meta:
        model = RatingTour
        fields = ('tour_id', 'rating')
