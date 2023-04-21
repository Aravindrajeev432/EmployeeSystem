from rest_framework import serializers

from right.serializers import RightSerializer
from .models import Roles

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'

class RoleViewSerializer(serializers.ModelSerializer):
    rights = RightSerializer(many=True)
    class Meta:
        model = Roles
        fields = '__all__'
