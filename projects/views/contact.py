from django.conf import settings
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from projects.models import ContactInformation, Service
from projects.serializers import ContactInformationSerializer
from projects.serializers.contact import ContactFormViewSerializer
from projects.serializers.service import ServiceSerializer


class ContactInformationView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = ContactInformation.objects.all()
        serializer = ContactInformationSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ContactAPIView(APIView):
    serializer_class = ContactFormViewSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Send the feedback as an email using Django's built-in email functionality
            email_subject = 'Обратная связь: ' + str(serializer.validated_data['email'])

            # Create the email body as a table
            email_body = """
            <table border="1" cellpadding="5">
                <tr>
                    <td><strong>Имя</strong></td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td><strong>Фамилия</strong></td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td><strong>Email</strong></td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td><strong>Сообщение</strong></td>
                    <td>{}</td>
                </tr>
            </table>
            """.format(
                serializer.validated_data['first_name'],
                serializer.validated_data['last_name'],
                serializer.validated_data['email'],
                serializer.validated_data['message']
            )

            try:
                send_mail(
                    email_subject,
                    email_body,
                    settings.EMAIL_HOST_USER,
                    ['info@advocateabf.com'],  # Sending to the same email as the sender for testing purposes
                    fail_silently=False,
                    html_message=email_body  # Set the email_body as the HTML content
                )
            except Exception as e:
                print("Error sending email:", e)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
