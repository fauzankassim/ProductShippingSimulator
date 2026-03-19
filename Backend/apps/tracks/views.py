from .models import Track
from rest_framework import permissions, viewsets
from .serializers import TrackSerializers

# Create your views here.
class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializers
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(courier_id=self.request.user)