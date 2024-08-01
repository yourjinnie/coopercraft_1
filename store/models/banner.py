from django.db import models

class Banner(models.Model):
    banner_title = models.CharField(max_length=255, blank=True, null=True)
    banner_description = models.TextField(blank=True, null=True)
    banner_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.banner_title
