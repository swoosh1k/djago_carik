from django import forms
from .models import *




class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'



class DopForm(forms.ModelForm):
    class Meta:
        model = Dop
        fields = ('kovriki', 'camera', 'heated_sets', 'airbags')


class UserForm(forms.ModelForm):
    class Meta:
        model = UserBuy
        fields = ('name', 'email', 'phone')