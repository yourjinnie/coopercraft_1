from django.db import models


class Collection(models.Model):
    collection=models.CharField(max_length=100)
    # slug=models.CharField(max_length=100,default=1)
    # status = models.BooleanField(default=False, help_text="0=default 1=Hidden")
    collection_image=models.ImageField(upload_to='images/')
    url = models.URLField(default="https://example.com")


    def __str__(self):
        return self.collection






