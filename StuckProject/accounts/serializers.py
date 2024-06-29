from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate


from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True,
        validators=[UniqueValidator(queryset=User.objects.all())], # 이메일 중복검사
    )
    password = serializers.CharField(
        write_only=True,
        required = True,
        # validators=[validate_password], 배포 전 주석 풀기
    )
    password2 = serializers.CharField(
        write_only=True,
        required = True,
    )

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password2": "비밀번호가 일치하지 않습니다."}
            )
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user = user)

        return user
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user:
            Token.objects.filter(user=user).delete()
            token, created = Token.objects.get_or_create(user=user)
            return {'token': token}
        raise serializers.ValidationError(
            {"error": "ID나 비밀번호를 확인해주세요"}
        )
    