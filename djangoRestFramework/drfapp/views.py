from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .seraliazers import StudentSerializer
from .models import Student

class TesView(APIView):
    def get(sef, request, *arg, **kwargs):
        data = {
            'username':'admin',
            'year_active': 10,
        }

        return Response(data)
    
    def post(sef, request, *arg, **kwargs):
        serializer = StudentSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)   
        return Response(serializer.errors)
    

    permission_classes = (IsAuthenticated, )