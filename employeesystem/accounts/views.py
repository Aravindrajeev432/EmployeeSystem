from django.db.models import Q

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import AccountSerializer, EditUserSerializer, ListMembersSerializer
from .permissions import EditUser
from .models import Members


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['first_name'] = user.first_name
        token['role'] = user.role.role

        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class TestView(APIView):
    def get(self, request):
        print("tesing")
        return Response(status=status.HTTP_200_OK)


class CreateUser(generics.CreateAPIView):
    queryset = Members.objects.all()
    serializer_class = AccountSerializer


class EditUser(generics.UpdateAPIView):
    permission_classes = [EditUser]
    serializer_class = EditUserSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role.role == 'Operator':
            return Members.objects.filter(role__role__contains='Technician')
        if user.role.role == 'Admin':
            # is_sfaff is superuser
            users = Members.objects.filter(
                ~Q(role__role__contains='Super Admin') & ~Q(is_staff=True))

            return users

        return Members.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['pk'] = self.kwargs['pk']
        return context


class DeleteUser(APIView):
    def delete(self, request, pk):
        try:

            user = Members.objects.get(pk=pk)
            # users with same role
            if request.user.role == user.role:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except Members.DoesNotExist:
            return Response(status=status.HTTP_403_FORBIDDEN)


class ListMembers(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListMembersSerializer

    def get_queryset(self):
        user_role = self.request.user.role.role
        if user_role == 'Admin':
            return Members.objects.filter(
                ~Q(role__role__contains='Super Admin') & ~Q(is_staff=True))
        elif user_role == 'Operators':
            return Members.objects.filter(role__role__contains='Technicans')
        elif user_role == 'Technicians':
            return Members.objects.filter(role__role__contains='Technicans')
        return Members.objects.all()


class Profile(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListMembersSerializer
    # queryset = Members.objects.all()

    def get_queryset(self):
        user_role = self.request.user.role.role
        if user_role == 'Super Admin':

            return Members.objects.all()
        elif user_role == 'Admin':
            return Members.objects.filter(
                ~Q(role__role__contains='Super Admin') & ~Q(is_staff=True))
        elif user_role == 'Operators':
            return Members.objects.filter(role__role__contains='Technicans')
        elif user_role == 'Technicians':
            return Members.objects.filter(role__role__contains='Technicans')
