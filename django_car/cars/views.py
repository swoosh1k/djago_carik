from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from .models import *
from .forms import *
from django.views import View

class Car_list(ListView):
    model = Car
    context_object_name = 'cars'
    template_name = 'car/car_list.html'



    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titlte'] = 'главная страница'
        return context




class AddCar(CreateView):
    template_name = 'cars/add_car.html'
    form_class = CarForm
    success_url = ('main')




class CarDetail(ListView):
    template_name = 'cars/car_detail.html'
    model = Car
    context_object_name = 'car'

    def get_queryset(self):
        return Car.objects.get(id = self.kwargs['pk'])



    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titlte'] = 'Добавление машины в корзину '
        context['form_1'] = DopForm
        context['form_2'] = UserForm
        return context




class AddDop(View):
    def post(self, request, pk):
        form_1  = DopForm(request.POST or None)
        form_2 = UserForm(request.POST or None)
        car = Car.objects.get(id = pk)
        if all([form_1.is_valid(), form_2.is_valid()]):
            form_1 = form_1.save(commit = False)
            form_2 = form_2.save(commit = False)
            form_1.car = car
            form_2.car = car
            form_1.save()
            form_2.save()
            return redirect('main')





from decimal import Decimal
from django.conf import settings

#
# class Cart(object):
#
#     def __init__(self, request):
#         """
#         Инициализируем корзину
#         """
#         self.session = request.session
#         cart = self.session.get(settings.CARS_SESSION_ID)
#         if not cart:
#             # save an empty cart in the session
#             cart = self.session[settings.CART_SESSION_ID] = {}
#         self.cart = cart

