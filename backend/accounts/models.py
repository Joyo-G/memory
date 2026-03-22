from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    rut = models.CharField(max_length=12, unique=True)
    is_active = models.BooleanField(default=True)

class WorkShedule(models.TextChoices):
    FULL_TIME = 'FT', 'Full Time'
    PART_TIME = 'PT', 'Part Time'

class Docente(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name='docente_user')
    teaching_quota = models.IntegerField(default=0)
    work_schedule = models.CharField(max_length=2, choices=WorkShedule.choices, default=WorkShedule.FULL_TIME)

class Docencia(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name='docencia_user')

