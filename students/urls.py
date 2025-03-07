from django.urls import path
from . import views

urlpatterns = [
    path('', views.appointment_list, name='appointment_list'),
    path('new/', views.appointment_create, name='appointment_create'),
    path('edit/<int:pk>/', views.appointment_update, name='appointment_update'),
    path('delete/<int:pk>/', views.appointment_delete, name='appointment_delete'),
    path('calendar/', views.appointment_calendar, name='appointment_calendar'),  # API JSON
    path('calendar/view/', views.appointment_calendar_view, name='appointment_calendar_view'),  # Página del calendario
]
