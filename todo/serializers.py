from rest_framework import serializers
from .models import Todo , a 
from django.contrib.auth.models import User




class TodoSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=Todo
        fields='__all__'

class ASerializers(serializers.ModelSerializer):
    class Meta:
        model=a
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    qwe=TodoSerializers(read_only=True , many=True)
    class Meta:
        model=User
        fields='__all__'


 