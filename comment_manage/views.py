from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404

# Create your views here.
class CommentListCreateView(APIView):
    permission_classes=[IsAuthenticatedOrReadOnly]

    def get(self,request,post_id):
        comments=comments.objects.filter(post_id=post_id)
        serializer=CommentSerializer(comments,many=True)
        return Response(serializer.data)
    
    def post(self,request,post_id):
        serializer=CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user,post_id=post_id)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class CommentRetrieveUpdateDeleteView(APIView):
    permission_classes=[IsAuthenticatedOrReadOnly]

    def get(self,request,post_id,comment_id):
        comment=get_object_or_404(Comment,id=comment_id,post_id=post_id)
        serializer=CommentSerializer(comment)
        return Response(serializer.data)
    def put(self,request,post_id,comment_id):
        comment=get_object_or_404(Comment,id=comment_id,post_id=post_id)
        serializer=CommentSerializer(comment,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,post_id,comment_id):
        comment=get_object_or_404(Comment,id=comment_id,post_id=post_id)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
