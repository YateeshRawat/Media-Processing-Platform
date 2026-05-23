import uuid
from django.db import models
from django.contrib.auth.models import User

class ProcessingTask(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )

    TASK_TYPES = (
        ('text_summarization', 'Text Summarization'),
        ('sentiment_analysis', 'Sentiment Analysis'),
        ('image_captioning', 'Image Caption Generation'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    task_type = models.CharField(max_length=50, choices=TASK_TYPES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    input_data = models.JSONField(help_text="Input data for the processing task")
    result_data = models.JSONField(null=True, blank=True, help_text="Result of the processing task")
    error_message = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.task_type} - {self.id} ({self.status})"
