from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from app.views import TourView, CountryView, TestView, CityView, HotelView, AirlineView, InsuranceView

router = SimpleRouter()
router.register('tours', TourView)
router.register('countries', CountryView)
router.register('cities', CityView)  # ?country=COUNTRY_ID, или ?country_name=Россия
router.register('hotels', HotelView)
router.register('airlines', AirlineView)
router.register('insurances', InsuranceView)

urlpatterns = [
    path('test', TestView.as_view())
]

# регистрация /auth/users/ POST (username и password)
# логин /auth/jwt/create/ POST (username и password) вернет (access, refresh)

urlpatterns += router.urls
