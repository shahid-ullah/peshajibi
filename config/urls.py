"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from apps.users.apis import (
    FavouriteUserAddRemove,
    FavouriteUserListAPI,
    ProfileUpdateAPI,
    RegistrationAPI,
    UserDetailAPI,
    UserListAPI,
)

# from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('v1/api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('users/', UserListAPI.as_view(), name='user_list'),
    path('user/<int:pk>/', UserDetailAPI.as_view(), name='user_detail'),
    path('registration/', RegistrationAPI.as_view(), name='registration'),
    path('update_profile/', ProfileUpdateAPI.as_view(), name='update_profile'),
    path('favourite_users/', FavouriteUserListAPI.as_view(), name='favourite_users'),
    path('favourite_user/', FavouriteUserAddRemove.as_view(), name='favourite_user'),
    path('', include('apps.peshajibi.urls')),
]


if settings.DEBUG:
    optional_urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
    urlpatterns += optional_urlpatterns
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Peshajibi admin"
admin.site.site_title = "Peshajibi admin"
admin.site.index_title = "Welcome to Peshajibi Admin Panel"

handler404 = 'apps.core.views.error_404'
handler500 = 'apps.core.views.error_500'
