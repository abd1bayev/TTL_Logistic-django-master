from rest_framework import serializers

from projects.models.contact import ContactInformation


class ContactInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInformation
        fields = ['id', 'country', 'city', 'address', 'phone_number', 'email', 'landmark', 'latitude', 'longitude']
        read_only_fields = ['id']