from django.db import models

class Modality(models.TextChoices):
    PRESENCIAL = 'Presencial', 'Presencial'
    ONLINE = 'Online', 'Online'
    HYBRID = 'Híbrido', 'Híbrido'
    SEMIPRESENCIAL = 'Semipresencial', 'Semipresencial'

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)
    credits = models.IntegerField(default=0)
    tags = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return f"{self.code} - {self.name}"

class AcademicPeriod(models.Model):
    name = models.CharField(max_length=50)
    term = models.CharField(max_length=20)
    year = models.IntegerField()
    def __str__(self):
        return f"{self.name} {self.term} {self.year}"
    
class CourseOffering(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='offerings')
    academic_period = models.ForeignKey(AcademicPeriod, on_delete=models.CASCADE, related_name='course_offerings')
    offering_comment = models.TextField(blank=True)
    type = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return f"{self.course.code} - {self.academic_period.name} {self.academic_period.term} {self.academic_period.year}"

class Section(models.Model):
    course_offering = models.ForeignKey(CourseOffering, on_delete=models.CASCADE, related_name='sections')
    section_number = models.IntegerField(default=1)
    mobility_quota = models.IntegerField(default=0)
    service_quota = models.IntegerField(default=0)
    control_count = models.IntegerField(default=0)
    has_exam = models.BooleanField(default=False)
    has_survey = models.BooleanField(default=False)
    quota = models.IntegerField(default=0)
    modality = models.CharField(max_length=20, choices=Modality.choices, default=Modality.PRESENCIAL)
    management_comment = models.TextField(blank=True)
    def __str__(self):
        return f"{self.course_offering.course.code} - {self.course_offering.academic_period.name} {self.course_offering.academic_period.term} {self.course_offering.academic_period.year} - Sección {self.section_number}"

class ClassType(models.TextChoices):
    CATEDRA = 'Cátedra', 'Cátedra'
    LABORATORIO = 'Laboratorio', 'Laboratorio'
    AUXILIAR = 'Auxiliar', 'Auxiliar'

class Schedule(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='schedules')
    block = models.CharField(max_length=20)
    type = models.CharField(max_length=20, choices=ClassType.choices, default=ClassType.CATEDRA)
    classroom = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return f"{self.section} - {self.block}"