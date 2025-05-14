from django.shortcuts import render
from rest_framework import viewsets
from .serializers import studentSerializers
from .models import studentModel
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class studentViewSet(viewsets.ModelViewSet):
    queryset = studentModel.objects.all()
    serializer_class = studentSerializers
    permission_classes = [IsAuthenticated]