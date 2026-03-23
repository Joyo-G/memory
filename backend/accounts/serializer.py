from .models import Docente, User, Docencia
from rest_framework import serializers

class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = ['user_id', 'teaching_quota', 'work_schedule']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name','rut','is_active']

class DocenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docencia
        fields = ['user_id']