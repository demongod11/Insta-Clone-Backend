from django.contrib.auth import get_user_model
from Users.models import User
from rest_framework import serializers
from rest_framework.settings import api_settings


class RegisterUserSerializer(serializers.ModelSerializer):
    """Serializer for creating a new user account"""

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'fullname', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True,
                                     'min_length': 5},
                        'username': {'min_length': 3}}

    def create(self):
        """Create a new user with encrypted password and return it"""
        if not self.validated_data['email']:
            raise serializers.ValidationError('Users must have an email address')
        if not self.validated_data['username']:
            raise serializers.ValidationError('Users must have a username')
        if not self.validated_data['fullname']:
            raise serializers.ValidationError('Users must have a fullname')
        user = User(
                    email=self.validated_data['email'],
                    username=self.validated_data['username'],
                    fullname = self.validated_data['fullname']
                )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user


# class UserInfoSerializer(serializers.ModelSerializer):
#     """Serializer for the user settings objects"""

#     class Meta:
#         model = get_user_model()
#         fields = ('id', 'email', 'username', 'password',
#                   'fullname', 'bio', 'profile_pic')
#         extra_kwargs = {'password': {'write_only': True,
#                                      'min_length': 5},
#                         'username': {'min_length': 3}}

#     def update(self, instance, validated_data):
#         """Update a user, setting the password correctly and return it"""
#         password = validated_data.pop('password', None)
#         user = super().update(instance, validated_data)

#         if password:
#             user.set_password(password)
#             user.save()

#         return user


class UserInfoSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ['id', 'email', 'username', 'fullname', 'bio', 'profile_pic']


class ChangePasswordSerializer(serializers.Serializer):

	old_password 				= serializers.CharField(required=True)
	new_password 				= serializers.CharField(required=True)
	confirm_new_password 		= serializers.CharField(required=True)
