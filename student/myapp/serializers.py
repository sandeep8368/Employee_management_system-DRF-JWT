from rest_framework import serializers
from .models import studentModel

class studentSerializers(serializers.ModelSerializer):
    class Meta:
        model = studentModel
        fields = '__all__'
        