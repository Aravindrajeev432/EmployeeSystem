from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import Roles
from role.serializers import RoleSerializer, RoleViewSerializer
from .custom_permissions import DeleteRolePermission, EditRolePermission,\
    CreatRolePermission

class CreateRole(generics.CreateAPIView):
    permission_classes = [CreatRolePermission]
    queryset = Roles.objects.all()
    serializer_class = RoleSerializer
    
class ListRoles(generics.ListAPIView):
    queryset = Roles.objects.all()
    serializer_class = RoleViewSerializer

class EditRole(generics.UpdateAPIView):
    permission_classes = [EditRolePermission]
    queryset = Roles.objects.all()
    serializer_class = RoleSerializer
    lookup_field = 'pk'



class DeleteRole(APIView):
    permission_classes = [DeleteRolePermission]
    def delete(self, request, pk):
        try:
            roles = Roles.objects.get(pk=pk)
            if request.user.role.role=='Admin':
                if roles.role == 'Super Admin':
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
                roles.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Roles.DoesNotExist:
            return Response(status=status.HTTP_403_FORBIDDEN) 
        
