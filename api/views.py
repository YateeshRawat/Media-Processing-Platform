from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .models import ProcessingTask
from .serializers import UserSerializer, ProcessingTaskSerializer
from .tasks import process_media_task

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

class ProcessingTaskViewSet(viewsets.ModelViewSet):
    serializer_class = ProcessingTaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return ProcessingTask.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        task = serializer.save(user=self.request.user)
        process_media_task.delay(str(task.id))
