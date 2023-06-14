from rest_framework import serializers
from myshop.models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Detail
        fields = '__all__'
