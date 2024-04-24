from django.conf import settings
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from projects.models import ContactInformation
from projects.serializers import ContactInformationSerializer


class ContactInformationView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = ContactInformation.objects.all()
        serializer = ContactInformationSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



