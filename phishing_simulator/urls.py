from django.urls import path
from . import views
from .admin import custom_admin_site

urlpatterns = [
    path('', views.home, name='home'),  # Add the home view

    # URLs for phishing_attempt success and failure pages
    path('phishing_attempt/', views.phishing_attempt, name='phishing_attempt'),
    path('phishing_attempt/success/', views.phishing_success, name='phishing_success'),
    path('phishing_attempt/failure/', views.phishing_failure, name='phishing_failure'),

    # URLs for Smishing (SMS Phishing) success and failure pages
    path('smishing/', views.smishing, name='smishing'),
    path('smishing/success/', views.smishing_success, name='smishing_success'),
    path('smishing/failure/', views.smishing_failure, name='smishing_failure'),

    # URLs for Pharming success and failure pages
    path('pharming/', views.pharming, name='pharming'),
    path('pharming/success/', views.pharming_success, name='pharming_success'),
    path('pharming/failure/', views.pharming_failure, name='pharming_failure'),

    # URLs for CEO Fraud (Business Email Compromise) success and failure pages
    path('ceo_fraud/', views.ceo_fraud, name='ceo_fraud'),
    path('ceo_fraud/success/', views.ceo_fraud_success, name='ceo_fraud_success'),
    path('ceo_fraud/failure/', views.ceo_fraud_failure, name='ceo_fraud_failure'),
    
    # Define your custom admin dashboard URL pattern first
    path('dashboard/', views.custom_admin_dashboard, name='custom_admin_dashboard'),

    path('customadmin/', custom_admin_site.urls),
]
