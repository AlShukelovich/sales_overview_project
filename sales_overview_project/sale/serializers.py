from django.contrib.auth.models import User

from .models import Sale
from rest_framework import serializers


class SaleSerializer(serializers.ModelSerializer):
    """
    This serializer to get data about sales
    """

    class Meta:
        model = Sale
        fields = "__all__"


class SalesToUsersSerializer(serializers.HyperlinkedModelSerializer):
    """
    This serializer to get data about sales
    """
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Sale
        fields = "__all__"