# # # # # from django.contrib import admin

# # # # # # Register your models here.

# # # # # from django.contrib import admin
# # # # # from .models import Zone, Division, Lobby  # Import your models here

# # # # # # Register your models
# # # # # admin.site.register(Zone)
# # # # # admin.site.register(Division)
# # # # # admin.site.register(Lobby)

# # # # # from django.contrib import admin
# # # # # from django.contrib.auth.admin import UserAdmin
# # # # # from .models import CustomUser

# # # # # @admin.register(CustomUser)
# # # # # class CustomUserAdmin(UserAdmin):
# # # # #     model = CustomUser
# # # # #     list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

# # # # # # from django.contrib import admin
# # # # # # from django.contrib.auth.models import User

# # # # # # admin.site.register(User)

# # # # from django.contrib import admin
# # # # from django.contrib.auth.admin import UserAdmin
# # # # from .models import Zone, Division, Lobby, Room, Bed, FoodToken, Feedback, CustomUser

# # # # # Register your models
# # # # @admin.register(Zone)
# # # # class ZoneAdmin(admin.ModelAdmin):
# # # #     list_display = ('name', 'code')
# # # #     search_fields = ('name', 'code')


# # # # @admin.register(Division)
# # # # class DivisionAdmin(admin.ModelAdmin):
# # # #     list_display = ('name', 'code', 'zone')
# # # #     search_fields = ('name', 'code', 'zone__name')


# # # # @admin.register(Lobby)
# # # # class LobbyAdmin(admin.ModelAdmin):
# # # #     list_display = ('name', 'location', 'division')
# # # #     search_fields = ('name', 'location', 'division__name')


# # # # @admin.register(CustomUser)
# # # # class CustomUserAdmin(UserAdmin):
# # # #     model = CustomUser
# # # #     list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'LobbyAssigned')
# # # #     list_filter = ('is_staff', 'is_active', 'groups')
# # # #     fieldsets = (
# # # #         (None, {'fields': ('username', 'password')}),
# # # #         ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
# # # #         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
# # # #         ('Assigned Lobby', {'fields': ('LobbyAssigned',)}),
# # # #         ('Important dates', {'fields': ('last_login', 'date_joined')}),
# # # #     )
# # # # ### admin.py ###
# # # # from django.contrib import admin
# # # # from django.contrib.auth.admin import UserAdmin
# # # # from .models import Zone, Division, Lobby, Room, Bed, CustomUser, FoodToken, Feedback

# # # # @admin.register(CustomUser)
# # # # class CustomUserAdmin(UserAdmin):
# # # #     model = CustomUser
# # # #     list_display = ('username', 'email', 'first_name', 'last_name', 'LobbyAssigned', 'is_staff')

# # # # @admin.register(FoodToken)
# # # # class FoodTokenAdmin(admin.ModelAdmin):
# # # #     list_display = ('crew_name', 'meal_type', 'status')
# # # #     list_filter = ('meal_type', 'status')
# # # #     search_fields = ('crew_name', 'meal_type')

# # # # @admin.register(Feedback)
# # # # class FeedbackAdmin(admin.ModelAdmin):
# # # #     list_display = ['user_name', 'feedback_type', 'rating']
# # # #     search_fields = ['user_name', 'feedback_type']

# # # # # Register your models
# # # # admin.site.register(Zone)
# # # # admin.site.register(Division)
# # # # admin.site.register(Lobby)
# # # # admin.site.register(Room)
# # # # admin.site.register(Bed)
# # # # admin.site.register(FoodToken)
# # # # admin.site.register(Feedback)

# # # from django.contrib import admin
# # # from .models import Zone, Division, Lobby, Room, Bed, FoodToken, Feedback, CustomUser
# # # from django.contrib.auth.admin import UserAdmin

# # # # Register models
# # # admin.site.register(Zone)
# # # admin.site.register(Division)
# # # admin.site.register(Lobby)
# # # admin.site.register(Room)
# # # admin.site.register(Bed)
# # # # admin.site.register(Feedback)


# # # # Custom Admin for FoodToken (if needed)
# # # @admin.register(FoodToken)
# # # class FoodTokenAdmin(admin.ModelAdmin):
# # #     list_display = ('crew_name', 'meal_type', 'status')  # Add fields to display in the admin list view


# # # # Custom Admin for CustomUser
# # # @admin.register(CustomUser)
# # # class CustomUserAdmin(UserAdmin):
# # #     model = CustomUser
# # #     list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

# # # @admin.register(Feedback)
# # # class FeedbackAdmin(admin.ModelAdmin):
# # #     list_display = ('user_name', 'feedback_type', 'rating')  # Adjust fields as needed

# # from django.contrib import admin
# # from django.contrib.auth.admin import UserAdmin
# # from .models import Zone, Division, Lobby, Room, Bed, FoodToken, Feedback, CustomUser

# # # Admin Registration for Zone
# # @admin.register(Zone)
# # class ZoneAdmin(admin.ModelAdmin):
# #     list_display = ('name', 'code')  # Fields displayed in the admin list view
# #     search_fields = ('name', 'code')  # Fields for the search functionality


# # # Admin Registration for Division
# # @admin.register(Division)
# # class DivisionAdmin(admin.ModelAdmin):
# #     list_display = ('name', 'code', 'zone')  # Fields displayed in the admin list view
# #     search_fields = ('name', 'code', 'zone__name')  # Fields for the search functionality
# # # 

# # # Admin Registration for Lobby
# # @admin.register(Lobby)
# # class LobbyAdmin(admin.ModelAdmin):
# #     list_display = ('name', 'location', 'division')  # Fields displayed in the admin list view
# #     search_fields = ('name', 'location', 'division__name')  # Fields for the search functionality


# # # Admin Registration for Room
# # @admin.register(Room)
# # class RoomAdmin(admin.ModelAdmin):
# #     list_display = ('room_number', 'lobby')  # Fields displayed in the admin list view
# #     search_fields = ('room_number', 'lobby__name')  # Fields for the search functionality


# # # Admin Registration for Bed
# # @admin.register(Bed)
# # class BedAdmin(admin.ModelAdmin):
# #     list_display = ('room', 'status')  # Fields displayed in the admin list view
# #     search_fields = ('room__room_number', 'status')  # Fields for the search functionality


# # # Admin Registration for FoodToken
# # @admin.register(FoodToken)
# # class FoodTokenAdmin(admin.ModelAdmin):
# #     list_display = ('crew_name', 'meal_type', 'status', 'lobby', 'created_at')  # Add fields for better visibility
# #     list_filter = ('meal_type', 'status', 'lobby')  # Filter options in the admin panel
# #     search_fields = ('crew_name', 'meal_type')  # Search fields for admin panel


# # # Admin Registration for Feedback
# # @admin.register(Feedback)
# # class FeedbackAdmin(admin.ModelAdmin):
# #     list_display = ('user_name', 'feedback_type', 'rating', 'lobby', 'created_at')  # Add fields for better visibility
# #     search_fields = ('user_name', 'feedback_type', 'lobby__name')  # Search fields for admin panel


# # # Custom Admin for CustomUser
# # @admin.register(CustomUser)
# # class CustomUserAdmin(UserAdmin):
# #     model = CustomUser
# #     list_display = ('username', 'email', 'first_name', 'last_name', 'LobbyAssigned', 'is_staff', 'is_active')
# #     list_filter = ('is_staff', 'is_active', 'groups', 'LobbyAssigned')  # Filters for CustomUser admin
# #     fieldsets = (
# #         (None, {'fields': ('username', 'password')}),
# #         ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
# #         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
# #         ('Assigned Lobby', {'fields': ('LobbyAssigned',)}),
# #         ('Important dates', {'fields': ('last_login', 'date_joined')}),
# #     )

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import Zone, Division, Lobby, Room, Bed, FoodToken, Feedback, CustomUser

# # Admin for Zone
# @admin.register(Zone)
# class ZoneAdmin(admin.ModelAdmin):
#     list_display = ('name', 'code')
#     search_fields = ('name', 'code')


# # Admin for Division
# @admin.register(Division)
# class DivisionAdmin(admin.ModelAdmin):
#     list_display = ('name', 'code', 'zone')
#     search_fields = ('name', 'code', 'zone__name')


# # Admin for Lobby
# @admin.register(Lobby)
# class LobbyAdmin(admin.ModelAdmin):
#     list_display = ('name', 'location', 'division')
#     search_fields = ('name', 'location', 'division__name')


# # Admin for Room
# @admin.register(Room)
# class RoomAdmin(admin.ModelAdmin):
#     list_display = ('room_number', 'lobby')
#     search_fields = ('room_number', 'lobby__name')


# # Admin for Bed
# @admin.register(Bed)
# class BedAdmin(admin.ModelAdmin):
#     list_display = ('room', 'status')
#     search_fields = ('room__room_number', 'status')


# # Admin for FoodToken
# @admin.register(FoodToken)
# class FoodTokenAdmin(admin.ModelAdmin):
#     list_display = ('crew_name', 'meal_type', 'status', 'lobby', 'created_at')
#     list_filter = ('meal_type', 'status', 'lobby')
#     search_fields = ('crew_name', 'meal_type')


# # Admin for Feedback
# @admin.register(Feedback)
# class FeedbackAdmin(admin.ModelAdmin):
#     list_display = ('user_name', 'feedback_type', 'rating', 'lobby', 'created_at')
#     search_fields = ('user_name', 'feedback_type', 'lobby__name')


# # Custom Admin for CustomUser
# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ('username', 'email', 'first_name', 'last_name', 'LobbyAssigned', 'is_staff', 'is_active')
#     list_filter = ('is_staff', 'is_active', 'groups', 'LobbyAssigned')
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Assigned Lobby', {'fields': ('LobbyAssigned',)}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )


### admin.py ###
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Zone, Division, Lobby, Room, Bed, CustomUser, FoodToken, Feedback

# Admin for Zone
@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')

# Admin for Division
@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'zone')
    search_fields = ('name', 'code', 'zone__name')

# Admin for Lobby
@admin.register(Lobby)
class LobbyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'division')
    search_fields = ('name', 'location', 'division__name')

# Admin for Room
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'lobby')
    search_fields = ('room_number', 'lobby__name')

# Admin for Bed
@admin.register(Bed)
class BedAdmin(admin.ModelAdmin):
    list_display = ('room', 'status')
    search_fields = ('room__room_number', 'status')

# Admin for FoodToken
@admin.register(FoodToken)
class FoodTokenAdmin(admin.ModelAdmin):
    list_display = ('crew_name', 'meal_type', 'status', 'lobby', 'created_at')
    list_filter = ('meal_type', 'status', 'lobby')
    search_fields = ('crew_name', 'meal_type')

# Admin for Feedback
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'feedback_type', 'rating', 'lobby', 'created_at')
    search_fields = ('user_name', 'feedback_type', 'lobby__name')

# Custom Admin for CustomUser
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'LobbyAssigned', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'groups', 'LobbyAssigned')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Assigned Lobby', {'fields': ('LobbyAssigned',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
