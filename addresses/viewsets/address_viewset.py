from api.serializers import DualSerializerViewSet
from addresses.models.address import Address
from rest_framework.response import Response
from addresses.serializers.address_serializer import AddressSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action


class AddressViewSet(DualSerializerViewSet):
    queryset = Address.objects.all()

    default_serializer_class = AddressSerializer

    serializer_classes = {
        'create': AddressSerializer,
        'update': AddressSerializer
    }

    def list(self, request, **kwargs):
        serializer_context = {'request': request}
        serializer = AddressSerializer(self.queryset, many=True, context=serializer_context)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        serializer_context = {'request': request}
        address = get_object_or_404(self.queryset, pk=pk)
        serializer = AddressSerializer(address, many=False, context=serializer_context)
        return Response(serializer.data)

    # def get(self, request):
    #     return Response()

    @action(methods=['post'], detail=True, permission_classes=[IsAdminUser])
    def post(self, request):
        return Response()

