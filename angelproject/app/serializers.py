from rest_framework import serializers
from .models import *

class CompanyNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = company_name
        fields = ['company_name']

class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = options
        fields = ['ce', 'pe']

class ExpiryPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = options
        fields = ['ce', 'pe']        