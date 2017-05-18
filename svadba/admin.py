# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Slika, Kategorija, Proizvod
from django.utils.html import format_html
"""
class SlikaAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.fajl.url))

    image_tag.short_description = 'Image'

    list_display = ['image_tag',]
"""
admin.site.register(Slika)
""", SlikaAdmin"""
admin.site.register(Kategorija)
admin.site.register(Proizvod)
# Register your models here.
