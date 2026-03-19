from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls))
]