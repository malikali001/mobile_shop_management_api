from rest_framework import generics

from base.models import CustomUser
from user.permissions import IsAdmin, IsAdminOrOwner
from user.serializers import CustomUserSerializer


class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdmin]


class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_permissions(self):
        if self.request.method in ("GET", "PATCH", "PUT"):
            return [IsAdminOrOwner()]
        return [IsAdmin()]
