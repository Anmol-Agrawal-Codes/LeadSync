from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('leads/', views.lead_page, name='leads'),
    path('lead_details/<str:pk>/', views.lead_detail, name='lead-details'),
    path('create_lead/', views.create_lead, name='create-lead'),
    path('update_lead/<str:pk>', views.update_lead, name='update-lead'),
    path('delete_lead/<str:pk>', views.delete_lead, name='delete-lead')
]