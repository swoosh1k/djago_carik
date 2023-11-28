from django.db.models.signals import post_save
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import UserBuy
import telebot
from telegram import Bot, Update
from telegram.ext import Updater

@receiver(post_save, sender = UserBuy )
def print_telebot(sender,  instance, created, **kwargs):
    if created:
        print(instance.name)
        bot = telebot.TeleBot('6986696520:AAHr3K5vonVOGL4fzIgdtSru-ZkiAYek3-U')
        name = instance.name
        phone = instance.phone
        car = instance.car.mark
        message = f"Заказ машины {car} от человека с номером телефона {phone} и именем {name}"
        bot.send_message(545589900, message)