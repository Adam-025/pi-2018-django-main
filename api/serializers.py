from django.contrib.auth.models import User
from rest_framework import serializers, viewsets


class DualSerializerViewSet(viewsets.ModelViewSet, viewsets.ViewSet):

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class UserSerializer(serializers.ModelSerializer):

    created_at = serializers.CharField(source='date_joined')

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff', 'is_superuser', 'created_at']
