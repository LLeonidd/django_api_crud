from django.contrib import admin
from django.urls import path, include
#from rest_framework.schemas import get_schema_view

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
import dj_rest_auth.views

schema_view = get_schema_view(
    openapi.Info(
        title='BlogApi',
        default_version='3.0.1',
        description='Blog OpenApi description',
        terms_of_service='http://google.ocm/polices/terms/',
        contact=openapi.Contact(email='admin@email.ru'),
        license=openapi.License(name='BSD License')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls')),  # Подключаются формф для логина
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')), # полключения форм для логина, логаута, резета пароля, задания пароля
    path('api/v1/dj-rest-auth/registration/',
         include('dj_rest_auth.registration.urls')), # для формы регистрации пользователя

    # swagger_documentation
    path('swagger', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'
         ),

    #Redoc documentation
    path('redoc', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc'
         )
    # Создание OpenAPI схема
    #pip install pyyml uritemplate

    # path('openapi', get_schema_view(
    #     title="Blog Api",
    #     description="Any training blog",
    #     version="1.0.0"
    # ), name='openapi-schema'),

    # Создание документации для схемы OpenApi
    # pip install drf-yasg






]
