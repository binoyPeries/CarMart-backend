from rest_framework import serializers
from .models import Customer


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

        if len(str(contact_no)) < 10:
            raise serializers.ValidationError('The contact number is invalid')

        return attrs

    def create(self, validated_data):
        return Customer.objects.create_user(**validated_data)
