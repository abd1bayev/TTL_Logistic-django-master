from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response

from projects.models import TeamMember
from projects.serializers import TeamMemberSerializer
from projects.utils import TeamPagination


class TeamMemberListView(ListAPIView):
    queryset = TeamMember.objects.all().select_related()
    serializer_class = TeamMemberSerializer
    pagination_class = TeamPagination

    @swagger_auto_schema(
        operation_description="Get a list of Team Members",
        responses={200: TeamMemberSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(
            queryset,
        )
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class TeamMemberDetailView(RetrieveAPIView):
    queryset = TeamMember.objects.all().select_related()
    serializer_class = TeamMemberSerializer
    lookup_field = 'slug'

    @swagger_auto_schema(
        operation_description="Get details of a team member by slug",
        responses={
            status.HTTP_200_OK: TeamMemberSerializer(),
            status.HTTP_404_NOT_FOUND: "Team member not found"
        },
        manual_parameters=[
            openapi.Parameter(
                'slug',
                openapi.IN_PATH,
                description="Slug of the team member",
                type=openapi.TYPE_STRING
            )
        ]
    )
    def get(self, request, slug, *args, **kwargs):
        try:
            team_member = self.get_object()
        except TeamMember.DoesNotExist:
            return Response({"error": "Team member not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(team_member)
        return Response(serializer.data)
