from django.core.management import BaseCommand, call_command
from django.db import transaction

from accounts.models import Docencia, Docente, User, WorkShedule


class Command(BaseCommand):
    help = "Apply migrations and create one Docente and one Docencia profile."

    def add_arguments(self, parser):
        parser.add_argument(
            "--skip-migrate",
            action="store_true",
            help="Do not run migrations before seeding profiles.",
        )

    def handle(self, *args, **options):
        if not options["skip_migrate"]:
            call_command("migrate")

        with transaction.atomic():
            docente_user, docente_user_created = User.objects.get_or_create(
                username="docente_demo",
                defaults={
                    "email": "docente_demo@example.com",
                    "first_name": "Perfil",
                    "last_name": "Docente",
                    "rut": "11111111-1",
                    "is_active": True,
                },
            )

            _, docente_profile_created = Docente.objects.get_or_create(
                user_id=docente_user,
                defaults={
                    "teaching_quota": 6,
                    "work_schedule": WorkShedule.FULL_TIME,
                },
            )

            docencia_user, docencia_user_created = User.objects.get_or_create(
                username="docencia_demo",
                defaults={
                    "email": "docencia_demo@example.com",
                    "first_name": "Perfil",
                    "last_name": "Docencia",
                    "rut": "22222222-2",
                    "is_active": True,
                },
            )

            _, docencia_profile_created = Docencia.objects.get_or_create(user_id=docencia_user)

        created_users = int(docente_user_created) + int(docencia_user_created)
        created_profiles = int(docente_profile_created) + int(docencia_profile_created)

        self.stdout.write(self.style.SUCCESS("Seed ejecutado correctamente."))
        self.stdout.write(
            f"Usuarios creados: {created_users}. Perfiles creados: {created_profiles}."
        )
