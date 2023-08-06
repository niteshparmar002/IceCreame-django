# Generated by Django 3.2.7 on 2021-10-19 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icecream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img')),
                ('desc', models.TextField()),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
