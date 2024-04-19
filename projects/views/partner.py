from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from projects.models import Partner
from projects.serializers import PartnerSerializer


class PartnerView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Partner.objects.all()
        serializer = PartnerSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
