from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from app.views import TourView, CountryView, CityView, HotelView, AirlineView, InsuranceView, DocumentView, \
    FavouriteTourView, UserProfileView, HotelPhotoView, document_types, access_types, food_types, BookedTourView, \
    RatingTourView, TopTourView

router = SimpleRouter()
router.register('tours', TourView)  # ?city=CITY_NAME & country=COUNTRY_NAME & count_days=7
router.register('booked-tours', BookedTourView)
router.register('documents', DocumentView)  # only GET and PATCH
router.register('fav-tours', FavouriteTourView)  # /fav-tour/TOUR_ID/ - удаление
router.register('countries', CountryView)
router.register('cities', CityView)  # ?country=COUNTRY_ID, или ?country_name=Россия
router.register('hotels', HotelView)  # ?city=CITY_NAME & country=COUNTRY_NAME & type_of_food=1
router.register('airlines', AirlineView)
router.register('insurances', InsuranceView)

router.register('hotel-photos', HotelPhotoView)  # ?hotel=HOTEL_ID & many=True - все фотки; many=False - одну


urlpatterns = [
    path('user-profile/', UserProfileView.as_view()),
    path('rating-tours/', RatingTourView.as_view()),  # only POST, передать tour_id, rating
    path('top-tours/', TopTourView.as_view()),
    path('documents/types/', document_types),
    path('users/types/', access_types),
    path('hotels/food-types/', food_types),
]

# регистрация /auth/users/ POST (username и password)
# логин /auth/jwt/create/ POST (username и password) вернет (access, refresh)

urlpatterns += router.urls
