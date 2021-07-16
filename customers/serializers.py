from rest_framework import serializers
from .models import Customer
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = Customer
        fields = ['email', 'password', 'first_name', 'last_name', 'contact_no', 'city']

    def validate(self, attrs):
        first_name = attrs.get('first_name', '')
        last_name = attrs.get('last_name', '')
        contact_no = attrs.get('contact_no', '')

        if not first_name.isalnum():
            raise serializers.ValidationError('The first name can only contain alphanumerics')

        if not last_name.isalnum():
            raise serializers.ValidationError('The last name can only contain alphanumerics')

        if len(contact_no) < 10:
            raise serializers.ValidationError('The contact number is invalid')

        return attrs

    def create(self, validated_data):
        return Customer.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=225, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    first_name = serializers.CharField(max_length=225, read_only=True)
    last_name = serializers.CharField(max_length=225, read_only=True)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = Customer.objects.get(email=obj['email'])

        return {
            'access': user.tokens()['access'],
            'refresh': user.tokens()['refresh']
        }

    class Meta:
        model = Customer
        fields = ['email', 'password', 'first_name', 'last_name', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials')

        return {
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'tokens': user.tokens

        }
