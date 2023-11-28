from django.urls import path, include
from .views import *


urlpatterns = [
    path('',Car_list.as_view(), name = 'main'),
    path('car_add/<int:pk>/', AddDop.as_view(), name='add_dop'),
    path('cardetail/<int:pk>/', CarDetail.as_view(), name = 'car_detail'),
    path('AddCar/', AddCar.as_view(), name = 'add_car'),
]