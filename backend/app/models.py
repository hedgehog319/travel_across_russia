from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    FOOD_CHOICES = (
        (0, 'Пользователь'),
        (1, 'Турменеджер'),
        (2, 'Админ'),
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
        return f'{self.user.username} - {self.tour.name}'


class Document(models.Model):
    series = models.IntegerField()
    number = models.IntegerField()
    visa_availability = models.BooleanField()  # наличие визы
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
        return f'Id {self.id}: {self.tour.name}'


class Tour(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count_days = models.PositiveIntegerField()
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE)
    airline = models.ForeignKey('Airline', on_delete=models.PROTECT)
    insurance = models.ForeignKey('Insurance', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Id {self.id}: {self.name}'


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
        (2, 'Скромный завтрак'),
        (3, 'Завтрак'),
        (4, 'Завтрак + ужин'),
        (5, 'Завтрак + обед + ужин'),
        (6, 'Все включено'),
    )

    name = models.CharField(max_length=150)
    address = models.CharField(max_length=300)
    number_of_rooms = models.IntegerField()
    type_of_food = models.PositiveSmallIntegerField(choices=FOOD_CHOICES)
    price_for_night = models.DecimalField(max_digits=8, decimal_places=2)
    city = models.ForeignKey('City', on_delete=models.CASCADE)

    def __str__(self):
        return f'Id {self.id}: {self.name}'


class City(models.Model):
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return f'Id {self.id}: {self.name}'


class Country(models.Model):
    name = models.CharField(max_length=150)
    is_visa = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return f'Id {self.id}: {self.name}'
