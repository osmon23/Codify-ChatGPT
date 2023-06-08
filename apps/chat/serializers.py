from rest_framework import serializers

from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    answer = serializers.ReadOnlyField()

    class Meta:
        model = Message
        fields = (
            'id',
            'question',
            'answer',
            'time',
        )
