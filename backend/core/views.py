# # # from django.shortcuts import render

# # # # Create your views here.
# # # from rest_framework import viewsets
# # # from .models import Zone, Division, Lobby, Room, Bed, FoodToken, Feedback
# # # from .serializers import ZoneSerializer, DivisionSerializer, LobbySerializer, RoomSerializer, BedSerializer, FoodTokenSerializer, FeedbackSerializer


# # # class ZoneViewSet(viewsets.ModelViewSet):
# # #     queryset = Zone.objects.all()
# # #     serializer_class = ZoneSerializer


# # # class DivisionViewSet(viewsets.ModelViewSet):
# # #     queryset = Division.objects.all()
# # #     serializer_class = DivisionSerializer


# # # class LobbyViewSet(viewsets.ModelViewSet):
# # #     queryset = Lobby.objects.all()
# # #     serializer_class = LobbySerializer


# # # class RoomViewSet(viewsets.ModelViewSet):
# # #     queryset = Room.objects.all()
# # #     serializer_class = RoomSerializer


# # # class BedViewSet(viewsets.ModelViewSet):
# # #     queryset = Bed.objects.all()
# # #     serializer_class = BedSerializer


# # # class FoodTokenViewSet(viewsets.ModelViewSet):
# # #     queryset = FoodToken.objects.all()
# # #     serializer_class = FoodTokenSerializer


# # # class FeedbackViewSet(viewsets.ModelViewSet):
# # #     queryset = Feedback.objects.all()
# # #     serializer_class = FeedbackSerializer

# # from rest_framework import viewsets, filters
# # from django_filters.rest_framework import DjangoFilterBackend
# # from .models import Zone, Division, Lobby, Room, Bed, FoodToken, Feedback
# # from .serializers import ZoneSerializer, DivisionSerializer, LobbySerializer, RoomSerializer, BedSerializer, FoodTokenSerializer, FeedbackSerializer


# # class ZoneViewSet(viewsets.ModelViewSet):
# #     queryset = Zone.objects.all()
# #     serializer_class = ZoneSerializer
# #     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
# #     filterset_fields = ['name', 'code']
# #     search_fields = ['name', 'code']


# # class DivisionViewSet(viewsets.ModelViewSet):
# #     queryset = Division.objects.all()
# #     serializer_class = DivisionSerializer
# #     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
# #     filterset_fields = ['zone__name', 'name', 'code']
# #     search_fields = ['name', 'code']


# # class LobbyViewSet(viewsets.ModelViewSet):
# #     queryset = Lobby.objects.all()
# #     serializer_class = LobbySerializer
# #     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
# #     filterset_fields = ['division__name', 'name', 'location']
# #     search_fields = ['name', 'location']


# # class RoomViewSet(viewsets.ModelViewSet):
# #     queryset = Room.objects.all()
# #     serializer_class = RoomSerializer
# #     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
# #     filterset_fields = ['lobby__name', 'room_number']
# #     search_fields = ['room_number']


# # class BedViewSet(viewsets.ModelViewSet):
# #     queryset = Bed.objects.all()
# #     serializer_class = BedSerializer
# #     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
# #     filterset_fields = ['room__room_number', 'status']
# #     search_fields = ['status']


# # class FoodTokenViewSet(viewsets.ModelViewSet):
# #     queryset = FoodToken.objects.all()
# #     serializer_class = FoodTokenSerializer
# #     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
# #     filterset_fields = ['crew_name', 'meal_type', 'status']
# #     search_fields = ['crew_name', 'meal_type']


# # class FeedbackViewSet(viewsets.ModelViewSet):
# #     queryset = Feedback.objects.all()
# #     serializer_class = FeedbackSerializer
# #     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
# #     filterset_fields = ['user_name', 'feedback_type', 'rating']
# #     search_fields = ['user_name', 'feedback_type', 'comment']

# # from rest_framework.permissions import BasePermission
# # from rest_framework.viewsets import ModelViewSet
# # from core.models import FoodToken
# # from core.serializers import FoodTokenSerializer

# # class IsCrewController(BasePermission):
# #     def has_permission(self, request, view):
# #         return request.user.groups.filter(name='Crew Controller').exists()

# # class FoodTokenViewSet(ModelViewSet):
# #     queryset = FoodToken.objects.all()
# #     serializer_class = FoodTokenSerializer

# #     def get_queryset(self):
# #         user = self.request.user
# #         if user.groups.filter(name='Crew Controller').exists():
# #             return FoodToken.objects.all()  # Crew Controller can see all tokens
# #         elif user.groups.filter(name='Crew Member').exists():
# #             return FoodToken.objects.filter(crew_name=user.username)  # Crew Members see their tokens only
# #         return FoodToken.objects.none()  # No access for others

# # class IsAdmin(BasePermission):
# #     def has_permission(self, request, view):
# #         return request.user.groups.filter(name='Admin').exists()

# # # class IsCrewController(BasePermission):
# # #     def has_permission(self, request, view):
# # #         return request.user.groups.filter(name='Crew Controller').exists()

# # # Example for a protected view
# # class LobbyViewSet(ModelViewSet):
# #     queryset = Lobby.objects.all()
# #     serializer_class = LobbySerializer
# #     permission_classes = [IsCrewController]

# from rest_framework import viewsets
# from .models import Zone, Division, Lobby, CustomUser
# from .serializers import ZoneSerializer, DivisionSerializer, LobbySerializer, CustomUserSerializer


# class ZoneViewSet(viewsets.ModelViewSet):
#     queryset = Zone.objects.all()
#     serializer_class = ZoneSerializer


# class DivisionViewSet(viewsets.ModelViewSet):
#     queryset = Division.objects.all()
#     serializer_class = DivisionSerializer


# class LobbyViewSet(viewsets.ModelViewSet):
#     queryset = Lobby.objects.all()
#     serializer_class = LobbySerializer


# class CustomUserViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer

### views.py ###
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Zone, Division, Lobby, Room, Bed
from .serializers import ZoneSerializer, DivisionSerializer, LobbySerializer, RoomSerializer, BedSerializer
from .models import CustomUser
from .serializers import CustomUserSerializer

class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'code']
    search_fields = ['name', 'code']

class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['zone__name', 'name', 'code']
    search_fields = ['name', 'code']

class LobbyViewSet(viewsets.ModelViewSet):
    queryset = Lobby.objects.all()
    serializer_class = LobbySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['division__name', 'name', 'location']
    search_fields = ['name', 'location']

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['lobby__name', 'room_number']
    search_fields = ['room_number']

class BedViewSet(viewsets.ModelViewSet):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['room__room_number', 'status']
    search_fields = ['status']

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer