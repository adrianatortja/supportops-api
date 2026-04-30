from django.urls import path
from .views import TicketListCreateView, TicketDetailView, SuggestedReplyView, TicketAnalyticsView


urlpatterns = [
    path('', TicketListCreateView.as_view(), name='ticket-list-create'),
    path('analytics/', TicketAnalyticsView.as_view(), name='ticket-analytics'),
    path('<int:pk>/', TicketDetailView.as_view(), name='ticket-detail'),
    path('<int:pk>/suggested-reply/', SuggestedReplyView.as_view(), name='ticket-suggested-reply'),
]
