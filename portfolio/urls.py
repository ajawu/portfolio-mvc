from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.LandingView.as_view(), name='landing_page'),
    path('resume/', views.ResumeView.as_view(), name='resume_download'),
    path('contact/', views.ResumeView.as_view(), name='contact_me'),
]
