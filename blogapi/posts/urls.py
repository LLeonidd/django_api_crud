from django.urls import path, include
from .views import PostList, PostDetail, UserViewSet
from rest_framework.routers import SimpleRouter


# Маршрутизация для ViewSets
router = SimpleRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
]

urlpatterns += router.urls
