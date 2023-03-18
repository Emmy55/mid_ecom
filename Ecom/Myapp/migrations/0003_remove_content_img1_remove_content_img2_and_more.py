# Generated by Django 4.1.7 on 2023-03-18 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Myapp', '0002_product_content_alter_content_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='img1',
        ),
        migrations.RemoveField(
            model_name='content',
            name='img2',
        ),
        migrations.RemoveField(
            model_name='content',
            name='price1',
        ),
        migrations.RemoveField(
            model_name='content',
            name='price2',
        ),
        migrations.RemoveField(
            model_name='content',
            name='title1',
        ),
        migrations.RemoveField(
            model_name='content',
            name='title2',
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='Myapp.content')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]