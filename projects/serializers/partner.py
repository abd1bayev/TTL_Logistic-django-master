from rest_framework import serializers


class PartnerSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    image = serializers.ImageField(allow_empty_file=True, required=False)
    url = serializers.URLField()
