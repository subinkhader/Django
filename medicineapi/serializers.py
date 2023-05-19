from rest_framework import serializers
from store.models import Medicinedetails
from django.contrib.auth.models import User


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicinedetails
        fields = '__all__'
        

        
class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
    def create(self, validated_data):
        user = User.objects.create_superuser(**validated_data)
        return user
        