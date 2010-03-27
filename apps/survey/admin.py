#!/usr/bin/env python
#vim ai ts=4 sts=4 et sw=4
''' admin U i for the survey Apps'''
from django.contrib import admin
from models import SrActivity,SrProfile

class ProAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','sex','age','activity','date')
    list_filter = ('first_name','date')
    search_fields = ('first_name', 'last_name')


admin.site.register(SrActivity)
admin.site.register(SrProfile, ProAdmin)