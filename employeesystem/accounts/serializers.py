from rest_framework import serializers
import re
from .models import Members
from role.models import Roles
from role.serializers import RoleSerializer, RoleViewSerializer


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Members
        fields = ['email', 'first_name', 'last_name', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):

        email = attrs['email']
        email_pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]{2,5}\\.[a-z]{2,3}$"
        email_verify = re.match(email_pattern, email)

        if email_verify is None:
            raise serializers.ValidationError(
                {"email": "Enter valid email"})

        first_name = attrs['first_name']
        if not first_name:
            raise serializers.ValidationError('First name must be provided')

        last_name = attrs['last_name']
        if not last_name:
            raise serializers.ValidationError('Last name must be provided')

        password = attrs['password']
        password_pattern = re.compile(r'^(?=.*[A-Z])(?=.*[0-9]).{8,15}$')
        password_verify = password_pattern.search(password)
        print(password_verify)
        if password_verify is None:
            raise serializers.ValidationError({
                "Password": "Password should contain minimum 8 characters including numbers and Capital letters"
            })

        return attrs

    def save(self):
        register = Members.objects.create_user(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            password=self.validated_data['password'],
            role=self.validated_data['role']
        )

        return register


class EditUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ['email', 'first_name', 'last_name', 'role']

    def validate(self, attrs):
        print(self.context)
        try:
            email = attrs['email']
            email_pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]{2,5}\\.[a-z]{2,3}$"
            email_verify = re.match(email_pattern, email)
            if email_verify is None:
                raise serializers.ValidationError(
                    {"email": "Enter valid email"})
        except KeyError:
            pass

        try:
            first_name = attrs['first_name']
            if not first_name:
                raise serializers.ValidationError(
                    'First name must be provided')
        except KeyError:
            pass
        try:
            last_name = attrs['last_name']
            if not last_name:
                raise serializers.ValidationError('Last name must be provided')
        except KeyError:
            pass
        try:
            print(self.context['request'].user.role)
            if self.context['request'].user.id == self.context['pk']:
                role = attrs['role']
                if role != self.context['request'].user.role:
                    raise serializers.ValidationError(
                        'You cannot Edit Your Role')

        except KeyError:
            pass

        return attrs


class ListMembersSerializer(serializers.ModelSerializer):
    role = RoleViewSerializer()

    class Meta:
        model = Members
        fields = ['first_name', 'last_name', 'email', 'role']
