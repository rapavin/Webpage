from django.urls import path

from . import views

urlpatterns = [
    path('',views.Home_Page, name='Home_Page'),
    path('Firmware_Page',views.Firmware_Page, name='Firmware_Page'),
    path('',views.stacking_Page, name='stacking_Page'),
]
