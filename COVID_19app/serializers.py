from rest_framework import serializers
from .models import Doctor, Patient, Report

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
