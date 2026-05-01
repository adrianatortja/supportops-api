from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User
from .models import Ticket


class TicketAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123"
        )

        self.client.force_authenticate(user=self.user)

    def test_user_can_create_ticket(self):
        response = self.client.post("/api/tickets/", {
            "subject": "Where is my order?",
            "message": "My order has not arrived yet.",
            "status": "open"
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        self.assertEqual(Ticket.objects.count(), 1)
        self.assertEqual(Ticket.objects.first().user, self.user)
        self.assertEqual(Ticket.objects.first().subject, "Where is my order?")

    def test_user_can_list_only_their_own_tickets(self):
        other_user = User.objects.create_user(
            username="otheruser",
            email="other@example.com",
            password="testpass123"
        )

        Ticket.objects.create(
            user=self.user,
            subject="My ticket",
            message="This ticket belongs to me",
            status="open"
        )

        Ticket.objects.create(
            user=other_user,
            subject="Other user ticket",
            message="This ticket belongs to another user",
            status="open"
        )

        response = self.client.get("/api/tickets/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["subject"], "My ticket")

    def test_user_can_retrieve_ticket_detail(self):
        ticket = Ticket.objects.create(
            user=self.user,
            subject="Detail ticket",
            message="Testing ticket detail endpoint",
            status="open"
        )

        response = self.client.get(f"/api/tickets/{ticket.id}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], ticket.id)
        self.assertEqual(response.data["subject"], "Detail ticket")

    def test_suggested_reply_returns_404_for_invalid_ticket(self):
        response = self.client.get("/api/tickets/999/suggested-reply/")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_analytics_endpoint_returns_correct_counts(self):
        Ticket.objects.create(
            user=self.user,
            subject="Refund request",
            message="I need a refund for my order",
            status="open"
        )

        Ticket.objects.create(
            user=self.user,
            subject="Shipping delay",
            message="My package has not arrived",
            status="closed"
        )

        response = self.client.get("/api/tickets/analytics/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["total_tickets"], 2)
        self.assertEqual(response.data["open_tickets"], 1)
        self.assertEqual(response.data["closed_tickets"], 1)