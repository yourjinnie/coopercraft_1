from django.db import models
from store.models.register import Register
from store.models.products import Product
import datetime


class Order(models.Model):
    customer = models.ForeignKey(Register, on_delete=models.CASCADE,default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,default=1)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    fname = models.CharField(max_length=50, default='default_first_name')
    lname = models.CharField(max_length=50, default='default_last_name')
    company_name = models.CharField(max_length=100, default='default_company_name')
    email = models.EmailField(default='default@example.com')
    # address = models.CharField(max_length=255, default='default_address')
    address_line_1 = models.CharField(max_length=255,default='default_address')
    address_line_2 = models.CharField(max_length=255, blank=True, null=True,default='default_address')
    city = models.CharField(max_length=100, default='default_city')
    zipcode = models.CharField(max_length=20, default='default_postal_code')
    country = models.CharField(max_length=100, default='default_country')
    phone_no = models.CharField(max_length=15, default='000-000-0000')
    date = models.DateField(default=datetime.datetime.today())
    status = models.BooleanField(default=False)


    def place_order(self):
        self.save()
        return self  # Returning the saved order instance

    def __str__(self):
        return f"{self.customer} - {self.product} - {self.quantity}"

    @staticmethod
    def get_order_by_customer(user_id):
        return Order \
            .objects \
            .filter(customer=user_id) \
            .order_by('-date')