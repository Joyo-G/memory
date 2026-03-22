from django.db import models
class Modality(models.TextChoices):
    PRESENCIAL = 'Presencial', 'Presencial'
    REMOTO = 'Remoto', 'Remoto'
    HIBRIDO = 'Híbrido', 'Híbrido'
    SEMIPRESENCIAL = 'Semipresencial', 'Semipresencial'

class Preference(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='preferences')
    course_offering = "pass"
    modality = models.CharField(max_length=20, choices=Modality.choices)
    priority = models.IntegerField()