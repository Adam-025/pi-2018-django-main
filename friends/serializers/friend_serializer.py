from contacts.serializers.contact_serializer import ContactSerializerPopulated, ContactSerializer
from friends.models.friend import Friend
from rest_framework import serializers


class FriendSerializer(serializers.ModelSerializer):

    class Meta:
        model = Friend
        fields = '__all__'


class FriendSerializerPopulated(serializers.ModelSerializer):

    first_contact = ContactSerializer()
    second_contact = ContactSerializer()

    class Meta:
        model = Friend
        fields = '__all__'


class FriendSerializerPopulatedContactPopulated(serializers.ModelSerializer):

    first_contact = ContactSerializerPopulated()
    second_contact = ContactSerializerPopulated()

    foo = serializers.SerializerMethodField()

    @staticmethod
    def get_foo(obj):
        return f"Foo id: {obj.pk}"

    class Meta:
        model = Friend
        fields = '__all__'
