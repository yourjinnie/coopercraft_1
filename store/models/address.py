from django.db import models
from store.models.register import Register

class Address(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=50)  # 'billing' or 'shipping'
    first_name = models.CharField(max_length=100,default='default_first_name')
    last_name = models.CharField(max_length=100, default='default_last_name')
    company_name = models.CharField(max_length=100, default='default_company_name')
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.address_type} - {self.user.name}"
