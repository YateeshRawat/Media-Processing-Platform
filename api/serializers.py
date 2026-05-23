from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ProcessingTask

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

class ProcessingTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessingTask
        fields = ('id', 'task_type', 'status', 'input_data', 'result_data', 'error_message', 'created_at', 'updated_at')
        read_only_fields = ('id', 'status', 'result_data', 'error_message', 'created_at', 'updated_at')
