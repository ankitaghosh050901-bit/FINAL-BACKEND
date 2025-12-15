from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import FitnessGoal, ActivityLog, UserProfile
from .serializers import RegisterSerializer, FitnessGoalSerializer, ActivityLogSerializer,  UserProfileSerializer
from .models import FitnessGoal, ActivityLog



from .serializers import RegisterSerializer, FitnessGoalSerializer
from .models import FitnessGoal


# -------------------------
# USER REGISTER API
# -------------------------
@api_view(['POST'])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User registered successfully'})
    return Response(serializer.errors, status=400)


# -------------------------
# FITNESS GOAL APIS
# -------------------------

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def fitness_goal_list_create(request):
    if request.method == 'GET':
        goals = FitnessGoal.objects.filter(user=request.user)
        serializer = FitnessGoalSerializer(goals, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = FitnessGoalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def fitness_goal_update_delete(request, id):
    try:
        goal = FitnessGoal.objects.get(id=id, user=request.user)
    except FitnessGoal.DoesNotExist:
        return Response({'error': 'Goal not found'}, status=404)

    if request.method == 'PUT':
        serializer = FitnessGoalSerializer(goal, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        goal.delete()
        return Response({'message': 'Goal deleted successfully'})
    
    
# -------------------------
# ACTIVITY LOG APIS
# -------------------------

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def activity_log_list_create(request):
    if request.method == 'GET':
        logs = ActivityLog.objects.filter(user=request.user)
        serializer = ActivityLogSerializer(logs, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ActivityLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def activity_log_update_delete(request, id):
    try:
        log = ActivityLog.objects.get(id=id, user=request.user)
    except ActivityLog.DoesNotExist:
        return Response({'error': 'Activity log not found'}, status=404)

    if request.method == 'PUT':
        serializer = ActivityLogSerializer(log, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        log.delete()
        return Response({'message': 'Activity log deleted successfully'})
    
# -------------------------
# PROGRESS TRACKING API
# -------------------------

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def progress_summary(request):
    logs = ActivityLog.objects.filter(user=request.user)

    total_steps = sum(log.steps for log in logs)
    total_calories = sum(log.calories_burned for log in logs)
    total_activities = logs.count()

    return Response({
        "total_activities": total_activities,
        "total_steps": total_steps,
        "total_calories": total_calories,
    })
    
# -------------------------
# USER PROFILE APIS
# -------------------------

@api_view(['GET', 'POST', 'PUT'])
@permission_classes([IsAuthenticated])
def user_profile_view(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = None

    if request.method == 'GET':
        if not profile:
            return Response({"message": "Profile not found"}, status=404)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

    if request.method == 'POST':
        if profile:
            return Response({"message": "Profile already exists"}, status=400)
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    if request.method == 'PUT':
        if not profile:
            return Response({"message": "Profile not found"}, status=404)
        serializer = UserProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)



