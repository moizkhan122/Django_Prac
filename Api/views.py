from django.shortcuts import render
from .models import CompanyModel
from .serializers import CompanySerializer

#viewsets have all default crud operations methods
# Create your views here.

                    #use for CRUD operations
from rest_framework.generics import ListAPIView #listApiView is for to call get Api
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView

class ListProductApiView(ListAPIView):
    queryset= CompanyModel.objects.all()
    #send after serialize
    serializer_class=CompanySerializer

class CreateProductApiView(CreateAPIView):
    queryset= CompanyModel.objects.all()
    #send after serialize
    serializer_class=CompanySerializer

class UpdateProductApiView(UpdateAPIView):
    queryset= CompanyModel.objects.all()
    #send after serialize
    serializer_class=CompanySerializer

class DeleteProductApiView(DestroyAPIView):
    queryset= CompanyModel.objects.all()
    #send after serialize
    serializer_class=CompanySerializer