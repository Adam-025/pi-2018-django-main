from django.contrib import admin
from contacts.models.contact import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

