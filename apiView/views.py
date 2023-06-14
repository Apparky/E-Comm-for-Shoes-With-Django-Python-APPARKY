from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import *
from myshop.models import *

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product_Detail.objects.all()
    serializer_class = ProductSerializer
