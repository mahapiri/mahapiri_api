from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Todo
from .serializer import TodoSerializer

# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('-create_at')
    serializer_class = TodoSerializer
    permission_classes = [] #permissions.IsAuthenticated