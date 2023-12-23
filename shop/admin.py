from django.contrib import admin
from . import models

class PostcodeAdmin(admin.ModelAdmin):
    search_fields = ['postcode', ]
    list_display = ("postcode", "locality", "state", "type")
admin.site.register(models.Postcode, PostcodeAdmin)

class SuburbAdmin(admin.ModelAdmin):
    search_fields = ['locality', ]
    list_display = ("locality", "postcode", "state", "type")  
admin.site.register(models.Suburb, SuburbAdmin)
#State
class StateAdmin(admin.ModelAdmin):
    search_fields = ['state',]  # Search by user's name, profile name, mobile, or email
    list_display = ("state",)
    
admin.site.register(models.State, StateAdmin)
# Customer Address
class CustomerAddressAdmin(admin.ModelAdmin):
    search_fields = ["houseNumber","streetName","suburb","state","postcode"]
    autocomplete_fields = ["postcode", "suburb"]
    list_display = ("houseNumber","streetName","suburb","state","postcode")
admin.site.register(models.CustomerAddress, CustomerAddressAdmin)

# Category
admin.site.register(models.Category)
# Size
admin.site.register(models.Size)

# Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ("category","title","title","detail","price")
admin.site.register(models.Product, ProductAdmin)
# Order
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer","ordertime")
admin.site.register(models.Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    search_fields = ["product",]
    list_display = ("product","quantity")
admin.site.register(models.OrderItem, OrderItemAdmin)

# Product Rating
class ProductRatingAdmin(admin.ModelAdmin):
    list_display = ("customer","product","rating","reviews","add_time")
admin.site.register(models.ProductRating, ProductRatingAdmin)