from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator, RegexValidator
from django.utils.translation import gettext as _
# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.IntegerField(validators=[RegexValidator(r'^\d{1,10}$')])
    email = models.EmailField(validators=[EmailValidator()])

    def __str__(self):
        return self.user.username

class State(models.Model):
    state = models.CharField(_("state"), max_length=255)

    def __str__(self):
        return self.state

class Postcode(models.Model):
    postcode = models.CharField(_("postcode"), max_length=10)
    locality = models.CharField(_("locality"), max_length=255)
    state = models.CharField(_("state"), max_length=255)
    type = models.CharField(_("type"), max_length=255)

    def __str__(self):
        return self.postcode
class Suburb(models.Model):
    postcode = models.CharField(_("postcode"), max_length=10)
    locality = models.CharField(_("locality"), max_length=255)
    state = models.CharField(_("state"), max_length=255)
    type = models.CharField(_("type"), max_length=255)

    def __str__(self):
        return f'{self.locality}, {self.postcode}, {self.state}, {self.type}'
    
class CustomerAddress(models.Model):   
    houseNumber = models.CharField(max_length=1024)
    streetName = models.CharField(max_length=1024)
    suburb = models.ForeignKey(Suburb, on_delete=models.SET_NULL, null=True, blank=True, related_name="postcodes")
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    postcode = models.ForeignKey(Postcode, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.postcode is None and self.suburb:
            try:
                postcode = Postcode.objects.get(locality__iexact=self.suburb.locality, state=self.suburb.state)
                self.postcode = postcode
                state = State.objects.get(state=self.suburb.state)
                self.state = state
            except Postcode.DoesNotExist:
                pass
        super().save(*args, **kwargs)
    def __str__(self):
        return f'{self.houseNumber}/{self.streetName}, {self.suburb}, {self.state}, {self.postcode}'

class Category(models.Model):
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category


class Size(models.Model):
    size = models.CharField(max_length=50)
    def __str__(self):
        return self.size
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products_by_category')
    title = models.CharField(max_length=150)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True, related_name='products_by_size')
    detail = models.TextField(null=True)
    price = models.FloatField()

    def __str__(self):
        return self.title


class ProductRating(models.Model):
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name ='rating_customers')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name ='product_ratings') 
    rating = models.IntegerField()
    reviews = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.rating} - {self.reviews}'
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product}"

class Order(models.Model):
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    order_items = models.ManyToManyField(OrderItem)
    ordertime = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField(null=True, blank=True)
    address = models.ForeignKey(CustomerAddress, on_delete=models.SET_NULL, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.phone_number:
            self.phone_number = self.customer.mobile
        if not self.email:
            self.email = self.customer.email
        self.total_price = sum([item.product.price * item.quantity for item in self.order_items.all()])
        super().save(*args, **kwargs)


    def __str__(self):
        return f'Order for {self.customer.user.username} at {self.ordertime}'
    

