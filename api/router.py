from rest_framework.routers import DefaultRouter

router = DefaultRouter()


def register_route(prefix, viewset, base_name=None):
    router.register(prefix, viewset, basename=base_name)
