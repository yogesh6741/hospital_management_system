from django.urls import path
from . import views

urlpatterns = [
    path('doctors/register', views.doctor_register),
    path('doctors/login', views.doctor_login),
    path('patients/register', views.patient_register),
    path('patients/<int:patient_id>/create_report', views.create_patient_report),
    path('patients/<int:patient_id>/all_reports', views.get_all_patient_reports),
    path('reports/<str:status>', views.get_all_reports_by_status),
]
