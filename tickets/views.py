from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Ticket
from .serializers import TicketSerializer
from .services import generate_suggested_reply


class TicketListCreateView(generics.ListCreateAPIView):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)


class SuggestedReplyView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        ticket = Ticket.objects.get(pk=pk, user=request.user)
        suggested_reply = generate_suggested_reply(ticket.category)

        return Response({
            'ticket_id': ticket.id,
            'category': ticket.category,
            'priority': ticket.priority,
            'suggested_reply': suggested_reply,
        })


class TicketAnalyticsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tickets = Ticket.objects.filter(user=request.user)

        return Response({
            'total_tickets': tickets.count(),
            'open_tickets': tickets.filter(status='open').count(),
            'pending_tickets': tickets.filter(status='pending').count(),
            'closed_tickets': tickets.filter(status='closed').count(),
            'high_priority_tickets': tickets.filter(priority='high').count(),
            'medium_priority_tickets': tickets.filter(priority='medium').count(),
            'low_priority_tickets': tickets.filter(priority='low').count(),
            'refund_tickets': tickets.filter(category='refund').count(),
            'shipping_tickets': tickets.filter(category='shipping').count(),
            'technical_tickets': tickets.filter(category='technical').count(),
            'general_tickets': tickets.filter(category='general').count(),
        })
        