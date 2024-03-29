from rest_framework import serializers
from .models import *


class CompanySerializer(serializers.ModelSerializer) :
    class Meta :
        model = Company
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer): 
    company = CompanySerializer()   
    class Meta :
        model = File
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    class Meta :
        model = User
        fields = '__all__'        