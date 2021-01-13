from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth import get_user_model

from app.models import Document, Tourist, BookedTour, Tour, Airline, Insurance, Country, Hotel, City, FavouriteTour


@admin.register(get_user_model())
class UserAdmin(ModelAdmin):
    list_display = ('username', 'id', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff',)


@admin.register(Country)
class CountryAdmin(ModelAdmin):
    list_display = ('name', 'id', 'is_visa')


@admin.register(City)
class CityAdmin(ModelAdmin):
    list_display = ('name', 'country', 'id')


@admin.register(Hotel)
class HotelAdmin(ModelAdmin):
    list_display = ('name', 'city', 'id')


admin.site.register(Document)
admin.site.register(Tourist)
admin.site.register(BookedTour)
admin.site.register(Tour)
admin.site.register(Airline)
admin.site.register(Insurance)
admin.site.register(FavouriteTour)



# для настройки отображения в админке
# https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Admin_site
