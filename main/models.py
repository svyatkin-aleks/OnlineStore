from django.db import models
from django.urls import reverse
from django.contrib.auth import  get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(blank=True, help_text='150x150px', verbose_name='Ссылка картинки')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name', 'price')
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product_list_by_category',
                       args=[self.slug])


class BasketProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name='Customer', on_delete=models.CASCADE)
    basket = models.ForeignKey('Basket', on_delete=models.CASCADE, related_name='related_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "Product in Basket {}".format(self.product.name)


class Basket(models.Model):

    owner = models.ForeignKey('Customer', on_delete=models.CASCADE)
    products = models.ManyToManyField(BasketProduct, blank=True, related_name='related_basket')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.id)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    adress = models.CharField(max_length=20)

    def __str__(self):
        return "Customer: {} {}".format(self.user.first_name, self.user_last_name)