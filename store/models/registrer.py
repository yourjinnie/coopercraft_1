from django.db import models

class Register(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    confirm_password=models.CharField(max_length=200)

    def __str__(self):
        return self.name