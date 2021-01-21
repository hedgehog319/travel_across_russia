from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe

from app.models import Document, Tourist, BookedTour, Tour, Airline, Insurance, Country, Hotel, City, FavouriteTour, \
    HotelPhoto, RatingTour


@admin.register(get_user_model())
class UserAdmin(ModelAdmin):
    list_display = ('username', 'id', 'first_name', 'last_name', 'is_staff')
    readonly_fields = ('username', 'email')
    list_filter = ('is_staff',)


@admin.register(Country)
class CountryAdmin(ModelAdmin):
    list_display = ('name', 'id', 'is_visa')


@admin.register(City)
class CityAdmin(ModelAdmin):
    list_display = ('name', 'country', 'id')


class HotelShortsInline(admin.TabularInline):
    model = HotelPhoto
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="50" height="60">')

    get_image.short_description = 'Preview'


@admin.register(Hotel)
class HotelAdmin(ModelAdmin):
    list_display = ('name', 'city', 'id')
    list_filter = ('name', 'city')
    search_fields = ('city__name',)
    inlines = [HotelShortsInline]
    save_on_top = True
    save_as = True


@admin.register(HotelPhoto)
class HotelPhotoAdmin(ModelAdmin):
    list_display = ('hotel_name', 'id', 'get_image')
    readonly_fields = ('get_image',)

    def hotel_name(self, obj):
        return obj.hotel.name

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="50" height="60">')

    get_image.short_description = 'Preview'


class TourRatingInline(admin.TabularInline):
    model = RatingTour
    extra = 1


@admin.register(Tour)
class TourAdmin(ModelAdmin):
    list_display = ('id', 'name', 'city_name', 'country_name')
    list_display_links = ('name',)
    inlines = [TourRatingInline]


admin.site.register(Document)
admin.site.register(Tourist)
admin.site.register(BookedTour)
admin.site.register(Airline)
admin.site.register(Insurance)
admin.site.register(FavouriteTour)
admin.site.register(RatingTour)

admin.site.site_title = 'Django Travel-Across-Russia'
admin.site.site_header = 'Django Travel-Across-Russia'

# для настройки отображения в админке
# https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Admin_site
