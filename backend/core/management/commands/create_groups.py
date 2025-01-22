# from django.core.management.base import BaseCommand
# from django.contrib.auth.models import Group, Permission
# from core.models import Zone, Division, Lobby

# class Command(BaseCommand):
#     help = 'Create default groups and permissions'

#     def handle(self, *args, **kwargs):
#         # Define groups and their permissions
#         groups_permissions = {
#             'Admin': Permission.objects.all(),
#             'Crew Controller': ['view_lobby', 'view_division', 'view_zone'],
#             'Crew Member': ['view_lobby', 'add_feedback', 'view_own_foodtoken'],
#             'Caretaker': ['view_lobby', 'view_bed', 'view_feedback'],
#             'Contractor': ['view_bed', 'view_foodtoken', 'view_feedback'],
#         }

#         for group_name, permissions in groups_permissions.items():
#             group, created = Group.objects.get_or_create(name=group_name)
#             if created:
#                 self.stdout.write(f'Group "{group_name}" created.')
#             else:
#                 self.stdout.write(f'Group "{group_name}" already exists.')

#             # Assign permissions to the group
#             for perm_codename in permissions:
#                 try:
#                     perm = Permission.objects.get(codename=perm_codename)
#                     group.permissions.add(perm)
#                 except Permission.DoesNotExist:
#                     self.stdout.write(f'Permission "{perm_codename}" not found.')
#         self.stdout.write("Groups and permissions are successfully set up.")

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Create default user groups'

    def handle(self, *args, **kwargs):
        # Define the default groups
        groups = ['Admin', 'Crew Controller', 'Crew Member', 'Caretaker', 'Contractor']

        for group_name in groups:
            group, created = Group.objects.get_or_create(name=group_name)
            if created:
                self.stdout.write(f'Group "{group_name}" created.')
            else:
                self.stdout.write(f'Group "{group_name}" already exists.')

        self.stdout.write("Default groups created successfully. You can assign permissions from the admin panel.")
