from django.urls import path
from .api_views import CVListCreateAPIView, CVDetailAPIView

urlpatterns = [
    path('cvs/', CVListCreateAPIView.as_view(), name='api_cv_list'),
    path('cvs/<int:pk>/', CVDetailAPIView.as_view(), name='api_cv_detail'),
]
