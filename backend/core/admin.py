# # from django.contrib import admin

# # # Register your models here.

# # from django.contrib import admin
# # from .models import Zone, Division, Lobby  # Import your models here

# # # Register your models
# # admin.site.register(Zone)
# # admin.site.register(Division)
# # admin.site.register(Lobby)

# # from django.contrib import admin
# # from django.contrib.auth.admin import UserAdmin
# # from .models import CustomUser

# # @admin.register(CustomUser)
# # class CustomUserAdmin(UserAdmin):
# #     model = CustomUser
# #     list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

# # # from django.contrib import admin
# # # from django.contrib.auth.models import User

# # # admin.site.register(User)

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import Zone, Division, Lobby, Room, Bed, FoodToken, Feedback, CustomUser

# # Register your models
# @admin.register(Zone)
# class ZoneAdmin(admin.ModelAdmin):
#     list_display = ('name', 'code')
#     search_fields = ('name', 'code')


# @admin.register(Division)
# class DivisionAdmin(admin.ModelAdmin):
#     list_display = ('name', 'code', 'zone')
#     search_fields = ('name', 'code', 'zone__name')


# @admin.register(Lobby)
# class LobbyAdmin(admin.ModelAdmin):
#     list_display = ('name', 'location', 'division')
#     search_fields = ('name', 'location', 'division__name')


# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'LobbyAssigned')
#     list_filter = ('is_staff', 'is_active', 'groups')
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Assigned Lobby', {'fields': ('LobbyAssigned',)}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )
# ### admin.py ###
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import Zone, Division, Lobby, Room, Bed, CustomUser, FoodToken, Feedback

# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ('username', 'email', 'first_name', 'last_name', 'LobbyAssigned', 'is_staff')

# @admin.register(FoodToken)
# class FoodTokenAdmin(admin.ModelAdmin):
#     list_display = ('crew_name', 'meal_type', 'status')
#     list_filter = ('meal_type', 'status')
#     search_fields = ('crew_name', 'meal_type')

# @admin.register(Feedback)
# class FeedbackAdmin(admin.ModelAdmin):
#     list_display = ['user_name', 'feedback_type', 'rating']
#     search_fields = ['user_name', 'feedback_type']

# # Register your models
# admin.site.register(Zone)
# admin.site.register(Division)
# admin.site.register(Lobby)
# admin.site.register(Room)
# admin.site.register(Bed)
# admin.site.register(FoodToken)
# admin.site.register(Feedback)

from django.contrib import admin
from .models import Zone, Division, Lobby, Room, Bed, FoodToken, Feedback, CustomUser
from django.contrib.auth.admin import UserAdmin

# Register models
admin.site.register(Zone)
admin.site.register(Division)
admin.site.register(Lobby)
admin.site.register(Room)
admin.site.register(Bed)
# admin.site.register(Feedback)


# Custom Admin for FoodToken (if needed)
@admin.register(FoodToken)
class FoodTokenAdmin(admin.ModelAdmin):
    list_display = ('crew_name', 'meal_type', 'status')  # Add fields to display in the admin list view


# Custom Admin for CustomUser
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'feedback_type', 'rating')  # Adjust fields as needed