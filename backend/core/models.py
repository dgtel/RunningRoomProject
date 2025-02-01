

# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.utils.timezone import now
# from django.core.exceptions import ValidationError
# from django.contrib.auth import get_user_model



# # ✅ Zone Model
# class Zone(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#     code = models.CharField(max_length=10, unique=True)

#     def __str__(self):
#         return self.name


# # ✅ Division Model
# class Division(models.Model):
#     zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name='divisions')
#     name = models.CharField(max_length=255)
#     code = models.CharField(max_length=10, unique=True)

#     def __str__(self):
#         return f"{self.name} ({self.zone.name})"


# # ✅ Lobby Model
# class Lobby(models.Model):
#     division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='lobbies')
#     name = models.CharField(max_length=255)
#     location = models.CharField(max_length=255)
#     lobby_code = models.CharField(max_length=10, unique=True, help_text="Lobby Code")

#     def clean(self):
#         if not self.lobby_code.isalpha() or len(self.lobby_code) > 4:
#             raise ValidationError('Lobby code must be a valid railway station code (max 4 letters).')

#     def __str__(self):
#         return f"{self.name} ({self.lobby_code})"

# # ✅ Custom User Model
# class CustomUser(AbstractUser):
#     LobbyAssigned = models.ForeignKey(
#         Lobby, on_delete=models.SET_NULL, null=True, blank=True, related_name="assigned_users"
#     )

#     def __str__(self):
#         return self.username

# User = get_user_model()  # ✅ Ensure correct user model reference

# # ✅ Room Model
# class Room(models.Model):
#     lobby = models.ForeignKey(Lobby, on_delete=models.CASCADE, related_name='rooms')
#     room_number = models.CharField(max_length=10)

#     def __str__(self):
#         return f"Room {self.room_number} in {self.lobby.name}"


# # ✅ Updated Bed Model
# class Bed(models.Model):
#     STATUS_CHOICES = [
#         ("Available", "Available"),
#         ("Occupied", "Occupied"),
#         ("Reserved", "Reserved"),
#         ("Maintenance", "Maintenance"),
#     ]

#     # number = models.CharField(max_length=10, unique=True)
#     number = models.CharField(max_length=10, unique=True,null=True)

#     room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="beds")
#     assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Available")

#     def __str__(self):
#         return f"Bed {self.number} - {self.room.room_number} ({self.status})"


# # ✅ Food Token Model
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
#     lobby = models.ForeignKey(Lobby, on_delete=models.SET_NULL, null=True, blank=True)
#     created_at = models.DateTimeField(default=now, editable=False)

#     def __str__(self):
#         return f"{self.crew_name}'s {self.meal_type} token ({self.status})"


# # ✅ Feedback Model
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
#     lobby = models.ForeignKey(Lobby, on_delete=models.SET_NULL, null=True, blank=True)
#     created_at = models.DateTimeField(default=now, editable=False)

#     def __str__(self):
#         return f"Feedback by {self.user_name} ({self.feedback_type})"





# # ✅ Registration Request Model
# class RegistrationRequest(models.Model):
#     ROLE_CHOICES = [
#         ('Crew Member', 'Crew Member'),
#         ('Crew Controller', 'Crew Controller'),
#         ('Caretaker', 'Caretaker'),
#         ('Contractor', 'Contractor'),
#     ]

     

#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="registration_request")
#     role = models.CharField(max_length=50, choices=ROLE_CHOICES)

#     DESIGNATION_CHOICES = [
#         ('LP', 'Loco Pilot'),
#         ('ALP', 'Assistant Loco Pilot'),
#         ('SALP', 'Senior Assistant Loco Pilot'),
#         ('LPG', 'Loco Pilot Goods'),
#         ('SHT', 'Shunter'),
#         ('SSHT', 'Senior Shunter'),
#         ('LPP', 'Loco Pilot Passenger'),
#         ('LPM', 'Loco Pilot Mail'),
#         ('MMAN', 'Motorman'),
#         ('AGR', 'Assistant Guard'),
#         ('SAGR', 'Senior Assistant Guard'),
#         ('GD', 'Guard'),
#         ('SGD', 'Senior Guard'),
#         ('SGDP', 'Guard Passenger'),
#         ('GDM', 'Guard Mail'),
#         ('Others', 'Others'),
#     ]
#     designation = models.CharField(  # ✅ This field must exist
#         max_length=20,
#         choices=DESIGNATION_CHOICES,
#         null=True,
#         blank=True,
#         help_text="Designation is required for Crew Members",
#     )

#     is_approved = models.BooleanField(default=False)
#     approved_by = models.ForeignKey(
#         CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="approved_requests"
#     )
#     created_at = models.DateTimeField(default=now)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"Registration Request for {self.user.username} ({self.role})"


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.core.exceptions import ValidationError

# ✅ Zone Model
class Zone(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

# ✅ Division Model
class Division(models.Model):
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name='divisions')
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name} ({self.zone.name})"

# ✅ Lobby Model
class Lobby(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='lobbies')
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    lobby_code = models.CharField(max_length=10, unique=True, help_text="Lobby Code")

    def clean(self):
        if not self.lobby_code.isalpha() or len(self.lobby_code) > 4:
            raise ValidationError('Lobby code must be a valid railway station code (max 4 letters).')

    def __str__(self):
        return f"{self.name} ({self.lobby_code})"

# ✅ Custom User Model
class CustomUser(AbstractUser):
    LobbyAssigned = models.ForeignKey(
        Lobby, on_delete=models.SET_NULL, null=True, blank=True, related_name="assigned_users"
    )

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

    def __str__(self):
        return self.username

# ✅ Room Model
class Room(models.Model):
    lobby = models.ForeignKey(Lobby, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return f"Room {self.room_number} in {self.lobby.name}"

# ✅ Updated Bed Model
class Bed(models.Model):
    STATUS_CHOICES = [
        ("Available", "Available"),
        ("Occupied", "Occupied"),
        ("Reserved", "Reserved"),
        ("Maintenance", "Maintenance"),
    ]

    number = models.CharField(max_length=10, unique=True, blank=True, default="")  # ✅ Fixed NULL issue
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="beds")
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)  # ✅ Fixed User reference
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Available")

    def __str__(self):
        return f"Bed {self.number} - {self.room.room_number} ({self.status})"

# ✅ Food Token Model
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
    lobby = models.ForeignKey(Lobby, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return f"{self.crew_name}'s {self.meal_type} token ({self.status})"

# ✅ Feedback Model
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
    lobby = models.ForeignKey(Lobby, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return f"Feedback by {self.user_name} ({self.feedback_type})"

# ✅ Registration Request Model
class RegistrationRequest(models.Model):
    ROLE_CHOICES = [
        ('Crew Member', 'Crew Member'),
        ('Crew Controller', 'Crew Controller'),
        ('Caretaker', 'Caretaker'),
        ('Contractor', 'Contractor'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="registration_request")
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    designation = models.CharField(  
        max_length=20,
        choices=CustomUser.DESIGNATION_CHOICES,  # ✅ Fixed reference to CustomUser
        null=True,
        blank=True,
        help_text="Designation is required for Crew Members",
    )
    is_approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="approved_requests")
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Registration Request for {self.user.username} ({self.role})"

# ✅ Check-In History Table
class CheckInHistory(models.Model):
    crew = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="checkins")
    crew_name = models.CharField(max_length=255)
    crew_hq_lobby = models.ForeignKey(Lobby, on_delete=models.SET_NULL, null=True, related_name="crew_hq_lobby")
    checked_in_lobby = models.ForeignKey(Lobby, on_delete=models.SET_NULL, null=True, related_name="checked_in_lobby")
    bed = models.ForeignKey(Bed, on_delete=models.CASCADE)
    bed_number = models.CharField(max_length=10)
    check_in_time = models.DateTimeField(default=now)
    check_out_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.crew_name} ({self.checked_in_lobby.name}) - {self.bed_number}"