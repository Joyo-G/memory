from .models import Preference
from rest_framework import serializers

class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preference
        fields = ['id', 'user', 'course_offering', 'modality', 'priority']