from rest_framework import serializers

from projects.models import Publication
from .team import TeamMemberSerializer


class PublicationSerializer(serializers.ModelSerializer):
    team_member = TeamMemberSerializer(read_only=True)  # Use the nested serializer for team_member

    class Meta:
        model = Publication
        fields = ['id', 'title', 'content', 'team_member', 'slug', 'created_time', 'updated_time']
        read_only_fields = ['id', 'created_time', 'updated_time']
