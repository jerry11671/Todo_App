from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        # extra_kwargs = {
        #     'write_only': True,
        # }

    def validate(self, validated_data):
        password = validated_data['password']
        password2 = validated_data['password2']

        if password != password2:
            raise serializers.ValidationError("Passwords do not match!!")
        
        if User.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError("This email is already in use!")
        
        if len(password) <= 6:
            raise serializers.ValidationError("Password is too short!")
        
        return validated_data
        
    def save(self):
        username = self.validated_data['username']
        email = self.validated_data['email']
        password = self.validated_data['password']

        account = User.objects.create(username=username, email=email)
        account.set_password(password)
        account.save()

        return account


