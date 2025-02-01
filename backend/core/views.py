

# ### views.py ###
# from rest_framework import viewsets, filters
# from django_filters.rest_framework import DjangoFilterBackend
# from .models import Zone, Division, Lobby, Room, Bed, FoodToken, Feedback, CustomUser
# from .serializers import (
#     ZoneSerializer, DivisionSerializer, LobbySerializer, RoomSerializer,
#     BedSerializer, FoodTokenSerializer, FeedbackSerializer, CustomUserSerializer
# )

# class ZoneViewSet(viewsets.ModelViewSet):
#     queryset = Zone.objects.all()
#     serializer_class = ZoneSerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_fields = ['name', 'code']
#     search_fields = ['name', 'code']
#     permission_classes = []

# class DivisionViewSet(viewsets.ModelViewSet):
#     queryset = Division.objects.all()
#     serializer_class = DivisionSerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_fields = ['zone__name', 'name', 'code']
#     search_fields = ['name', 'code']
#     permission_classes = []

# class LobbyViewSet(viewsets.ModelViewSet):
#     queryset = Lobby.objects.all()
#     serializer_class = LobbySerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_fields = ['division__name', 'name', 'location']
#     search_fields = ['name', 'location']
#     permission_classes = []

# class RoomViewSet(viewsets.ModelViewSet):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_fields = ['lobby__name', 'room_number']
#     search_fields = ['room_number']
#     permission_classes = []

# # class BedViewSet(viewsets.ModelViewSet):
# #     queryset = Bed.objects.all()
# #     serializer_class = BedSerializer
# #     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
# #     filterset_fields = ['room__room_number', 'status']
# #     search_fields = ['status']
# #     permission_classes = []

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
# #---
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.contrib.auth import authenticate

# class LoginAPIView(APIView):
#     permission_classes = []  # Allow access without authentication

#     def post(self, request):
#         username = request.data.get("username")
#         password = request.data.get("password")
#         user = authenticate(username=username, password=password)

#         if user:
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 "success": True,
#                 "refresh": str(refresh),
#                 "access": str(refresh.access_token),
#                 # "role": user.groups.first().name if user.groups.exists() else "user",
#                 "role": user.groups.first().name if user.groups.exists() else "No role assigned",
#                 "username": user.username,
#                 "email": user.email,
#             })
#         return Response({"success": False, "error": "Invalid credentials"}, status=401)

# from rest_framework.permissions import IsAuthenticated

# class ProfileAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         user = request.user
#         return Response({
#             "username": user.username,
#             "email": user.email,
#             "role": user.groups.first().name if user.groups.exists() else "user",
#             "lobby": user.LobbyAssigned.name if user.LobbyAssigned else "No lobby assigned",
#         })
    
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.contrib.auth.models import User
# from core.models import CustomUser, Lobby
# from rest_framework.permissions import AllowAny

# from django.contrib.auth.models import Group
# from django.core.exceptions import ObjectDoesNotExist

# class RegisterAPIView(APIView):
#     permission_classes = [AllowAny]  # Allow public access for registration

#     def post(self, request):
#         username = request.data.get("username")
#         email = request.data.get("email")
#         password = request.data.get("password")
#         role = request.data.get("role", None)  # User should select from existing roles
#         lobby_id = request.data.get("lobby_id")  # Lobby Assignment

#         # **Step 1: Check if username or email already exists**
#         if CustomUser.objects.filter(username=username).exists():
#             return Response({"success": False, "error": "Username already taken."}, status=400)

#         if CustomUser.objects.filter(email=email).exists():
#             return Response({"success": False, "error": "Email already registered."}, status=400)

#         # **Step 2: Validate the Role** (Users can only select from existing groups)
#         allowed_roles = ["Crew Member", "Crew Controller", "Caretaker", "Contractor"]  # Predefined roles
#         if role not in allowed_roles:
#             return Response({"success": False, "error": "Invalid role selected."}, status=400)

#         # **Step 3: Create the User**
#         user = CustomUser.objects.create_user(username=username, email=email, password=password)

#         # **Step 4: Assign the User to the Existing Role**
#         try:
#             group = Group.objects.get(name=role)  # ✅ Only fetch existing groups
#             user.groups.add(group)
#         except ObjectDoesNotExist:
#             return Response({"success": False, "error": "Role does not exist. Contact admin."}, status=400)

#         # **Step 5: Assign Lobby (if applicable)**
#         if role in ["Crew Member", "Crew Controller", "Caretaker"] and lobby_id:
#             try:
#                 lobby = Lobby.objects.get(id=lobby_id)
#                 user.LobbyAssigned = lobby
#             except Lobby.DoesNotExist:
#                 return Response({"success": False, "error": "Invalid lobby ID."}, status=400)

#         user.save()

#         return Response({"success": True, "message": "User registered successfully."})

# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from core.models import Bed
# from core.serializers import BedSerializer

# class BedViewSet(viewsets.ModelViewSet):
#     queryset = Bed.objects.all()
#     serializer_class = BedSerializer
#     permission_classes = []

#     def list(self, request):
#         """
#         GET /beds/ - List all beds, filterable by status.
#         """
#         status_filter = request.query_params.get("status", None)
#         if status_filter:
#             beds = Bed.objects.filter(status=status_filter)
#         else:
#             beds = Bed.objects.all()

#         serializer = BedSerializer(beds, many=True)
#         return Response(serializer.data)






# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import status
# from .models import Bed, CustomUser
# from core.serializers import BedSerializer
# from django.shortcuts import get_object_or_404

# class AssignBedAPIView(APIView):
#     permission_classes = [IsAuthenticated]  # Ensure authentication required

#     def post(self, request):
#         bed_id = request.data.get("bed_id")
#         crew_id = request.data.get("crew_id")

#         # Validate IDs
#         try:
#             bed = Bed.objects.get(id=bed_id)
#             user = CustomUser.objects.get(id=crew_id)
#         except Bed.DoesNotExist:
#             return Response({"error": "Bed not found"}, status=status.HTTP_404_NOT_FOUND)
#         except CustomUser.DoesNotExist:
#             return Response({"error": "Crew Member not found"}, status=status.HTTP_404_NOT_FOUND)

#         # Check if bed is available
#         if bed.status not in ["Available", "Reserved"]:
#             return Response({"error": "Bed is not available for assignment"}, status=status.HTTP_400_BAD_REQUEST)

#         # Assign bed
#         bed.assigned_to = user
#         bed.status = "Occupied"
#         bed.save()

#         return Response({"message": "Bed assigned successfully"}, status=status.HTTP_200_OK)


# class ReleaseBedAPIView(APIView):
#     def post(self, request):
#         """
#         Release a bed (mark it as Available or Reserved).
#         """
#         bed_id = request.data.get("bed_id")
#         new_status = request.data.get("status", "Available")  # Default to Available

#         if new_status not in ["Available", "Reserved"]:
#             return Response({"error": "Invalid status for release"}, status=status.HTTP_400_BAD_REQUEST)

#         bed = get_object_or_404(Bed, id=bed_id)
#         bed.assigned_to = None
#         bed.status = new_status
#         bed.save()

#         return Response({"message": f"Bed released and marked as {new_status}"}, status=status.HTTP_200_OK)

# class UpdateBedStatusAPIView(APIView):
#     def put(self, request):
#         """
#         Update bed status (Caretaker only).
#         """
#         bed_id = request.data.get("bed_id")
#         new_status = request.data.get("status")

#         if new_status not in ["Available", "Occupied", "Reserved", "Maintenance"]:
#             return Response({"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)

#         bed = get_object_or_404(Bed, id=bed_id)
#         bed.status = new_status
#         bed.save()

#         return Response({"message": f"Bed status updated to {new_status}"}, status=status.HTTP_200_OK)

#-------------------------------------------------------#

from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.timezone import now  # Ensure this import is present
from core.models import Zone, Division, Lobby, Room, Bed, FoodToken, Feedback, CustomUser, CheckInHistory
from core.serializers import (
    ZoneSerializer, DivisionSerializer, LobbySerializer, RoomSerializer,
    BedSerializer, FoodTokenSerializer, FeedbackSerializer, CustomUserSerializer
)

import json

### ------------------------------------ ###
### ✅ Generic ViewSets for Models ###
### ------------------------------------ ###

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
    permission_classes = []

    def list(self, request):
        """
        GET /api/beds/ - List all beds, filterable by status.
        """
        status_filter = request.query_params.get("status", None)
        if status_filter:
            beds = Bed.objects.filter(status=status_filter)
        else:
            beds = Bed.objects.all()

        serializer = BedSerializer(beds, many=True)
        return Response(serializer.data)

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

### ------------------------------------ ###
### ✅ Authentication & User Profile APIs ###
### ------------------------------------ ###

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
                "role": user.groups.first().name if user.groups.exists() else "No role assigned",
                "username": user.username,
                "email": user.email,
            })
        return Response({"success": False, "error": "Invalid credentials"}, status=401)

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

class RegisterAPIView(APIView):
    permission_classes = [AllowAny]  # Allow public access for registration

    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        role = request.data.get("role", None)
        lobby_id = request.data.get("lobby_id")

        # Check for existing username/email
        if CustomUser.objects.filter(username=username).exists():
            return Response({"success": False, "error": "Username already taken."}, status=400)
        if CustomUser.objects.filter(email=email).exists():
            return Response({"success": False, "error": "Email already registered."}, status=400)

        # Validate role
        allowed_roles = ["Crew Member", "Crew Controller", "Caretaker", "Contractor"]
        if role not in allowed_roles:
            return Response({"success": False, "error": "Invalid role selected."}, status=400)

        # Create the user
        user = CustomUser.objects.create_user(username=username, email=email, password=password)

        # Assign Role
        try:
            group = Group.objects.get(name=role)
            user.groups.add(group)
        except ObjectDoesNotExist:
            return Response({"success": False, "error": "Role does not exist. Contact admin."}, status=400)

        # Assign Lobby if applicable
        if role in ["Crew Member", "Crew Controller", "Caretaker"] and lobby_id:
            try:
                lobby = Lobby.objects.get(id=lobby_id)
                user.LobbyAssigned = lobby
            except Lobby.DoesNotExist:
                return Response({"success": False, "error": "Invalid lobby ID."}, status=400)

        user.save()
        return Response({"success": True, "message": "User registered successfully."})

### ------------------------------------ ###
### ✅ Bed Assignment APIs ###
### ------------------------------------ ###

#---
# class AssignBedAPIView(APIView):
#     def post(self, request):
#         return Response({"message": "POST request to AssignBedAPIView received!"}, status=200)

#---

class AssignBedAPIView(APIView):
    permission_classes = [IsAuthenticated]  
    http_method_names = ["post"]  # Ensure POST is allowed

    def post(self, request):
        print("Inside AssignBedAPIView POST method") 
        bed_id = request.data.get("bed_id")
        crew_id = request.data.get("crew_id")

        bed = get_object_or_404(Bed, id=bed_id)
        user = get_object_or_404(CustomUser, id=crew_id)

        # bed_id = request.data.get("bed_id")
        # crew_id = request.user.id  # Crew is assigning themselves a bed
        # crew = get_object_or_404(CustomUser, id=crew_id)
        # bed = get_object_or_404(Bed, id=bed_id)

        if bed.status not in ["Available", "Reserved"]:
            return Response({"error": "Bed is not available for assignment"}, status=status.HTTP_400_BAD_REQUEST)

        bed.assigned_to = user
        bed.status = "Occupied"
        bed.save()

        # Store check-in history
        # check_in = CheckInHistory.objects.create(
        #     crew=crew,
        #     crew_name=crew.username,
        #     crew_hq_lobby=crew.LobbyAssigned,
        #     checked_in_lobby=bed.room.lobby,
        #     bed=bed,
        #     bed_number=bed.number,
        #     check_in_time=now()
        # )

        check_in = CheckInHistory.objects.create(
            crew=user,
            crew_name=user.username,
            crew_hq_lobby=user.LobbyAssigned,
            checked_in_lobby=bed.room.lobby,
            bed=bed,
            bed_number=bed.number,
            check_in_time= now()
        )

        return Response({"message": "Bed assigned successfully"}, status=status.HTTP_200_OK)

class ReleaseBedAPIView(APIView):
    permission_classes = [IsAuthenticated]  
    http_method_names = ["post"]  # Ensure POST is allowed

    def post(self, request):
        bed_id = request.data.get("bed_id")
        new_status = request.data.get("status", "Available")
        crew_id = request.user.id #Added Later

        if new_status not in ["Available", "Reserved"]:
            return Response({"error": "Invalid status for release"}, status=status.HTTP_400_BAD_REQUEST)
        
                # Update Check-In history
        check_in = CheckInHistory.objects.filter(crew_id=crew_id, bed_id=bed_id, check_out_time__isnull=True).first()
        if check_in:
         check_in.check_out_time = now()
         check_in.save()


        bed = get_object_or_404(Bed, id=bed_id)
        bed.assigned_to = None
        bed.status = new_status
        bed.save()

        return Response({"message": f"Bed released and marked as {new_status}"}, status=status.HTTP_200_OK)

class UpdateBedStatusAPIView(APIView):
    

    def put(self, request):
        bed_id = request.data.get("bed_id")
        new_status = request.data.get("status")

        if new_status not in ["Available", "Occupied", "Reserved", "Maintenance"]:
            return Response({"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)

        bed = get_object_or_404(Bed, id=bed_id)
        bed.status = new_status
        bed.save()

        return Response({"message": f"Bed status updated to {new_status}"}, status=status.HTTP_200_OK)

class TestPostAPIView(APIView):
    http_method_names = ["post"]

    def post(self, request):
        return Response({"message": "POST request successful!"}, status=200)
