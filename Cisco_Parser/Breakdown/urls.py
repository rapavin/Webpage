from django.urls import path

from . import views

urlpatterns = [
    path('',views.Home_Page, name='Home_Page'),
    path('Parser_Page',views.Parser_Page, name='Parser_Page'),
    path('upload_read',views.upload_read, name='upload_read'),
]
