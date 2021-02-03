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
    list_display = ('id', 'name', 'country')
    list_display_links = ('name',)


class HotelShortsInline(admin.TabularInline):
    model = HotelPhoto
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="50" height="60">')

    get_image.short_description = 'Preview'


@admin.register(Hotel)
class HotelAdmin(ModelAdmin):
    list_display = ('id', 'name', 'city')
    list_display_links = ('name',)
    list_filter = ('name', 'city')
    search_fields = ('city__name', 'name')
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


class TouristsInline(admin.TabularInline):
    model = Tourist
    extra = 0


@admin.register(BookedTour)
class BookedTourAdmin(ModelAdmin):
    list_display = ('tour_id', 'start_date', 'end_date')
    readonly_fields = ('tour_id', 'start_date', 'end_date', 'owner')
    inlines = [TouristsInline]


@admin.register(Airline)
class AirlineAdmin(ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)


@admin.register(Document)
class DocumentAdmin(ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'series', 'number')
    list_display_links = ('firstname', 'lastname')


@admin.register(FavouriteTour)
class FavouriteTourAdmin(ModelAdmin):
    list_display = ('user', 'tour_id')
    readonly_fields = ('user', 'tour_id')


@admin.register(RatingTour)
class RatingTourAdmin(ModelAdmin):
    list_display = ('id', 'tour_id', 'rating')
    list_display_links = ('tour_id',)
    readonly_fields = ('rating',)


@admin.register(Insurance)
class InsuranceAdmin(ModelAdmin):
    list_display = ('id', 'price_for_day', 'refund')
    list_display_links = ('price_for_day', 'refund')


@admin.register(Tourist)
class TouristAdmin(ModelAdmin):
    list_display = ('id', 'document', 'booked_tour')
    list_display_links = ('document', )


admin.site.site_title = 'Панел Администратора Travel-Across-Russia'
admin.site.site_header = 'Панел Администратора Travel-Across-Russia'

# для настройки отображения в админке
# https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Admin_site

# для добавления favicon в админку
# https://www.djangotricks.com/tricks/9RM5Mk6tRThd/
