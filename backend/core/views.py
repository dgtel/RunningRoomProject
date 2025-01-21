# from django.shortcuts import render

# # Create your views here.
# from rest_framework import viewsets
# from .models import Zone, Division, Lobby, Room, Bed, FoodToken, Feedback
# from .serializers import ZoneSerializer, DivisionSerializer, LobbySerializer, RoomSerializer, BedSerializer, FoodTokenSerializer, FeedbackSerializer


# class ZoneViewSet(viewsets.ModelViewSet):
#     queryset = Zone.objects.all()
#     serializer_class = ZoneSerializer


# class DivisionViewSet(viewsets.ModelViewSet):
#     queryset = Division.objects.all()
#     serializer_class = DivisionSerializer


# class LobbyViewSet(viewsets.ModelViewSet):
#     queryset = Lobby.objects.all()
#     serializer_class = LobbySerializer


# class RoomViewSet(viewsets.ModelViewSet):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer


# class BedViewSet(viewsets.ModelViewSet):
#     queryset = Bed.objects.all()
#     serializer_class = BedSerializer


# class FoodTokenViewSet(viewsets.ModelViewSet):
#     queryset = FoodToken.objects.all()
#     serializer_class = FoodTokenSerializer


# class FeedbackViewSet(viewsets.ModelViewSet):
#     queryset = Feedback.objects.all()
#     serializer_class = FeedbackSerializer

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Zone, Division, Lobby, Room, Bed, FoodToken, Feedback
from .serializers import ZoneSerializer, DivisionSerializer, LobbySerializer, RoomSerializer, BedSerializer, FoodTokenSerializer, FeedbackSerializer


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


class FoodTokenViewSet(viewsets.ModelViewSet):
    queryset = FoodToken.objects.all()
    serializer_class = FoodTokenSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['crew_name', 'meal_type', 'status']
    search_fields = ['crew_name', 'meal_type']


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['user_name', 'feedback_type', 'rating']
    search_fields = ['user_name', 'feedback_type', 'comment']
