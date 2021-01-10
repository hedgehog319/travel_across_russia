from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    access_right = models.IntegerField(default=0)
    document = models.ForeignKey('Document', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Id: {self.id}: {self.username}'


class Document(models.Model):
    series = models.IntegerField()
    number = models.IntegerField()
    visa_availability = models.BooleanField()  # наличие визы
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    birthdate = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Id {self.id}: {self.series} {self.number}'


class Tourist(models.Model):
    booked_tour = models.ForeignKey('BookedTour', on_delete=models.CASCADE)
    document = models.ForeignKey('Document', on_delete=models.PROTECT)
    email = models.EmailField()
    adult = models.BooleanField()

    def __str__(self):
        return f'Id {self.id}: {self.email}'


# Забронированные туры
class BookedTour(models.Model):
    tour = models.ForeignKey('TourCatalog', on_delete=models.CASCADE)
    departure_date = models.DateField(auto_now_add=True)
    arrival_date = models.DateField(auto_now_add=True)
    airline = models.ForeignKey('Airline', on_delete=models.CASCADE)
    insurance = models.ForeignKey('Insurance', on_delete=models.CASCADE)

    def __str__(self):
        return f'Id {self.id}: tour_id {self.tour.id}'


class TourCatalog(models.Model):
    name = models.CharField(max_length=150)
    tour_price = models.DecimalField(max_digits=8, decimal_places=2)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE)

    def __str__(self):
        return f'Id {self.id}: {self.name}'


class Airline(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'Id {self.id}: {self.name}'


class Insurance(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2)
    end_date = models.DateField()  # дата окончания страховки
    refund = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'Id {self.id}: price {self.price}'


class Country(models.Model):
    name = models.CharField(max_length=150)
    is_visa = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return f'Id {self.id}: {self.name}'


class Hotel(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=300)
    number_of_rooms = models.IntegerField()
    type_of_food = models.IntegerField()
    price_for_night = models.DecimalField(max_digits=8, decimal_places=2)
    city = models.ForeignKey('City', on_delete=models.CASCADE)

    def __str__(self):
        return f'Id {self.id}: {self.name}'


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return f'Id {self.id}: {self.name}'
