from django.urls import path
from .views import register_user, fitness_goal_list_create, fitness_goal_update_delete,activity_log_list_create,activity_log_update_delete,progress_summary, user_profile_view

urlpatterns = [
    path('register/', register_user),

    # Fitness Goal Routes
    path('goals/', fitness_goal_list_create),
    path('goals/<int:id>/', fitness_goal_update_delete),
    # Activity Log Routes
    path('logs/', activity_log_list_create),
    path('logs/<int:id>/', activity_log_update_delete),
    path('progress/', progress_summary),
    path('profile/', user_profile_view),


    
]
