from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Doctor, Patient, Report
from .serializers import DoctorSerializer, PatientSerializer, ReportSerializer

@api_view(['POST'])
def doctor_register(request):
    serializer = DoctorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def doctor_login(request):
    pass

@api_view(['POST'])
def patient_register(request):
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_patient_report(request, patient_id):
    doctor = request.user  
    try:
        patient = Patient.objects.get(id=patient_id)
    except Patient.DoesNotExist:
        return Response({'error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ReportSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(doctor=doctor, patient=patient)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_patient_reports(request, patient_id):
    try:
        patient = Patient.objects.get(id=patient_id)
    except Patient.DoesNotExist:
        return Response({'error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)
    
    reports = Report.objects.filter(patient=patient).order_by('created_date')
    serializer = ReportSerializer(reports, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_reports_by_status(request, status):
    reports = Report.objects.filter(status=status)
    serializer = ReportSerializer(reports, many=True)
    return Response(serializer.data)
