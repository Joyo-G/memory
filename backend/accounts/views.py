from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Docencia, Docente, User
from .serializer import DocenteSerializer, UserSerializer, DocenciaSerializer

class DocenteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows docentes to be viewed or edited.
    """
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class DocenciaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows docencias to be viewed or edited.
    """
    queryset = Docencia.objects.all()
    serializer_class = DocenciaSerializer
    permission_classes = [permissions.IsAuthenticated]
