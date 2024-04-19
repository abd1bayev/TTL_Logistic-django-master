from rest_framework import serializers


class ReviewSerializer(serializers.Serializer):
    service_id = serializers.IntegerField()
    full_name = serializers.CharField(max_length=50)
    description = serializers.CharField()
    file = serializers.FileField()
    is_active = serializers.BooleanField()
    guid = serializers.UUIDField(read_only=True)
    created_time = serializers.DateTimeField(read_only=True)
    updated_time = serializers.DateTimeField(read_only=True)
