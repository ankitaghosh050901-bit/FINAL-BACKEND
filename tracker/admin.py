from django.contrib import admin
from .models import FitnessGoal, ActivityLog,UserProfile

admin.site.register(FitnessGoal)
admin.site.register(ActivityLog)
admin.site.register(UserProfile)