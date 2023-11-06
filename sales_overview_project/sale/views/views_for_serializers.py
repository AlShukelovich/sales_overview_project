from rest_framework import viewsets, permissions
from sale.models import Sale
from sale.serializers import SaleSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [permissions.AllowAny]
