from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RecordedCall(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meeting_id = models.CharField(max_length=50)
    date_time = models.CharField(max_length=500)
    duration = models.CharField(max_length=50)
    #recording_file = models.CharField(max_length=50000)

    def __str__(self):
        return (self.meeting_id)
