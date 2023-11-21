from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from .serializer import BlogSerializer
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

@api_view(['GET'])
def getBlogs(request):
    blogs = blog.objects.filter(goLive='yes')
    serializer = BlogSerializer(blogs, many=True)
    return response(serializer.data)

def getBlog(request):
    blog = blog.object.get(_id=pk)
    serializer = BlogSerializer(blog, many=False)
    return response(serializer.data)
