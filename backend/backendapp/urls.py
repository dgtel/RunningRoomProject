"""
URL configuration for backendapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import ZoneViewSet, DivisionViewSet, LobbyViewSet, RoomViewSet, BedViewSet, FoodTokenViewSet, FeedbackViewSet


router = DefaultRouter()
router.register('zones', ZoneViewSet)
router.register('divisions', DivisionViewSet)
router.register('lobbies', LobbyViewSet)
router.register('rooms', RoomViewSet)
router.register('beds', BedViewSet)
router.register('food-tokens', FoodTokenViewSet)
router.register('feedbacks', FeedbackViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

