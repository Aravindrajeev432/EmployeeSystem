from rest_framework.permissions import BasePermission
from right.models import Rights


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        try:
            print(request.user.is_admin)
            if request.user.is_admin:
                return True
        except AttributeError:
            return False
        return False


class IsSuperAdmin(BasePermission):
    """ For Super admin returns True """

    def has_permission(self, request, view):
        # checking for anonymous users
        try:
            print(request.user.role)
            # returns true or false
            if request.user.role == "SUPER_ADMIN":
                return True
        except AttributeError:
            return False

        return False


class CreateUser(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        try:
            r = request.user.role.rights.get(right='Create User')
            if r:
                return True
        except Rights.DoesNotExist:

            return False
        return True


class EditUser(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        try:
            r = request.user.role.rights.get(right='Edit User')
            if r:
                return True
        except Rights.DoesNotExist:

            return False
        return True


class DeleteUser(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        try:
            r = request.user.role.rights.get(right='Delete User')
            if r:
                return True
        except Rights.DoesNotExist:

            return False
        return True
