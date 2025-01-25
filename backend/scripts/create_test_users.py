import os
import django
from random import randint, choice
from django.contrib.auth.models import Group
from core.models import CustomUser, Lobby

# Set the correct Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backendapp.settings")  # Update as per your structure
django.setup()

# Random data generation functions
def random_phone():
    return f"{randint(6000000000, 9999999999)}"

def create_test_users():
    groups = ["Admin", "Crew Controller", "Crew Member", "Caretaker", "Contractor"]
    genders = ["Male", "Female"]
    lobby_ids = [lobby.id for lobby in Lobby.objects.all()]
    designations = ["LP", "ALP", "SALP", "LPG", "SHT"]

    if not lobby_ids:
        raise ValueError("No lobbies available. Please add lobbies to the database first.")

    for group_name in groups:
        group = Group.objects.get(name=group_name)
        for i in range(3):
            username = f"{group_name.lower()}_testuser_{i+1}"
            email = f"{username}@example.com"
            mobile_number = random_phone()
            gender = choice(genders)
            lobby_id = choice(lobby_ids)
            lobby = Lobby.objects.get(id=lobby_id)

            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password="password123",
                mobile_number=mobile_number,
                gender=gender,
                LobbyAssigned=lobby,
                designation=choice(designations) if group_name == "Crew Member" else None,
            )
            user.groups.add(group)
            user.save()

            print(f"Created user: {username} ({group_name})")

if __name__ == "__main__":
    create_test_users()
