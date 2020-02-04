from dashboard import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='dashboard-home'),
    path('about/', views.about, name='dashboard-about'),
    ]