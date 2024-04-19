from rest_framework import serializers

from projects.models.contact import ContactFormView


class ContactInformationSerializer(serializers.Serializer):
    address = serializers.CharField(max_length=200)
    phone_number = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    landmark = serializers.CharField(max_length=200)
    transportation = serializers.CharField(max_length=100)


class ContactFormViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactFormView
        fields = ['id', 'first_name', 'last_name', 'email', 'message']
        read_only_fields = ['id']
