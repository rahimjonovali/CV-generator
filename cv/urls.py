from django.urls import path
from . import views

urlpatterns = [
    path('', views.CVCreateView.as_view(), name='create_cv'),
    path('cvs/', views.CVListView.as_view(), name='cv_list'),
    path('cv/<int:pk>/pdf/', views.generate_pdf, name='cv_pdf'),
]
