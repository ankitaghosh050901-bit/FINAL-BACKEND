from rest_framework import serializers
from django.contrib.auth.models import User
from datetime import date
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
from .models import FitnessGoal

class FitnessGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessGoal
        fields = '__all__'
        read_only_fields = ['user']
        
from .models import ActivityLog

class ActivityLogSerializer(serializers.ModelSerializer):
    date = serializers.DateField(required=True)
    class Meta:
        model = ActivityLog
        fields = '__all__'
        read_only_fields = ['user']
    def validate_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("Future dates are not allowed.")
        return value
        
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        read_only_fields = ['user']



