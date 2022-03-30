from django.db import models


class Address(models.Model):
    objects = models.Manager()

    street = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    country = models.CharField(max_length=30)
    code = models.CharField(max_length=6)

    @classmethod
    def get_address_title(cls):
        return f'{cls.country} {cls.city} {cls.street} {cls.code}'
