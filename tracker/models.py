from django.db import models
from django.contrib.auth.models import User

class FitnessGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    step_goal = models.IntegerField()
    calorie_goal = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
class ActivityLog(models.Model):
    ACTIVITY_CHOICES = [
        ('walking', 'Walking'),
        ('running', 'Running'),
        ('cycling', 'Cycling'),
        ('gym', 'Gym'),
        ('yoga', 'Yoga'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_CHOICES)
    steps = models.IntegerField()
    calories_burned = models.IntegerField()
    duration = models.IntegerField(help_text="Duration in minutes")
    date = models.DateField() 

    def __str__(self):
        return f"{self.user.username} - {self.activity_type}"
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_weight = models.FloatField()
    target_weight = models.FloatField()
    height = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

