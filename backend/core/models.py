# # # # from django.db import models

# # # # Create your models here.
# # # from django.db import models


# # # class Zone(models.Model):
# # #     name = models.CharField(max_length=255, unique=True)
# # #     code = models.CharField(max_length=10, unique=True)

# # #     def __str__(self):
# # #         return self.name


# # # class Division(models.Model):
# # #     zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name='divisions')
# # #     name = models.CharField(max_length=255)
# # #     code = models.CharField(max_length=10, unique=True)

# # #     def __str__(self):
# # #         return f"{self.name} ({self.zone.name})"


# # # class Lobby(models.Model):
# # #     division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='lobbies')
# # #     name = models.CharField(max_length=255)
# # #     location = models.CharField(max_length=255)

# # #     def __str__(self):
# # #         return f"{self.name} ({self.division.name})"


# # # class Room(models.Model):
# # #     lobby = models.ForeignKey(Lobby, on_delete=models.CASCADE, related_name='rooms')
# # #     room_number = models.CharField(max_length=10)

# # #     def __str__(self):
# # #         return f"Room {self.room_number} in {self.lobby.name}"


# # # class Bed(models.Model):
# # #     room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='beds')
# # #     status = models.CharField(max_length=20, choices=[
# # #         ('Available', 'Available'),
# # #         ('Occupied', 'Occupied'),
# # #         ('Reserved', 'Reserved'),
# # #         ('Maintenance', 'Maintenance'),
# # #     ], default='Available')

# # #     def __str__(self):
# # #         return f"Bed in {self.room.room_number} ({self.status})"


# # # class FoodToken(models.Model):
# # #     crew_name = models.CharField(max_length=255)
# # #     meal_type = models.CharField(max_length=50, choices=[
# # #         ('Breakfast', 'Breakfast'),
# # #         ('Lunch', 'Lunch'),
# # #         ('Dinner', 'Dinner'),
# # #     ])
# # #     status = models.CharField(max_length=20, default='Pending')

# # #     class Meta:
# # #         permissions = [
# # #             ("view_own_foodtoken", "Can view own food tokens"),
# # #         ]

# # #     def __str__(self):
# # #         return f"{self.crew_name}'s {self.meal_type} token ({self.status})"

# # # class Feedback(models.Model):
# # #     user_name = models.CharField(max_length=255)
# # #     feedback_type = models.CharField(max_length=50, choices=[
# # #         ('Food', 'Food'),
# # #         ('Bed', 'Bed'),
# # #         ('Staff', 'Staff'),
# # #         ('Other', 'Other'),
# # #     ])
# # #     comment = models.TextField()
# # #     rating = models.PositiveIntegerField()

# # #     class Meta:
# # #         permissions = [
# # #             ("view_own_feedback", "Can view own feedback"),
# # #         ]

# # #     def __str__(self):
# # #         return f"Feedback by {self.user_name} ({self.feedback_type})"


# # # from django.contrib.auth.models import AbstractUser
# # # from django.db import models
# # # from core.models import Lobby

# # # class CustomUser(AbstractUser):
# # #     LobbyAssigned = models.ForeignKey(
# # #         Lobby, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_users'
# # #     )

# # #     def __str__(self):
# # #         return self.username


# # from django.db import models
# # from django.contrib.auth.models import AbstractUser


# # class Zone(models.Model):
# #     name = models.CharField(max_length=255, unique=True)
# #     code = models.CharField(max_length=10, unique=True)

# #     def __str__(self):
# #         return self.name


# # class Division(models.Model):
# #     zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name='divisions')
# #     name = models.CharField(max_length=255)
# #     code = models.CharField(max_length=10, unique=True)

# #     def __str__(self):
# #         return f"{self.name} ({self.zone.name})"


# # class Lobby(models.Model):
# #     division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='lobbies')
# #     name = models.CharField(max_length=255)
# #     location = models.CharField(max_length=255)

# #     def __str__(self):
# #         return f"{self.name} ({self.division.name})"


# # class Room(models.Model):
# #     lobby = models.ForeignKey(Lobby, on_delete=models.CASCADE, related_name='rooms')
# #     room_number = models.CharField(max_length=10)

# #     def __str__(self):
# #         return f"Room {self.room_number} in {self.lobby.name}"


# # class Bed(models.Model):
# #     room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='beds')
# #     status = models.CharField(max_length=20, choices=[
# #         ('Available', 'Available'),
# #         ('Occupied', 'Occupied'),
# #         ('Reserved', 'Reserved'),
# #         ('Maintenance', 'Maintenance'),
# #     ], default='Available')

# #     def __str__(self):
# #         return f"Bed in {self.room.room_number} ({self.status})"


# # class FoodToken(models.Model):
# #     crew_name = models.CharField(max_length=255)
# #     meal_type = models.CharField(max_length=50, choices=[
# #         ('Breakfast', 'Breakfast'),
# #         ('Lunch', 'Lunch'),
# #         ('Dinner', 'Dinner'),
# #     ])
# #     status = models.CharField(max_length=20, default='Pending')

# #     class Meta:
# #         permissions = [
# #             ("view_own_foodtoken", "Can view own food tokens"),
# #         ]

# #     def __str__(self):
# #         return f"{self.crew_name}'s {self.meal_type} token ({self.status})"


# # class Feedback(models.Model):
# #     user_name = models.CharField(max_length=255)
# #     feedback_type = models.CharField(max_length=50, choices=[
# #         ('Food', 'Food'),
# #         ('Bed', 'Bed'),
# #         ('Staff', 'Staff'),
# #         ('Other', 'Other'),
# #     ])
# #     comment = models.TextField()
# #     rating = models.PositiveIntegerField()

# #     class Meta:
# #         permissions = [
# #             ("view_own_feedback", "Can view own feedback"),
# #         ]

# #     def __str__(self):
# #         return f"Feedback by {self.user_name} ({self.feedback_type})"


# # # class CustomUser(AbstractUser):
# # #     LobbyAssigned = models.ForeignKey(
# # #         Lobby, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_users'
# # #     )

# # #     def __str__(self):
# # #         return self.username


# # class CustomUser(AbstractUser):
# #     LobbyAssigned = models.ForeignKey(
# #         'Lobby', on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_users'
# #     )

# #     def __str__(self):
# #         return self.username

# #     class Meta:
# #         verbose_name = "User"
# #         verbose_name_plural = "Users"
# #         app_label = "auth"  # Move to Authentication and Authorization

# ### models.py ###
# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.utils.timezone import now

# class Zone(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#     code = models.CharField(max_length=10, unique=True)

#     def __str__(self):
#         return self.name

# class Division(models.Model):
#     zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name='divisions')
#     name = models.CharField(max_length=255)
#     code = models.CharField(max_length=10, unique=True)

#     def __str__(self):
#         return f"{self.name} ({self.zone.name})"

# class Lobby(models.Model):
#     division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='lobbies')
#     name = models.CharField(max_length=255)
#     location = models.CharField(max_length=255)

#     def __str__(self):
#         return f"{self.name} ({self.division.name})"

# class Room(models.Model):
#     lobby = models.ForeignKey(Lobby, on_delete=models.CASCADE, related_name='rooms')
#     room_number = models.CharField(max_length=10)

#     def __str__(self):
#         return f"Room {self.room_number} in {self.lobby.name}"

# class Bed(models.Model):
#     room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='beds')
#     status = models.CharField(max_length=20, choices=[
#         ('Available', 'Available'),
#         ('Occupied', 'Occupied'),
#         ('Reserved', 'Reserved'),
#         ('Maintenance', 'Maintenance'),
#     ], default='Available')

#     def __str__(self):
#         return f"Bed in {self.room.room_number} ({self.status})"

# class CustomUser(AbstractUser):
#     LobbyAssigned = models.ForeignKey(
#         Lobby, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_users'
#     )

#     def __str__(self):
#         return self.username
    
# from django.db import models


# # class FoodToken(models.Model):
# #     crew_name = models.CharField(max_length=255)
# #     meal_type = models.CharField(
# #         max_length=50,
# #         choices=[
# #             ('Breakfast', 'Breakfast'),
# #             ('Lunch', 'Lunch'),
# #             ('Dinner', 'Dinner'),
# #             ('Snacks', 'Snacks'),
# #             ('Parcel', 'Parcel'),
# #         ]
# #     )
# #     status = models.CharField(
# #         max_length=20,
# #         choices=[
# #             ('Pending', 'Pending'),
# #             ('Served', 'Served'),
# #             ('Cancelled', 'Cancelled'),
# #         ],
# #         default='Pending',
# #     )

# #     class Meta:
# #         permissions = [
# #             ("view_own_foodtoken", "Can view own food tokens"),
# #         ]  # Only include custom permissions here; default permissions are auto-generated.

# #     def __str__(self):
# #         return f"{self.crew_name}'s {self.meal_type} token ({self.status})"

# class FoodToken(models.Model):
#     crew_name = models.CharField(max_length=255)
#     meal_type = models.CharField(
#         max_length=50,
#         choices=[
#             ('Breakfast', 'Breakfast'),
#             ('Lunch', 'Lunch'),
#             ('Dinner', 'Dinner'),
#             ('Snacks', 'Snacks'),
#             ('Parcel', 'Parcel'),
#         ]
#     )
#     status = models.CharField(
#         max_length=20,
#         choices=[
#             ('Pending', 'Pending'),
#             ('Served', 'Served'),
#             ('Cancelled', 'Cancelled'),
#         ],
#         default='Pending',
#     )
#     lobby = models.ForeignKey('Lobby', on_delete=models.SET_NULL, null=True, blank=True)
#     created_at = models.DateTimeField(default=now, editable=False)

#     def __str__(self):
#         return f"{self.crew_name}'s {self.meal_type} token ({self.status})"

# # class Feedback(models.Model):
# #     user_name = models.CharField(max_length=255)
# #     feedback_type = models.CharField(
# #         max_length=50,
# #         choices=[
# #             ('Food', 'Food'),
# #             ('Bed', 'Bed'),
# #             ('Staff', 'Staff'),
# #             ('Other', 'Other'),
# #         ]
# #     )
# #     comment = models.TextField()
# #     rating = models.PositiveIntegerField()

# #     class Meta:
# #         permissions = [
# #             ("view_own_feedback", "Can view own feedback"),
# #         ]

# #     def __str__(self):
# #         return f"Feedback by {self.user_name} ({self.feedback_type})"
# class FoodToken(models.Model):
#     crew_name = models.CharField(max_length=255)
#     meal_type = models.CharField(
#         max_length=50,
#         choices=[
#             ('Breakfast', 'Breakfast'),
#             ('Lunch', 'Lunch'),
#             ('Dinner', 'Dinner'),
#             ('Snacks', 'Snacks'),
#             ('Parcel', 'Parcel'),
#         ]
#     )
#     status = models.CharField(
#         max_length=20,
#         choices=[
#             ('Pending', 'Pending'),
#             ('Served', 'Served'),
#             ('Cancelled', 'Cancelled'),
#         ],
#         default='Pending',
#     )
#     lobby = models.ForeignKey('Lobby', on_delete=models.SET_NULL, null=True, blank=True)
#     created_at = models.DateTimeField(default=now, editable=False)

#     def __str__(self):
#         return f"{self.crew_name}'s {self.meal_type} token ({self.status})"

# ### models.py ###
# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.utils.timezone import now

# class Zone(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#     code = models.CharField(max_length=10, unique=True)

#     def __str__(self):
#         return self.name

# class Division(models.Model):
#     zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name='divisions')
#     name = models.CharField(max_length=255)
#     code = models.CharField(max_length=10, unique=True)

#     def __str__(self):
#         return f"{self.name} ({self.zone.name})"

# class Lobby(models.Model):
#     division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='lobbies')
#     name = models.CharField(max_length=255)
#     location = models.CharField(max_length=255)

#     def __str__(self):
#         return f"{self.name} ({self.division.name})"

# class Room(models.Model):
#     lobby = models.ForeignKey(Lobby, on_delete=models.CASCADE, related_name='rooms')
#     room_number = models.CharField(max_length=10)

#     def __str__(self):
#         return f"Room {self.room_number} in {self.lobby.name}"

# class Bed(models.Model):
#     room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='beds')
#     status = models.CharField(max_length=20, choices=[
#         ('Available', 'Available'),
#         ('Occupied', 'Occupied'),
#         ('Reserved', 'Reserved'),
#         ('Maintenance', 'Maintenance'),
#     ], default='Available')

#     def __str__(self):
#         return f"Bed in {self.room.room_number} ({self.status})"

# class FoodToken(models.Model):
#     crew_name = models.CharField(max_length=255)
#     meal_type = models.CharField(
#         max_length=50,
#         choices=[
#             ('Breakfast', 'Breakfast'),
#             ('Lunch', 'Lunch'),
#             ('Dinner', 'Dinner'),
#             ('Snacks', 'Snacks'),
#             ('Parcel', 'Parcel'),
#         ]
#     )
#     status = models.CharField(
#         max_length=20,
#         choices=[
#             ('Pending', 'Pending'),
#             ('Served', 'Served'),
#             ('Cancelled', 'Cancelled'),
#         ],
#         default='Pending',
#     )
#     lobby = models.ForeignKey('Lobby', on_delete=models.SET_NULL, null=True, blank=True)
#     created_at = models.DateTimeField(default=now, editable=False)

#     def __str__(self):
#         return f"{self.crew_name}'s {self.meal_type} token ({self.status})"

# class Feedback(models.Model):
#     user_name = models.CharField(max_length=255)
#     feedback_type = models.CharField(
#         max_length=50,
#         choices=[
#             ('Food', 'Food'),
#             ('Bed', 'Bed'),
#             ('Staff', 'Staff'),
#             ('Other', 'Other'),
#         ]
#     )
#     comment = models.TextField()
#     rating = models.PositiveIntegerField(
#         choices=[
#             (1, 'Very Bad'),
#             (2, 'Bad'),
#             (3, 'Neutral'),
#             (4, 'Good'),
#             (5, 'Excellent'),
#         ]
#     )
#     lobby = models.ForeignKey('Lobby', on_delete=models.SET_NULL, null=True, blank=True)
#     created_at = models.DateTimeField(default=now, editable=False)

#     def __str__(self):
#         return f"Feedback by {self.user_name} ({self.feedback_type})"

# class CustomUser(AbstractUser):
#     LobbyAssigned = models.ForeignKey(
#         Lobby, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_users'
#     )

#     def __str__(self):
#         return self.username

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.core.exceptions import ValidationError


class Zone(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Division(models.Model):
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name='divisions')
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name} ({self.zone.name})"


# class Lobby(models.Model):
#     division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='lobbies')
#     name = models.CharField(max_length=255)
#     location = models.CharField(max_length=255)

#     def __str__(self):
#         return f"{self.name} ({self.division.name})"



class Lobby(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='lobbies')
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    lobby_code = models.CharField(max_length=10, unique=True, help_text="Lobby Code")  # New field for Lobby Code

    def clean(self):
        # Ensure lobby_code corresponds to the railway station code
        if not self.lobby_code.isalpha() or len(self.lobby_code) > 4:
            raise ValidationError('Lobby code must be a valid railway station code (max 4 letters).')

    def __str__(self):
        return f"{self.name} ({self.lobby_code})"



class Room(models.Model):
    lobby = models.ForeignKey(Lobby, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return f"Room {self.room_number} in {self.lobby.name}"


class Bed(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='beds')
    status = models.CharField(max_length=20, choices=[
        ('Available', 'Available'),
        ('Occupied', 'Occupied'),
        ('Reserved', 'Reserved'),
        ('Maintenance', 'Maintenance'),
    ], default='Available')

    def __str__(self):
        return f"Bed in {self.room.room_number} ({self.status})"


class FoodToken(models.Model):
    crew_name = models.CharField(max_length=255)
    meal_type = models.CharField(
        max_length=50,
        choices=[
            ('Breakfast', 'Breakfast'),
            ('Lunch', 'Lunch'),
            ('Dinner', 'Dinner'),
            ('Snacks', 'Snacks'),
            ('Parcel', 'Parcel'),
        ]
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Served', 'Served'),
            ('Cancelled', 'Cancelled'),
        ],
        default='Pending',
    )
    lobby = models.ForeignKey('Lobby', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return f"{self.crew_name}'s {self.meal_type} token ({self.status})"


class Feedback(models.Model):
    user_name = models.CharField(max_length=255)
    feedback_type = models.CharField(
        max_length=50,
        choices=[
            ('Food', 'Food'),
            ('Bed', 'Bed'),
            ('Staff', 'Staff'),
            ('Other', 'Other'),
        ]
    )
    comment = models.TextField()
    rating = models.PositiveIntegerField(
        choices=[
            (1, 'Very Bad'),
            (2, 'Bad'),
            (3, 'Neutral'),
            (4, 'Good'),
            (5, 'Excellent'),
        ]
    )
    lobby = models.ForeignKey('Lobby', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return f"Feedback by {self.user_name} ({self.feedback_type})"


class CustomUser(AbstractUser):
    DESIGNATION_CHOICES = [
        ('LP', 'Loco Pilot'),
        ('ALP', 'Assistant Loco Pilot'),
        ('SALP', 'Senior Assistant Loco Pilot'),
        ('LPG', 'Loco Pilot Goods'),
        ('SHT', 'Shunter'),
        ('SSHT', 'Senior Shunter'),
        ('LPP', 'Loco Pilot Passenger'),
        ('LPM', 'Loco Pilot Mail'),
        ('MMAN', 'Motorman'),
        ('AGR', 'Assistant Guard'),
        ('SAGR', 'Senior Assistant Guard'),
        ('GD', 'Guard'),
        ('SGD', 'Senior Guard'),
        ('SGDP', 'Guard Passenger'),
        ('GDM', 'Guard Mail'),
        ('Others', 'Others'),
    ]

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    designation = models.CharField(
        max_length=20,
        choices=DESIGNATION_CHOICES,
        null=True,
        blank=True,
        help_text="Designation for Crew Members"
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    mobile_number = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        blank=True,
        help_text="Mobile number for the user. Must be unique."
    )
    LobbyAssigned = models.ForeignKey(
        Lobby, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_users'
    )

    def __str__(self):
        return f"{self.username} ({self.get_designation_display() if self.designation else 'N/A'})"


class RegistrationRequest(models.Model):
    ROLE_CHOICES = [
        ('Crew Member', 'Crew Member'),
        ('Crew Controller', 'Crew Controller'),
        ('Caretaker', 'Caretaker'),
        ('Contractor', 'Contractor'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='registration_request')
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    designation = models.CharField(
        max_length=20,
        choices=CustomUser.DESIGNATION_CHOICES,
        null=True,
        blank=True,
        help_text="Designation is required for Crew Members"
    )
    is_approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_requests'
    )
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Registration Request for {self.user.username} ({self.role})"
