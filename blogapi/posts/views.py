from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PostSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly


class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly, ) # Custom permissions
    queryset = Post.objects.all()
    serializer_class = PostSerializer
