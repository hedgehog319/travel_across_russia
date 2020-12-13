from django.db import models
from datetime import date


class Countries(models.Model):
    country_name = models.CharField(max_length=50)
    is_visa = models.BooleanField(default=False)

    class Meta:
        # для отображения в адимнке
        verbose_name_plural = "Countries"  # Имя во множественном числе для объекта


class Cities(models.Model):
    country_id = models.ForeignKey(Countries, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=50)

    class Meta:
        # для отображения в адимнке
        verbose_name_plural = "Cities"  # Имя во множественном числе для объекта


class Hotels(models.Model):
    hotel_name = models.CharField(max_length=50)
    hotel_address = models.CharField(max_length=50)
    number_of_rooms = models.IntegerField()
    type_of_food = models.IntegerField()
    price_for_night = models.DecimalField(max_digits=8, decimal_places=2)
    city_id = models.ForeignKey(Cities, on_delete=models.CASCADE)

    class Meta:
        # для отображения в адимнке
        verbose_name_plural = "Hotels"  # Имя во множественном числе для объекта


# Страхования
class Insurances(models.Model):
    insurance_price = models.DecimalField(max_digits=8, decimal_places=2)  # цена страховки
    dates_of_insurance = models.DateField()  # todo решить либо дата окончания страховки, либо количество дней
    value_of_insurance = models.DecimalField(max_digits=8, decimal_places=2)  # стоимость возмещения

    class Meta:
        # для отображения в адимнке
        verbose_name_plural = "Insurances"  # Имя во множественном числе для объекта


# Авиакомпании
class Airlines(models.Model):
    airline_name = models.CharField(max_length=50)
    airline_country = models.CharField(max_length=50)

    class Meta:
        # для отображения в адимнке
        verbose_name_plural = "Airlines"  # Имя во множественном числе для объекта


# Заказчик
class Clients(models.Model):
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField()

    class Meta:
        # для отображения в адимнке
        verbose_name_plural = "Clients"  # Имя во множественном числе для объекта


class TourCatalog(models.Model):
    name = models.CharField(max_length=50)
    country_id = models.ForeignKey(Countries, on_delete=models.CASCADE)
    hotel_id = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    tour_price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        # для отображения в адимнке
        verbose_name_plural = "Tour_Catalog"  # Имя во множественном числе для объекта


# Забронированные туры
class BookedTours(models.Model):
    tour_id = models.ForeignKey(TourCatalog, on_delete=models.CASCADE)
    number_of_adults = models.IntegerField()
    number_of_children = models.IntegerField()
    departure_date = models.DateField()
    arrival_date = models.DateField()
    airline_id = models.ForeignKey(Airlines, on_delete=models.CASCADE)
    insurance_id = models.ForeignKey(Insurances, on_delete=models.CASCADE)

    class Meta:
        # для отображения в адимнке
        verbose_name_plural = "Booked_Tours"  # Имя во множественном числе для объекта


class TypeOfDocuments(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        # для отображения в адимнке
        verbose_name_plural = "Type_Of_Documents"  # Имя во множественном числе для объекта


class Tourists(models.Model):
    tour_id = models.ForeignKey(BookedTours, on_delete=models.CASCADE)
    client_id = models.ForeignKey(Clients, on_delete=models.SET_NULL, null=True)
    sex = models.BooleanField()  # True - men, False - woman
    date_of_birth = models.DateField(default=date.today)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    citizenship = models.CharField(max_length=50)
    type_of_document = models.ForeignKey(TypeOfDocuments, on_delete=models.SET_NULL, null=True)  # redo maybe

    # todo предлагаю все поместить в document_data
    document_data = models.CharField(max_length=50)
    document_term = models.DateField()  # срок дейстивия документа
    date_of_issue_of_document = models.DateField()  # дата выдачи документа
    document_issued_by = models.CharField(max_length=50)  # кем выдан

    class Meta:
        # для отображения в адимнке
        verbose_name_plural = "Tourists"  # Имя во множественном числе для объекта


class Users(models.Model):
    login = models.CharField(max_length=50)
    access_right = models.IntegerField()
    password = models.CharField(max_length=50)

    class Meta:
        # для отображения в адимнке
        verbose_name_plural = "Users"  # Имя во множественном числе для объекта


class Employees(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)

    class Meta:
        # для отображения в адимнке
        verbose_name_plural = "Employees"  # Имя во множественном числе для объекта
