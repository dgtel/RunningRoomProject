"""
URL configuration for backendapp project.

The `urlpatterns` list routes URLs to views. For more information, see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/

Examples:
Function views:
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')

Class-based views:
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

Including another URLconf:
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import (
    ZoneViewSet,
    DivisionViewSet,
    LobbyViewSet,
    CustomUserViewSet,
    FoodTokenViewSet,
    FeedbackViewSet,
    RoomViewSet,
    BedViewSet,
    LoginAPIView,
    ProfileAPIView,
    RegisterAPIView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Registering viewsets with the DefaultRouter for API endpoints
router = DefaultRouter()
router.register('zones', ZoneViewSet, basename='zones')
router.register('divisions', DivisionViewSet, basename='divisions')
router.register('lobbies', LobbyViewSet, basename='lobbies')
router.register('users', CustomUserViewSet, basename='users')
router.register('food-tokens', FoodTokenViewSet, basename='food-tokens')
router.register('feedbacks', FeedbackViewSet, basename='feedbacks')
router.register('rooms', RoomViewSet, basename='rooms')
router.register('beds', BedViewSet, basename='beds')

# URL patterns
urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),
    
    # API endpoints managed by the router
    path('api/', include(router.urls)),
    
    # JWT authentication endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Browsable API authentication login/logout
    path('api-auth/', include('rest_framework.urls')),

    path("api/login/", LoginAPIView.as_view(), name="custom_login"),
    path("api/profile/", ProfileAPIView.as_view(), name="profile"),

    path("api/register/", RegisterAPIView.as_view(), name="register"),
]


# urlpatterns += [
#     path("api/login/", LoginAPIView.as_view(), name="custom_login"),
# ]
