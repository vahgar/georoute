from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from accounts.api.serializers import UserCreateSerializer, UserUpdateSerializer
from accounts.models import CustomUser


class UserCreateAPIView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer

    permission_classes = [AllowAny]


class UserListAPIView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer

class UserDetailAPIView(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer

class UserUpdateAPIView(UpdateAPIView,RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserUpdateSerializer

class UserDeleteAPIView(DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer
