from django.db.models import Q
from rest_framework.exceptions import APIException

from api.serializers import DualSerializerViewSet
from friends.models.friend import Friend
from rest_framework import viewsets
from rest_framework.response import Response
from friends.serializers.friend_serializer import FriendSerializer, FriendSerializerPopulatedContactPopulated
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action


class FriendViewSet(DualSerializerViewSet):
    queryset = Friend.objects.prefetch_related('first_contact', 'second_contact', 'first_contact__user', 'second_contact__user').all()

    serializer_classes = {
        'create': FriendSerializer,
        'update': FriendSerializer
    }

    default_serializer_class = FriendSerializerPopulatedContactPopulated

    def list(self, request, **kwargs):
        serializer_context = {'request': request}
        serializer = FriendSerializer(self.queryset, many=True, context=serializer_context)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, permission_classes=[IsAdminUser])
    def get(self, request):
        return Response()

    @action(methods=['post'], detail=True, permission_classes=[IsAdminUser])
    def post(self, request):
        return Response()

    def create(self, request, *args, **kwargs):
        first_contact_id = request.data.get('first_contact')
        second_contact_id = request.data.get('second_contact')
        friend_exists = Friend.objects.filter(Q(first_contact_id=first_contact_id,
                                                second_contact_id=second_contact_id) |
                                              Q(first_contact_id=second_contact_id,
                                                second_contact_id=first_contact_id)).exists()
        if friend_exists:
            raise APIException("Friend already exists")

        return super(FriendViewSet, self).create(request, *args, **kwargs)
