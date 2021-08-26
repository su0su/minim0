from django.db import models

# Create your models here.
class Upload(models.Model):
    title = models.TextField(max_length=40, null=True)
    image = models.ImageField(null=True, upload_to="images/%Y/%m/%d", blank=True)
    keyword = models.TextField(null=True)
    media = models.TextField(null=True)
    url = models.URLField(null=True)

    def __str__(self):
        return self.title