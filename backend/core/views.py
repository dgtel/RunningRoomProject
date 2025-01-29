# # # # from django.shortcuts import render

# # # # # Create your views here.
# # # # from rest_framework import viewsets
# # # # from .models import Zone, Division, Lobby, Room, Bed, FoodToken, Feedback
# # # # from .serializers import ZoneSerializer, DivisionSerializer, LobbySerializer, RoomSerializer, BedSerializer, FoodTokenSerializer, FeedbackSerializer


# # # # class ZoneViewSet(viewsets.ModelViewSet):
# # # #     queryset = Zone.objects.all()
# # # #     serializer_class = ZoneSerializer


# # # # class DivisionViewSet(viewsets.ModelViewSet):
# # # #     queryset = Division.objects.all()
# # # #     serializer_class = DivisionSerializer


# # # # class LobbyViewSet(viewsets.ModelViewSet):
# # # #     queryset = Lobby.objects.all()
# # # #     serializer_class = LobbySerializer


# # # # class RoomViewSet(viewsets.ModelViewSet):
# # # #     queryset = Room.objects.all()
# # # #     serializer_class = RoomSerializer


# # # # class BedViewSet(viewsets.ModelViewSet):
# # # #     queryset = Bed.objects.all()
# # # #     serializer_class = BedSerializer


# # # # class FoodTokenViewSet(viewsets.ModelViewSet):
# # # #     queryset = FoodToken.objects.all()
# # # #     serializer_class = FoodTokenSerializer


# # # # class FeedbackViewSet(viewsets.ModelViewSet):
# # # #     queryset = Feedback.objects.all()
# # # #     serializer_class = FeedbackSerializer

# # # from rest_framework import viewsets, filters
# # # from django_filters.rest_framework import DjangoFilterBackend
# # # from .models import Zone, Division, Lobby, Room, Bed, FoodToken, Feedback
# # # from .serializers import ZoneSerializer, DivisionSerializer, LobbySerializer, RoomSerializer, BedSerializer, FoodTokenSerializer, FeedbackSerializer


# # # class ZoneViewSet(viewsets.ModelViewSet):
# # #     queryset = Zone.objects.all()
# # #     serializer_class = ZoneSerializer
# # #     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
# # #     filterset_fields = ['name', 'code']
# # #     search_fields = ['name', 'code']


# # # class DivisionViewSet(viewsets.ModelViewSet):
# # #     queryset = Division.objects.all()
# # #     serializer_class = DivisionSerializer
# # #     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
# # #     filterset_fields = ['zone__name', 'name', 'code']
# # #     search_fields = ['name', 'code']


# # # class LobbyViewSet(viewsets.ModelViewSet):
# # #     queryset = Lobby.objects.all()
# # #     serializer_class = LobbySerializer
# # #     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
# # #     filterset_fields = ['division__name', 'name', 'location']
# # #     search_fields = ['name', 'location']


# # # class RoomViewSet(viewsets.ModelViewSet):
# # #     queryset = Room.objects.all()
# # #     serializer_class = RoomSerializer
# # #     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
# # #     filterset_fields = ['lobby__name', 'room_number']
# # #     search_fields = ['room_number']


# # # class BedViewSet(viewsets.ModelViewSet):
# # #     queryset = Bed.objects.all()
# # #     serializer_class = BedSerializer
# # #     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
# # #     filterset_fields = ['room__room_number', 'status']
# # #     search_fields = ['status']


# # # class FoodTokenViewSet(viewsets.ModelViewSet):
# # #     queryset = FoodToken.objects.all()
# # #     serializer_class = FoodTokenSerializer
# # #     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
# # #     filterset_fields = ['crew_name', 'meal_type', 'status']
# # #     search_fields = ['crew_name', 'meal_type']


# # # class FeedbackViewSet(viewsets.ModelViewSet):
# # #     queryset = Feedback.objects.all()
# # #     serializer_class = FeedbackSerializer
# # #     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
# # #     filterset_fields = ['user_name', 'feedback_type', 'rating']
# # #     search_fields = ['user_name', 'feedback_type', 'comment']

# # # from rest_framework.permissions import BasePermission
# # # from rest_framework.viewsets import ModelViewSet
# # # from core.models import FoodToken
# # # from core.serializers import FoodTokenSerializer

# # # class IsCrewController(BasePermission):
# # #     def has_permission(self, request, view):
# # #         return request.user.groups.filter(name='Crew Controller').exists()

# # # class FoodTokenViewSet(ModelViewSet):
# # #     queryset = FoodToken.objects.all()
# # #     serializer_class = FoodTokenSerializer

# # #     def get_queryset(self):
# # #         user = self.request.user
# # #         if user.groups.filter(name='Crew Controller').exists():
# # #             return FoodToken.objects.all()  # Crew Controller can see all tokens
# # #         elif user.groups.filter(name='Crew Member').exists():
# # #             return FoodToken.objects.filter(crew_name=user.username)  # Crew Members see their tokens only
# # #         return FoodToken.objects.none()  # No access for others

# # # class IsAdmin(BasePermission):
# # #     def has_permission(self, request, view):
# # #         return request.user.groups.filter(name='Admin').exists()

# # # # class IsCrewController(BasePermission):
# # # #     def has_permission(self, request, view):
# # # #         return request.user.groups.filter(name='Crew Controller').exists()

# # # # Example for a protected view
# # # class LobbyViewSet(ModelViewSet):
# # #     queryset = Lobby.objects.all()
# # #     serializer_class = LobbySerializer
# # #     permission_classes = [IsCrewController]

# # from rest_framework import viewsets
# # from .models import Zone, Division, Lobby, CustomUser
# # from .serializers import ZoneSerializer, DivisionSerializer, LobbySerializer, CustomUserSerializer


# # class ZoneViewSet(viewsets.ModelViewSet):
# #     queryset = Zone.objects.all()
# #     serializer_class = ZoneSerializer


# # class DivisionViewSet(viewsets.ModelViewSet):
# #     queryset = Division.objects.all()
# #     serializer_class = DivisionSerializer


# # class LobbyViewSet(viewsets.ModelViewSet):
# #     queryset = Lobby.objects.all()
# #     serializer_class = LobbySerializer


# # class CustomUserViewSet(viewsets.ModelViewSet):
# #     queryset = CustomUser.objects.all()
# #     serializer_class = CustomUserSerializer

# ### views.py ###
# from rest_framework import viewsets, filters
# from django_filters.rest_framework import DjangoFilterBackend
# from .models import Zone, Division, Lobby, Room, Bed, FoodToken, Feedback
# from .serializers import ZoneSerializer, DivisionSerializer, LobbySerializer, RoomSerializer, BedSerializer, FoodTokenSerializer, FeedbackSerializer
# from .models import CustomUser
# from .serializers import CustomUserSerializer

# class ZoneViewSet(viewsets.ModelViewSet):
#     queryset = Zone.objects.all()
#     serializer_class = ZoneSerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_fields = ['name', 'code']
#     search_fields = ['name', 'code']

# class DivisionViewSet(viewsets.ModelViewSet):
#     queryset = Division.objects.all()
#     serializer_class = DivisionSerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_fields = ['zone__name', 'name', 'code']
#     search_fields = ['name', 'code']

# class LobbyViewSet(viewsets.ModelViewSet):
#     queryset = Lobby.objects.all()
#     serializer_class = LobbySerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_fields = ['division__name', 'name', 'location']
#     search_fields = ['name', 'location']

# class RoomViewSet(viewsets.ModelViewSet):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_fields = ['lobby__name', 'room_number']
#     search_fields = ['room_number']

# class BedViewSet(viewsets.ModelViewSet):
#     queryset = Bed.objects.all()
#     serializer_class = BedSerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_fields = ['room__room_number', 'status']
#     search_fields = ['status']

# class CustomUserViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer

# class FoodTokenViewSet(viewsets.ModelViewSet):
#     queryset = FoodToken.objects.all()
#     serializer_class = FoodTokenSerializer

#     def get_queryset(self):
#         user = self.request.user
#         if user.groups.filter(name='Crew Controller').exists():
#             return FoodToken.objects.all()  # Crew Controller can see all tokens
#         elif user.groups.filter(name='Crew Member').exists():
#             return FoodToken.objects.filter(crew_name=user.username)  # Crew Members see their tokens only
#         return FoodToken.objects.none()  # No access for others
    
# class FeedbackViewSet(viewsets.ModelViewSet):
#     queryset = Feedback.objects.all()
#     serializer_class = FeedbackSerializer

### views.py ###
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Zone, Division, Lobby, Room, Bed, FoodToken, Feedback, CustomUser
from .serializers import (
    ZoneSerializer, DivisionSerializer, LobbySerializer, RoomSerializer,
    BedSerializer, FoodTokenSerializer, FeedbackSerializer, CustomUserSerializer
)

class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'code']
    search_fields = ['name', 'code']
    permission_classes = []

class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['zone__name', 'name', 'code']
    search_fields = ['name', 'code']
    permission_classes = []

class LobbyViewSet(viewsets.ModelViewSet):
    queryset = Lobby.objects.all()
    serializer_class = LobbySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['division__name', 'name', 'location']
    search_fields = ['name', 'location']
    permission_classes = []

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['lobby__name', 'room_number']
    search_fields = ['room_number']
    permission_classes = []

class BedViewSet(viewsets.ModelViewSet):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['room__room_number', 'status']
    search_fields = ['status']
    permission_classes = []

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class FoodTokenViewSet(viewsets.ModelViewSet):
    queryset = FoodToken.objects.all()
    serializer_class = FoodTokenSerializer

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Crew Controller').exists():
            return FoodToken.objects.all()  # Crew Controller can see all tokens
        elif user.groups.filter(name='Crew Member').exists():
            return FoodToken.objects.filter(crew_name=user.username)  # Crew Members see their tokens only
        return FoodToken.objects.none()  # No access for others

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
#---
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate

class LoginAPIView(APIView):
    permission_classes = []  # Allow access without authentication

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "success": True,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                # "role": user.groups.first().name if user.groups.exists() else "user",
                "role": user.groups.first().name if user.groups.exists() else "No role assigned",
                "username": user.username,
                "email": user.email,
            })
        return Response({"success": False, "error": "Invalid credentials"}, status=401)

from rest_framework.permissions import IsAuthenticated

class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email,
            "role": user.groups.first().name if user.groups.exists() else "user",
            "lobby": user.LobbyAssigned.name if user.LobbyAssigned else "No lobby assigned",
        })
    
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from core.models import CustomUser, Lobby
from rest_framework.permissions import AllowAny

# class RegisterAPIView(APIView):
#     permission_classes = [AllowAny]  # Allow public access for registration

#     def post(self, request):
#         username = request.data.get("username")
#         email = request.data.get("email")
#         password = request.data.get("password")
#         role = request.data.get("role", "crew")  # Default to crew if no role is provided
#         lobby_id = request.data.get("lobby_id")  # New: Lobby Assignment

#         # Check if username or email is already taken
#         if CustomUser.objects.filter(username=username).exists():
#             return Response({"success": False, "error": "Username already taken."}, status=400)

#         if CustomUser.objects.filter(email=email).exists():
#             return Response({"success": False, "error": "Email already registered."}, status=400)

#         # Create the user
#         user = CustomUser.objects.create_user(username=username, email=email, password=password)

#         # Assign user to a role
#         user.groups.create(name=role)

#         # Assign Lobby if applicable
#         if role in ["Crew Member", "Crew Controller", "Caretaker"] and lobby_id:
#             try:
#                 lobby = Lobby.objects.get(id=lobby_id)
#                 user.LobbyAssigned = lobby
#             except Lobby.DoesNotExist:
#                 return Response({"success": False, "error": "Invalid lobby ID."}, status=400)

#         user.save()

#         return Response({"success": True, "message": "User registered successfully."})

from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist

class RegisterAPIView(APIView):
    permission_classes = [AllowAny]  # Allow public access for registration

    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        role = request.data.get("role", None)  # User should select from existing roles
        lobby_id = request.data.get("lobby_id")  # Lobby Assignment

        # **Step 1: Check if username or email already exists**
        if CustomUser.objects.filter(username=username).exists():
            return Response({"success": False, "error": "Username already taken."}, status=400)

        if CustomUser.objects.filter(email=email).exists():
            return Response({"success": False, "error": "Email already registered."}, status=400)

        # **Step 2: Validate the Role** (Users can only select from existing groups)
        allowed_roles = ["Crew Member", "Crew Controller", "Caretaker", "Contractor"]  # Predefined roles
        if role not in allowed_roles:
            return Response({"success": False, "error": "Invalid role selected."}, status=400)

        # **Step 3: Create the User**
        user = CustomUser.objects.create_user(username=username, email=email, password=password)

        # **Step 4: Assign the User to the Existing Role**
        try:
            group = Group.objects.get(name=role)  # ✅ Only fetch existing groups
            user.groups.add(group)
        except ObjectDoesNotExist:
            return Response({"success": False, "error": "Role does not exist. Contact admin."}, status=400)

        # **Step 5: Assign Lobby (if applicable)**
        if role in ["Crew Member", "Crew Controller", "Caretaker"] and lobby_id:
            try:
                lobby = Lobby.objects.get(id=lobby_id)
                user.LobbyAssigned = lobby
            except Lobby.DoesNotExist:
                return Response({"success": False, "error": "Invalid lobby ID."}, status=400)

        user.save()

        return Response({"success": True, "message": "User registered successfully."})
