from .models import Preference
from .serializer import PreferenceSerializer
from rest_framework import viewsets, permissions

class PreferenceViewSet(viewsets.ModelViewSet):
    queryset = Preference.objects.all()
    serializer_class = PreferenceSerializer
    permission_classes = [permissions.IsAuthenticated]
