from django.urls import path
from .views import LeadListView, LeadDeteailView, LeadCreateView, LeadUpdateView, LeadDeleteView, AssignAgentView


app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),
    path('<int:pk>/', LeadDeteailView.as_view(), name='lead-detail'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
    path('<int:pk>/assign-agent/', AssignAgentView.as_view(), name='assign-agent'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
]