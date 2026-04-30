from rest_framework import serializers
from .models import Ticket
from .services import categorize_ticket, detect_priority


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            'id',
            'user',
            'subject',
            'message',
            'status',
            'priority',
            'category',
            'created_at',
        ]
        read_only_fields = ['id', 'user', 'created_at', 'category', 'priority']

    def create(self, validated_data):
        message = validated_data.get('message', '')

        validated_data['category'] = categorize_ticket(message)
        validated_data['priority'] = detect_priority(message)

        return super().create(validated_data)
    