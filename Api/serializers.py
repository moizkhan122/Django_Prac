
#serializer is for to convert model into json

from rest_framework import serializers
from Api.models import CompanyModel

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=CompanyModel
        fields=['name','location','about','type','added_date','active'] #import all fields of company model

