
# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Place, HeroPosition

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'subtype', 'size', 'x', 'y')

class HeroPositionAdmin(admin.ModelAdmin):
    list_display = ('hero', 'place', 'road', 'percents', 'invert_direction')

admin.site.register(Place, PlaceAdmin)
admin.site.register(HeroPosition, HeroPositionAdmin)
