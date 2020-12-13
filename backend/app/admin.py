from django.contrib import admin

from app.models import Countries, Cities, Hotels, Insurances, Airlines, Clients, TourCatalog, BookedTours, \
    TypeOfDocuments, Tourists, Users, Employees

admin.site.register(Countries)
admin.site.register(Cities)
admin.site.register(Hotels)
admin.site.register(Insurances)
admin.site.register(Airlines)
admin.site.register(Clients)
admin.site.register(TourCatalog)
admin.site.register(BookedTours)
admin.site.register(TypeOfDocuments)
admin.site.register(Tourists)
admin.site.register(Users)
admin.site.register(Employees)

# для настройки отображения в админке
# https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Admin_site
