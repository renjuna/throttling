from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.

from rest_framework.response import Response

class ExampleView(APIView):

    def get(self, request, format=None):
        # Write your code here
        return Response({'Hello World'})
