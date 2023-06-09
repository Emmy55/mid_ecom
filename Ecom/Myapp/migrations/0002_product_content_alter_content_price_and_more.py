# Generated by Django 4.1.5 on 2023-03-14 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img/%y')),
                ('title', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('img1', models.ImageField(upload_to='img/%y')),
                ('title1', models.CharField(max_length=200)),
                ('price1', models.IntegerField()),
                ('img2', models.ImageField(upload_to='img/%y')),
                ('title2', models.CharField(max_length=200)),
                ('price2', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='content',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='content',
            name='price1',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='content',
            name='price2',
            field=models.IntegerField(),
        ),
    ]
