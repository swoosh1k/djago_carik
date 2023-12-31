# Generated by Django 4.2.7 on 2023-11-28 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.SmallIntegerField(verbose_name='год выпуска')),
                ('color', models.CharField(max_length=150, verbose_name='цвет машины')),
                ('description', models.TextField(max_length=10000, verbose_name='история машины')),
                ('price', models.SmallIntegerField(verbose_name='цена машины')),
            ],
            options={
                'verbose_name': 'машина',
                'verbose_name_plural': 'машины',
            },
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='марка')),
            ],
        ),
        migrations.CreateModel(
            name='Dop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kovriki', models.BooleanField(default=False, verbose_name='коврики')),
                ('camera', models.BooleanField(default=False, verbose_name='камера заднего вида')),
                ('heated_sets', models.BooleanField(default=False, verbose_name='подогрев седений')),
                ('airbags', models.BooleanField(default=False, verbose_name='подушки безопасности')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car', verbose_name='машина')),
            ],
            options={
                'verbose_name': 'дополнение',
                'verbose_name_plural': 'дополнения',
            },
        ),
        migrations.AddField(
            model_name='car',
            name='mark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.mark', verbose_name='марка машины '),
        ),
    ]
