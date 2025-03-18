from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Patient, Doctor, PatientDoctorMapping
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    name = serializers.CharField(source='first_name', required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        email = validated_data.pop('email')
        name = validated_data.pop('first_name')
        user = User.objects.create_user(username=email, email=email, first_name=name, **validated_data)
        return user
    
class EmailLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({"error": "Invalid email or password"})

        user = authenticate(username=user.username, password=password)
        if not user:
            raise serializers.ValidationError({"error": "Invalid email or password"})

        attrs['user'] = user
        return attrs
    
    
class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = ["id", "p_user", "name", "age", "phone", "address"]


class DoctorSerializer(serializers.ModelSerializer):
    d_user = UserSerializer(read_only=True)

    class Meta:
        model = Doctor
        fields = ["id", "d_user", "name", "specialization", "phone"]


class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient_id = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all(), source="patient", write_only=True
    )
    doctor_id = serializers.PrimaryKeyRelatedField(
        queryset=Doctor.objects.all(), source="doctor", write_only=True
    )

    patient = serializers.SerializerMethodField()
    doctor = serializers.SerializerMethodField()

    class Meta:
        model = PatientDoctorMapping
        fields = ["id", "patient_id", "doctor_id", "patient", "doctor"]

    def get_patient(self, obj):
        return {"id": obj.patient.id, "name": obj.patient.name}

    def get_doctor(self, obj):
        return {"id": obj.doctor.id, "name": obj.doctor.name}