from django.contrib import admin
from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'email', 'phone')

    def save_model(self, request, obj, form, change):
        if 'password' in form.changed_data:
            password = form.cleaned_data.get('password')
            obj.set_password(password)

        super().save_model(request, obj, form, change)


admin.site.register(User, UserAdmin)
