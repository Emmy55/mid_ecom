from django.db import models
# from django.conf import settings 
# from django.contrib.auth import get_user_model
# from django.db.models.signals import post_save
# from products.models import Product

# User = get_user_model()



# Create your models here.

class content(models.Model):
    img = models.ImageField(upload_to='img/%y')
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    

    img1 = models.ImageField(upload_to='img/%y')
    title1 = models.CharField(max_length=200)
    price1 = models.IntegerField()
    
    
    img2 = models.ImageField(upload_to='img/%y')
    title2 = models.CharField(max_length=200)
    price2 = models.IntegerField()



# class Cart(BaseModel):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
#     is_paid = models.BooleanField(default=False)





class CartItems(models.Model):
    cart = models.ForeignKey(to=content, on_delete=models.CASCADE)
    quantity =models.IntegerField()




# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     eitems = models.ManyToManyField(product, blank=True)

#     def __str__(self):
#         return self.user.username
    


# def post_save_profile_create(sender, instance, created, =args, ==kwargs):
#     if created:
#         Profile.objects.get_or_create(user=instance)


# post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)


class product_content(models.Model):
    img = models.ImageField(upload_to='img/%y')
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    

    img1 = models.ImageField(upload_to='img/%y')
    title1 = models.CharField(max_length=200)
    price1 = models.IntegerField()
    
    
    img2 = models.ImageField(upload_to='img/%y')
    title2 = models.CharField(max_length=200)
    price2 = models.IntegerField()