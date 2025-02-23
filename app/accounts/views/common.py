from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, RetrieveAPIView

from accounts.models import CustomUser
from accounts.serializers import UserListSerializer, UserDetailSerializer


@extend_schema(tags=["users"])
class UserListView(ListAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = UserListSerializer


@extend_schema(tags=["users"])
class UserDetailView(RetrieveAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = "username"
