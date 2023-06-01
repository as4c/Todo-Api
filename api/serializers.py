from rest_framework import serializers
from .models import Task, Tag
from datetime import datetime
from django.contrib.auth.models import User

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True,read_only=True)
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'due_date', 'tags','timestamp')

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
            
        task = Task(**validated_data)  # Create the Task object without saving it
        
        task.full_clean()  # Run the full validation on the Task object
        
        task.save()  # Save the Task object after validation
        
        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(**tag_data)
            task.tags.add(tag)
        
        return task


    # validating ‘Due Date’ field value cannot be before ‘Timestamp created’
    #field value
    def validate(self, data):
        due_date = data.get('due_date') 
        if due_date:
            timestamp = datetime.now().date()  # Get the current timestamp
        if due_date and timestamp:          
            if due_date < timestamp:
                raise serializers.ValidationError("Due date cannot be earlier than the timestamp.")
            
        return data
