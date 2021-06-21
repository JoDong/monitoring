from django.urls import path
from . import views

app_name = 'domain'

urlpatterns = [
    path('create/', views.url_create, name='create'),
    path('update/<int:pk>', views.url_update, name='update'),
    path('delete/<int:pk>', views.url_delete, name='delete'),
    # path()
]
