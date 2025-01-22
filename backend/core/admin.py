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
### admin.py ###
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Zone, Division, Lobby, Room, Bed, CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'LobbyAssigned', 'is_staff')

# Register your models
admin.site.register(Zone)
admin.site.register(Division)
admin.site.register(Lobby)
admin.site.register(Room)
admin.site.register(Bed)
