from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=['id','content','publication_date','author','post']
        