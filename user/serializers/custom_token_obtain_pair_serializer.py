from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        credentials = {
            "phone_number": attrs.get("phone_number"),
            "password": attrs.get("password"),
        }
        if all(credentials.values()):
            user = authenticate(request=self.context.get("request"), **credentials)

            if not user:
                raise serializers.ValidationError(
                    _("No active account found with the given credentials")
                )
        else:
            raise serializers.ValidationError(_('Must include "email" and "password".'))

        refresh = self.get_token(user)

        data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["name"] = user.first_name
        return token
