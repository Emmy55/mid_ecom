# Generated by Django 4.1.5 on 2023-03-14 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img/%y')),
                ('title', models.CharField(max_length=200)),
                ('price', models.IntegerField(max_length=20)),
                ('img1', models.ImageField(upload_to='img/%y')),
                ('title1', models.CharField(max_length=200)),
                ('price1', models.IntegerField(max_length=20)),
                ('img2', models.ImageField(upload_to='img/%y')),
                ('title2', models.CharField(max_length=200)),
                ('price2', models.IntegerField(max_length=20)),
            ],
        ),
    ]