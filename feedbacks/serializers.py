from rest_framework import serializers
from .models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ["id", "rating", "description", "owner"]
        read_only_fields = ["owner"]
        extra_kwargs = {"description": {"allow_null": True}}
