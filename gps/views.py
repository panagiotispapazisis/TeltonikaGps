from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class GpsView(APIView):
    def post(self, request):
        print(request.data)
        return Response(status=status.HTTP_200_OK)