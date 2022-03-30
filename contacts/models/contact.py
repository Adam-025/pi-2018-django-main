from django.db import models
from django.contrib.auth.models import User
from addresses.models.address import Address


class Contact(models.Model):
    objects = models.Manager()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=300)
    second_name = models.CharField(max_length=300)
    phone = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)


