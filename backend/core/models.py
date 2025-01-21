# from django.db import models

# Create your models here.
from django.db import models


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


class Lobby(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='lobbies')
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.division.name})"


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
    meal_type = models.CharField(max_length=50, choices=[
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
    ])
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.crew_name}'s {self.meal_type} token ({self.status})"


class Feedback(models.Model):
    user_name = models.CharField(max_length=255)
    feedback_type = models.CharField(max_length=50, choices=[
        ('Food', 'Food'),
        ('Bed', 'Bed'),
        ('Staff', 'Staff'),
        ('Other', 'Other'),
    ])
    comment = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f"Feedback by {self.user_name} ({self.feedback_type})"
