from django.db import models
from django.utils import timezone

class configweather(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    web = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    cityg = models.CharField(max_length=20)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.web

class configdev(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    location =models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    ip = models.CharField(max_length=20)


    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
