
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

from rest_framework.permissions import IsAdminUser

from .models import Rights

from .serializers import RightSerializer
from .custom_permissions import CreateRightPermission,EditRightPermission,\
    DeleteRightPermission


class CreateRight(generics.ListCreateAPIView):
    permission_classes = [CreateRightPermission]
    queryset = Rights.objects.all()
    serializer_class = RightSerializer

class EditRight(generics.UpdateAPIView):
    permission_classes = [EditRightPermission]
    queryset = Rights.objects.all()
    serializer_class = RightSerializer
    lookup_field = 'pk'

class DeleteRight(generics.DestroyAPIView):
    permission_classes = [DeleteRightPermission]
    queryset = Rights.objects.all()
    serializer_class = RightSerializer
    lookup_field = 'pk'
