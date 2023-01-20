from isup.models import Domain
from rest_framework import serializers


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id", "name", "is_up", "since", "owner"]
        model = Domain

    def perform_create(self, serializer):
        user = self.context["request"].user

        if user.is_authenticated:
            serializer.save(owner=user)
        else:
            serializer.save()
