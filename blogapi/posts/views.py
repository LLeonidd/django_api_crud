from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PostSerializer, UserSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly

from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model


class UserViewSet(ModelViewSet):
    """
    Реализует Api для CRUD модели юзера
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


# Все это возможно реализовать с помощью класса ModelViewSet
class PostList(ListAPIView):
    """
    Реализует api для отображение пользователя
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    """
    Реализует API для обновления, удаления пользователя
    """
    permission_classes = (IsAuthorOrReadOnly, ) # Custom permissions
    queryset = Post.objects.all()
    serializer_class = PostSerializer
