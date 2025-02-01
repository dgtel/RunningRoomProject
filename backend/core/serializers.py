# # # from rest_framework import serializers
# # # from .models import Zone, Division, Lobby, Room, Bed, FoodToken, Feedback, CustomUser


# # # class ZoneSerializer(serializers.ModelSerializer):
# # #     class Meta:
# # #         model = Zone
# # #         fields = '__all__'


# # # class DivisionSerializer(serializers.ModelSerializer):
# # #     class Meta:
# # #         model = Division
# # #         fields = '__all__'


# # # class LobbySerializer(serializers.ModelSerializer):
# # #     class Meta:
# # #         model = Lobby
# # #         fields = '__all__'


# # # class RoomSerializer(serializers.ModelSerializer):
# # #     class Meta:
# # #         model = Room
# # #         fields = '__all__'


# # # class BedSerializer(serializers.ModelSerializer):
# # #     class Meta:
# # #         model = Bed
# # #         fields = '__all__'


# # # class FoodTokenSerializer(serializers.ModelSerializer):
# # #     class Meta:
# # #         model = FoodToken
# # #         fields = '__all__'


# # # class FeedbackSerializer(serializers.ModelSerializer):
# # #     class Meta:
# # #         model = Feedback
# # #         fields = '__all__'

# # # class CustomUserSerializer(serializers.ModelSerializer):
# # #     class Meta:
# # #         model = CustomUser
# # #         fields = ['id', 'username', 'email', 'first_name', 'last_name', 'LobbyAssigned']

# # ### serializers.py ###
# # from rest_framework import serializers
# # from .models import Zone, Division, Lobby, Room, Bed, CustomUser, FoodToken, Feedback

# # class ZoneSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Zone
# #         fields = '__all__'

# # class DivisionSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Division
# #         fields = '__all__'

# # class LobbySerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Lobby
# #         fields = '__all__'

# # class RoomSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Room
# #         fields = '__all__'

# # class BedSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Bed
# #         fields = '__all__'

# # class CustomUserSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = CustomUser
# #         fields = ('username', 'email', 'first_name', 'last_name', 'LobbyAssigned')

# # class FoodTokenSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = FoodToken
# #         fields = '__all__'


# # class FeedbackSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Feedback
# #         fields = '__all__'

# ### serializers.py ###
# from rest_framework import serializers
# from .models import Zone, Division, Lobby, Room, Bed, CustomUser, FoodToken, Feedback

# class ZoneSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Zone
#         fields = '__all__'

# class DivisionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Division
#         fields = '__all__'

# class LobbySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Lobby
#         fields = '__all__'

# class RoomSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Room
#         fields = '__all__'

# # class BedSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Bed
# #         fields = '__all__'

# class BedSerializer(serializers.ModelSerializer):
#     assigned_to_username = serializers.CharField(source='assigned_to.username', read_only=True)

#     class Meta:
#         model = Bed
#         fields = ['id', 'room', 'status', 'assigned_to', 'assigned_to_username']

# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('id', 'username', 'email', 'first_name', 'last_name', 'LobbyAssigned')

# class FoodTokenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FoodToken
#         fields = '__all__'

# class FeedbackSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Feedback
#         fields = '__all__'


from rest_framework import serializers
from .models import Zone, Division, Lobby, Room, Bed, CustomUser, FoodToken, Feedback


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = '__all__'


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = '__all__'


class LobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lobby
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class BedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bed
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "first_name", "last_name", "LobbyAssigned")


class FoodTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodToken
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

