from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import GpsDataSerializer
from .models import GpsData

class GpsView(APIView):
      def get(self, request):
         gps_data = GpsData.objects.all()
         serializer = GpsDataSerializer(gps_data, many=True)
         return Response(serializer.data)
   
      def post(self, request):
         serializer = GpsDataSerializer(data=request.data)
         if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)