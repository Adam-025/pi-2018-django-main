from addresses.serializers.address_serializer import AddressSerializer
from api.serializers import UserSerializer
from contacts.models.contact import Contact
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'


class ContactSerializerPopulated(serializers.ModelSerializer):

    user = UserSerializer()
    address = AddressSerializer()

    class Meta:
        model = Contact
        fields = '__all__'


