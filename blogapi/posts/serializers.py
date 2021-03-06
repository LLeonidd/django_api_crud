from rest_framework.serializers import ModelSerializer
from .models import Post
from django.contrib.auth import get_user_model


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'

