from rest_framework.permissions import BasePermission
from .models import Rights

class IsAdminCustomPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.role.role == 'Super Admin':
            return True
        elif request.user.role.role == 'Admin':
            return True
        elif request.user.is_staff:
            return True
        else:
            return False
        
class CreateRightPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        try:
            r = request.user.role.rights.get(right='Create Right')
            if r:
                return True
        except Rights.DoesNotExist:
            return False
        return True

class EditRightPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        try:
            r = request.user.role.rights.get(right='Edit Right')
            if r:
                return True
        except Rights.DoesNotExist:
            return False
        return True
    
class DeleteRightPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        try:
            r = request.user.role.rights.get(right='Delete Right')
            if r:
                
                return True
        except Rights.DoesNotExist:
            return False
        return True
