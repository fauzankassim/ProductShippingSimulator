from .models import Status, Track
from rest_framework import serializers

class TrackSerializers(serializers.ModelSerializer):

    class Meta:
        model = Track
        fields = ["id", "transaction_id", "courier_id", "status_id", "created_at"]
        read_only_fields = [ "courier_id", "created_at"]