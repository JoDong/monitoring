from django.contrib import admin

# Register your models here.
from domain.models import UrlModel


class UrlAdmin(admin.ModelAdmin):
    list_display = ['url_name', 'url']


admin.site.register(UrlModel, UrlAdmin)
