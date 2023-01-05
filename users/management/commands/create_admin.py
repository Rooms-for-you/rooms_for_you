from users.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create admin users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--username",
            type=str,
        )
        parser.add_argument(
            "--password",
            type=str,
        )
        parser.add_argument(
            "--email",
            type=str,
        )

    def handle(self, *args, **kwargs):
        username = kwargs.get("username") or "admin"
        password = kwargs.get("password") or "admin1234"
        email = kwargs.get("email") or "admin@roomsforyou.com"

        user_username = User.objects.filter(username=username).exists()
        if user_username:
            raise CommandError(f"Username `{username}` already taken.")

        user_email = User.objects.filter(email=email).exists()
        if user_email:
            raise CommandError(f"Email `{email}` already taken.")

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )

        self.stdout.write(
            self.style.SUCCESS("Admin `admin` successfully created!"),
        )
