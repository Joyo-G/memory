from .models import Course, AcademicPeriod, CourseOffering, Section, Schedule
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['code', 'name', 'description', 'credits', 'tags']

class AcademicPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicPeriod
        fields = ['name', 'term', 'year']

class CourseOfferingSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    academic_period = AcademicPeriodSerializer(read_only=True)

    class Meta:
        model = CourseOffering
        fields = ['course', 'academic_period', 'offering_comment', 'type']

class SectionSerializer(serializers.ModelSerializer):
    course_offering = CourseOfferingSerializer(read_only=True)

    class Meta:
        model = Section
        fields = ['course_offering', 'section_number', 'mobility_quota', 'service_quota', 'control_count', 'has_exam', 'has_survey', 'quota', 'modality', 'management_comment']

class ScheduleSerializer(serializers.ModelSerializer):
    section = SectionSerializer(read_only=True)

    class Meta:
        model = Schedule
        fields = ['section', 'block', 'type', 'classroom']