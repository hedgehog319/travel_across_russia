from datetime import date
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_image_file_extension, int_list_validator, RegexValidator, validate_slug
from django.db import models


class User(AbstractUser):
    """Пользователь"""
    ACCESS_CHOICES = (
        (1, 'Пользователь'),
        (2, 'Турменеджер'),
        (3, 'Админ'),
    )
    access_right = models.PositiveSmallIntegerField("Уровень доступа", choices=ACCESS_CHOICES, default=1)
    document = models.OneToOneField('Document', verbose_name="Документ", on_delete=models.SET_NULL,
                                    null=True, blank=True)
    fav_tours = models.ManyToManyField('Tour', through='FavouriteTour')

    def __str__(self):
        return self.username


class FavouriteTour(models.Model):
    """Избранный тур"""
    user = models.ForeignKey('User', verbose_name="Пользователь", on_delete=models.CASCADE)
    tour_id = models.ForeignKey('Tour', verbose_name="Тур", on_delete=models.CASCADE, related_name='favourites')

    class Meta:
        unique_together = ['user', 'tour_id']
        verbose_name = "Избранный тур"
        verbose_name_plural = "Избранные туры"

    def name(self):
        return self.tour_id.name()

    def price(self):
        return self.tour_id.price()

    def city_name(self):
        return self.tour_id.city_name()

    def country_name(self):
        return self.tour_id.country_name()

    def description(self):
        return self.tour_id.description()

    def __str__(self):
        return f'{self.user.username} - {self.tour_id.hotel.name}'


class RatingTour(models.Model):
    """Оценка тура"""
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

    user = models.ForeignKey('User', verbose_name="Пользователь", on_delete=models.SET_NULL, null=True)
    tour_id = models.ForeignKey('Tour', verbose_name="Тур", on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField("Оценка", choices=RATING_CHOICES)

    class Meta:
        unique_together = ['user', 'tour_id']
        verbose_name = "Оценка тура"
        verbose_name_plural = "Оценки туров"

    def __str__(self):
        return f'User: {"Deleted User" if not self.user else self.user.username}; ' \
               f'tour: {self.tour_id.name()}; rating: {self.rating / 2}'


class Document(models.Model):
    """Документ"""
    TYPE_CHOICES = (
        (1, 'Паспорт'),
        (2, 'Загранпаспорт'),
    )
    type = models.PositiveSmallIntegerField("Тип документа", choices=TYPE_CHOICES)
    series = models.CharField("Серия", max_length=4,
                              validators=[int_list_validator(message="Допустимы только цифры.")])
    number = models.CharField("Номер", max_length=6,
                              validators=[int_list_validator(message="Допустимы только цифры.")])
    firstname = models.CharField("Имя", max_length=150, help_text='Латиница в верхнем регистре')
    lastname = models.CharField("Фамилия", max_length=150, help_text='Латиница в верхнем регистре')
    birthdate = models.DateField("Дата рождения", default=date.today)

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class Tourist(models.Model):
    """Турист"""
    booked_tour = models.ForeignKey('BookedTour', verbose_name="Забронированный тур", on_delete=models.CASCADE,
                                    related_name='tourists')
    document = models.OneToOneField('Document', verbose_name="Документ", on_delete=models.PROTECT)
    email = models.EmailField("Email", blank=True)

    class Meta:
        verbose_name = "Турист"
        verbose_name_plural = "Туристы"

    def __str__(self):
        return f'Id {self.id}: {self.email}'


class BookedTour(models.Model):
    """Забронированный тур"""
    tour_id = models.ForeignKey('Tour', verbose_name="Тур", on_delete=models.CASCADE)
    start_date = models.DateField("Дата начала", default=date.today)
    end_date = models.DateField("Дата завершения", default=date.today)
    owner = models.ForeignKey('User', verbose_name="Отправитель", on_delete=models.SET_NULL,
                              null=True, blank=True)

    class Meta:
        verbose_name = "Забронированный тур"
        verbose_name_plural = "Забронированные туры"

    def __str__(self):
        return f'{self.tour_id.name()}, {self.tour_id.city_name()}, {self.tour_id.country_name()}'


class Tour(models.Model):
    """Тур"""
    count_days = models.PositiveIntegerField("Кол-во дней")
    city = models.ForeignKey('City', verbose_name="Город", on_delete=models.CASCADE)
    hotel = models.ForeignKey('Hotel', verbose_name="Отель", on_delete=models.CASCADE)
    airline = models.ForeignKey('Airline', verbose_name="Авиакомпания", on_delete=models.PROTECT)
    insurance = models.ForeignKey('Insurance', verbose_name="Страховка", on_delete=models.SET_NULL, null=True)
    rating = models.ManyToManyField('User', verbose_name="Оценки", through='RatingTour')

    class Meta:
        verbose_name_plural = 'Туры'
        verbose_name = 'Тур'

    def tour_id(self):
        return self.id

    def country_name(self):
        return self.city.country.name

    def city_name(self):
        return self.city.name

    def name(self):
        return self.hotel.name

    def description(self):
        return self.hotel.description

    def food_type(self):
        return self.hotel.type_of_food

    def price(self):
        return self.count_days * (self.hotel.price_for_night + self.insurance.price_for_day)

    def __str__(self):
        return f'{self.name()}, {self.city_name()}, {self.country_name()}'


class Airline(models.Model):
    """Авиакомпания"""
    name = models.CharField("Название", max_length=150)

    class Meta:
        verbose_name = "Авиакомпания"
        verbose_name_plural = "Авиакомпании"

    def __str__(self):
        return f'Id {self.id}: {self.name}'


class Insurance(models.Model):
    """Страховка"""
    price_for_day = models.PositiveIntegerField("Цена за сутки")
    refund = models.DecimalField("Сумма возврата", max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = "Страховка"
        verbose_name_plural = "Страховки"

    def __str__(self):
        return f'Id {self.id}: price {self.price_for_day}'


class Hotel(models.Model):
    """Отель"""
    FOOD_CHOICES = (
        ('RO', 'Без питания'),
        ('BB', 'Завтрак'),
        ('HB', 'Завтрак + ужин'),
        ('FB', 'Завтрак + обед + ужин'),
        ('AI', 'Все включено'),
    )

    name = models.CharField("Название", max_length=150)
    address = models.CharField("Адрес", max_length=300)
    number_of_rooms = models.IntegerField("Кол-во комнат")
    description = models.CharField("Описание", max_length=500)
    type_of_food = models.CharField("Тип питания", choices=FOOD_CHOICES, max_length=2)
    price_for_night = models.PositiveIntegerField("Цена за ночь")
    city = models.ForeignKey('City', verbose_name="Город", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Отель"
        verbose_name_plural = "Отели"

    def __str__(self):
        return f'Id {self.id}: {self.name}'


class HotelPhoto(models.Model):
    """Фото отеля"""
    hotel = models.ForeignKey('Hotel', verbose_name="Отель", on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField("Фото", upload_to='hotels_photos', validators=[validate_image_file_extension])
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Фото отеля"
        verbose_name_plural = "Фото отелей"

    # https://habr.com/ru/post/505946/ - интересная статья, про хранение изображений
    def __str__(self):
        return f'Id {self.id}: to {self.hotel.name}'


class City(models.Model):
    """Город"""
    country = models.ForeignKey('Country', verbose_name="Страна", on_delete=models.CASCADE)
    name = models.CharField("Название", max_length=150)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.name


class Country(models.Model):
    """"Страна"""
    name = models.CharField("Название", max_length=150, null=True)
    is_visa = models.BooleanField("Нужна виза", default=False)

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

    def __str__(self):
        return self.name
