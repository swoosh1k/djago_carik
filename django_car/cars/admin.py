from django.contrib import admin
from .models import *
# Register your models here.




@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('color', 'mark', 'year')




@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('name',)



@admin.register(UserBuy)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone',)



@admin.register(Dop)
class DopAdmin(admin.ModelAdmin):
    list_display = ('camera',  'kovriki',)