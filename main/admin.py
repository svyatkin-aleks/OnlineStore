from django.contrib import admin
from .models import Category, Product, BasketProduct, Basket, Customer


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created']
    list_filter = ['available', 'created', 'price']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)

admin.site.register(BasketProduct)
admin.site.register(Basket)
admin.site.register(Customer)

