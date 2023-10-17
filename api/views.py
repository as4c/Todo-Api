from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task, Tag
from .serializers import TaskSerializer, TagSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.authentication import  BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.urls import URLPattern
from django.shortcuts import render
from django.http import JsonResponse
from django.urls import path
from users import views
from django.views.decorators.csrf import csrf_exempt
import os
from .tasks import add, thumbnail_task
import uuid
from PIL import Image
@api_view(http_method_names=["POST"])
def add_numbers(request):
    num1 = request.data['num1']
    num2 = request.data['num2']
    add.delay(num1, num2)
    return JsonResponse({
        "message":"Successfully submitted"
    }, status=200)

@api_view(http_method_names=["POST"])
def create_thumbnail(request):
    file = request.FILES.get('file')
    file_id = str(uuid.uuid4)
    image = Image.open(file)
    image.save("todo/Images/" + file_id + ".jpg")
    thumbnail_task.delay(file)
    return JsonResponse({
        "message":"Processing the Image."
    }, status=200)



# homepage to show all the available endpoints 
def homepage(request):
    env = os.environ.get("ENV", "None")
    urlpatterns = [      
        path('api/create-todo/', TaskCreateAPIView.as_view(), name='create-todo'),
        path('api/todos/', TaskAPIView.as_view(), name='todo-list'),
        path('api/todo/<int:pk>/', TaskDetailAPIView.as_view(), name='todos'),
        path('api/create-tag/', TagCreateAPIView.as_view(), name="create-tag"),
        path("api/tags/", TagAPIView.as_view(), name='tags'),
        path('api/tags/<int:pk>/', TagDetailAPIView.as_view(), name='detail-tags'),
        path('users/signup/', csrf_exempt(views.SignupAPIView.as_view()), name='signup'),
        path('users/login/', csrf_exempt(views.LoginAPIView.as_view()), name='login'),
        path('users/logout/', csrf_exempt(views.LogoutAPIView.as_view()), name='logout')
    ]

    api_endpoints = {}
    for urlpattern in urlpatterns:
        if isinstance(urlpattern, URLPattern):
            api_endpoints[urlpattern.name] = str(urlpattern.pattern)

    return JsonResponse({
        "message": "Hello I'm sagar!. Environment: " + env,
        # "data": api_endpoints
    }, status=200)
# All the method to perform CRUD Operation on the App
class TaskAPIView(APIView):
    authentication_classes = [BasicAuthentication]  # Add BasicAuthentication
    permission_classes = [IsAuthenticated]  # Optional permission class
    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

class TaskCreateAPIView(APIView):
    authentication_classes = [BasicAuthentication]  # Add BasicAuthentication
    permission_classes = [IsAuthenticated]  # Optional permission class

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response({"message": "Todo created"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailAPIView(APIView):
    authentication_classes = [BasicAuthentication]  # Add BasicAuthentication
    permission_classes = [IsAuthenticated]  # Optional permission class

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Todo updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response({"message": "Todo deleted"}, status=status.HTTP_204_NO_CONTENT)

class TagAPIView(APIView):
    authentication_classes = [BasicAuthentication]  # Add BasicAuthentication
    permission_classes = [IsAuthenticated]  # Optional permission class
    def get(self, request, format=None):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

  
class TagCreateAPIView(APIView):
    authentication_classes = [BasicAuthentication]  # Add BasicAuthentication
    permission_classes = [IsAuthenticated]  # Optional permission class
    authentication_classes = [BasicAuthentication]  # Add BasicAuthentication
    permission_classes = [IsAuthenticated]  # Optional permission class

    def post(self, request, format=None):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Tag created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TagDetailAPIView(APIView):
    authentication_classes = [BasicAuthentication]  # Add BasicAuthentication
    permission_classes = [IsAuthenticated]  # Optional permission class

    def get_object(self, pk):
        try:
            return Tag.objects.get(pk=pk)
        except Tag.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk, format=None):
        tag = self.get_object(pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        tag = self.get_object(pk)
        serializer = TagSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Tag updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tag = self.get_object(pk)
        tag.delete()
        return Response({"message": "Tag deleted"}, status=status.HTTP_204_NO_CONTENT)





