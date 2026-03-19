from .models import Product
from rest_framework import permissions, viewsets
from .serializers import ProductSerializers

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(merchant=self.request.user)