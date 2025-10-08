# myapp1/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contact_list, name='contacts-list'),
    path('contacts/new/', views.contact_create, name='contacts-create'),
    path('contacts/<int:pk>/', views.contact_detail, name='contacts-detail'),
    path('contacts/<int:pk>/edit/', views.contact_update, name='contacts-update'),
    path('contacts/<int:pk>/delete/', views.contact_delete, name='contacts-delete'),
]
