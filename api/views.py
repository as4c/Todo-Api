from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task, Tag
from .serializers import TaskSerializer, TagSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.authentication import  BasicAuthentication
from rest_framework.permissions import IsAuthenticated


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





