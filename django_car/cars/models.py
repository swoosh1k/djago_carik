from django.db import models




class Mark(models.Model):
    name = models.CharField('марка', max_length=100)


    def __str__(self):
        return self.name



class Car(models.Model):
    year = models.SmallIntegerField('год выпуска')
    color = models.CharField('цвет машины', max_length=150)
    description = models.TextField('история машины', max_length=10000)
    price = models.SmallIntegerField('цена машины')
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE , verbose_name='марка машины ')







    def __str__(self):
        return self.mark.name

    class Meta:
        verbose_name = 'машина'
        verbose_name_plural = 'машины'





class Dop(models.Model):
    kovriki = models.BooleanField('коврики', default=False)
    camera = models.BooleanField("камера заднего вида", default=False)
    heated_sets = models.BooleanField("подогрев седений", default = False)
    airbags = models.BooleanField('подушки безопасности', default = False)
    car = models.ForeignKey(Car, verbose_name='машина', on_delete = models.CASCADE)


    def __str__(self):
        return f'дополнение для машины {self.car}'


    class Meta:
        verbose_name = 'дополнение'
        verbose_name_plural = 'дополнения'


class UserBuy(models.Model):
    name = models.CharField('Ваше имя', max_length=150)
    email = models.EmailField()
    phone = models.CharField("ваш номер телефона", max_length=150)
    car = models.ForeignKey(Car, verbose_name='машина', on_delete= models.CASCADE)



