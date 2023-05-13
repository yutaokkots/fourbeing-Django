from rest_framework import serializers
from fourbeing.models import Test, Post, Reply

# serializer for create_user request
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, get_user_model

from rest_framework.validators import UniqueValidator

from rest_framework.response import Response
# from knox.auth import AuthToken


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title', 'description', 'created', 'profile', "username"]
        # extra_kwargs = {
        #     'title': {'required': True},
        #     'description': {'required': True},
        # }


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('name', 'description')


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(queryset=get_user_model().objects.all())
        ]
    )
    #user object serializer
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password')
        extra_kwargs = {'password': {'write_only': True, 'min_length':4}}


    
class AuthSerializer(serializers.Serializer):
    #user authentication object serializer
    username = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": 'password'},
        trim_whitespace=False
    )
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user =  authenticate(
            request = self.context.get('request'),
            username=username,
            password=password
        )
        if not user:
            message = ('Unable to authenticate user')
            raise serializers.ValidationError(message, code='authentication')
        
        attrs['user'] = user
        return 

class ReplySerializer(serializers.Serializer):
    class Meta:
        model = Reply
        fields = ['comment', 'love', 'profile', 'post']
