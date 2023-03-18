from django.contrib import admin

# Register your models here.

from .models import content
from .models import product_content, Cart

admin.site.register(content)
admin.site.register(product_content)
admin.site.register(Cart)