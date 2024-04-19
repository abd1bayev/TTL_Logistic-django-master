from rest_framework import serializers


class TeamMemberSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    patronymic = serializers.CharField(max_length=100)
    position = serializers.CharField(max_length=100)
    sphere_of_activity = serializers.CharField()
    education = serializers.CharField()
    scientific_degree = serializers.CharField()
    legal_practice = serializers.CharField()
    license = serializers.CharField(max_length=100)
    membership = serializers.CharField(max_length=100)
    languages = serializers.CharField()
    image = serializers.ImageField()
    slug = serializers.SlugField(max_length=400)
