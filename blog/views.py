from blog.serializers import BlogSerialize
from blog.models import Blog
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class BlogList(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerialize(blogs, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(args):
        pass
    
