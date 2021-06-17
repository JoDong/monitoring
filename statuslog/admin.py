from django.contrib import admin

# Register your models here.
from statuslog.models import StatusLog


class StatusAdmin(admin.ModelAdmin):
    list_display = ['url', 'status', 'process']


admin.site.register(StatusLog, StatusAdmin)
