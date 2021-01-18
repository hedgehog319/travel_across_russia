from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    FOOD_CHOICES = (
        (1, 'Пользователь'),
        (2, 'Турменеджер'),
        (3, 'Админ'),
    )
    access_right = models.PositiveSmallIntegerField(choices=FOOD_CHOICES, default=0)
    document = models.OneToOneField('Document', on_delete=models.SET_NULL, null=True, blank=True)
    fav_tours = models.ManyToManyField('Tour', through='FavouriteTour')

    def __str__(self):
        return f'Id: {self.id}: {self.username}'


class FavouriteTour(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.tour.hotel.name}'


class RatingTour(models.Model):
    RATING_CHOICES = (
        (1, '0.5'),
        (2, '1'),
        (3, '1.5'),
        (4, '2'),
        (5, '2.5'),
        (6, '3'),
        (7, '3.5'),
        (8, '4'),
        (9, '4.5'),
        (10, '5'),
    )

    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return f'User: {self.user.username}; tour: {self.tour.name()}; rating: {self.rating}'


class Document(models.Model):
    TYPE_CHOICES = (
        (1, 'Паспорт'),
        (2, 'Загранпаспорт'),
    )
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES)
    series = models.IntegerField()
    number = models.IntegerField()
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    birthdate = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Id {self.id}: {self.first_name} {self.last_name}'


class Tourist(models.Model):
    booked_tour = models.ForeignKey('BookedTour', on_delete=models.CASCADE)
    document = models.ForeignKey('Document', on_delete=models.PROTECT)
    email = models.EmailField()

    def __str__(self):
        return f'Id {self.id}: {self.email}'


# Забронированные туры
class BookedTour(models.Model):
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Id {self.id}: {self.tour.hotel.name}'


class Tour(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count_days = models.PositiveIntegerField()
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    hotel = models.OneToOneField('Hotel', on_delete=models.CASCADE)
    airline = models.ForeignKey('Airline', on_delete=models.PROTECT)
    insurance = models.ForeignKey('Insurance', on_delete=models.SET_NULL, null=True)
    rating = models.ManyToManyField('User', through='RatingTour')

    def country_name(self):
        return self.city.country.name

    def city_name(self):
        return self.city.name

    def name(self):
        return self.hotel.name

    def description(self):
        return self.hotel.description

    def __str__(self):
        return f'Id {self.id}: {self.hotel.name}'


class Airline(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'Id {self.id}: {self.name}'


class Insurance(models.Model):
    price_for_day = models.DecimalField(max_digits=8, decimal_places=2)
    refund = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'Id {self.id}: price {self.price_for_day}'


class Hotel(models.Model):
    FOOD_CHOICES = (
        (1, 'Без питания'),
        (2, 'Завтрак'),
        (3, 'Завтрак + ужин'),
        (4, 'Завтрак + обед + ужин'),
        (5, 'Все включено'),
    )

    name = models.CharField(max_length=150)
    address = models.CharField(max_length=300)
    number_of_rooms = models.IntegerField()
    description = models.CharField(max_length=500)
    type_of_food = models.PositiveSmallIntegerField(choices=FOOD_CHOICES)
    price_for_night = models.DecimalField(max_digits=8, decimal_places=2)
    city = models.ForeignKey('City', on_delete=models.CASCADE)

    def __str__(self):
        return f'Id {self.id}: {self.name}'


class HotelPhoto(models.Model):
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='hotels_photos', null=True, blank=True)
    # https://habr.com/ru/post/505946/ - интересная статья, про хранение изображений


class City(models.Model):
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return f'Id {self.id}: {self.name}'


class Country(models.Model):
    name = models.CharField(max_length=150, null=True)
    is_visa = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return f'Id {self.id}: {self.name}'
