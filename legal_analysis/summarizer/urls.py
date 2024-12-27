from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_document, name='upload_document'),
    path('summary/<int:pk>/', views.summary_view, name='summary'),
]
