from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'name', 'birthday', 'gender', 'bio']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            name=validated_data['name'],
            birthday=validated_data['birthday'],
            gender=validated_data['gender'],
            bio=validated_data['bio']
        )
        user.set_password(validated_data['password'])  # 비밀번호 암호화
        user.save()
        return user
