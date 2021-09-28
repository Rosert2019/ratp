from django.contrib import admin
from . models import Station

# Register your models here.

#admin.site.register(Station)


class StationAdmin(admin.ModelAdmin):
    list_display = ('name','line', 'geo_location')
    ordering = ('name',)
    search_fields = ('name',)

admin.site.register(Station, StationAdmin)
