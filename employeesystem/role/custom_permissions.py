from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission

from right.models import Rights

class CreateOrDeleteRolePermission(BasePermission):
    def has_permission(self,request, view):
        try:
            
            if request.user.role.role == 'Super Admin' :
                return True
            elif request.user.role == 'Admin':
                return True
            elif request.user.is_staff:
                return True
        except AttributeError:
            
            return False  
        
        return False
    
class CreatRolePermission(BasePermission):
    def has_permission(self,request, view):
        if not request.user.is_authenticated:
            return False
        
        try:
            r = request.user.role.rights.get(right='Create Role')
            if r:
                return True
        except Rights.DoesNotExist:
            
            return False
       
        return True

class DeleteRolePermission(BasePermission):
    def has_permission(self,request, view):
        if not request.user.is_authenticated:
            return False
        
        try:
            r = request.user.role.rights.get(right='Delete Role')
            if r:
                return True
        except Rights.DoesNotExist:
            
            return False
       
        return True


class EditRolePermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        try:
            r = request.user.role.rights.get(right='Edit Role')
            if r:
                return True
        except Rights.DoesNotExist:
            
            return False
        return True