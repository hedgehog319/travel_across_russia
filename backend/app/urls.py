from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from app.views import UserView

router = SimpleRouter()

router.register('api/users', UserView)

urlpatterns = [

]

urlpatterns += router.urls
