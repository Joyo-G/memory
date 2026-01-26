from dataclasses import dataclass
from typing import Dict, Optional
import pandas as pd

@dataclass
class SectionInfo:
    """
    SectionInfo dataclass to hold section details.
    Attributes:
        section (str): The section identifier.
        teachers (str): The teachers for the section.
        quota (int): The quota for the section.
        occupied (int): The number of occupied seats.
        vacancies (int): The number of vacancies.
    """
    section: str
    teachers: str
    quota: int
    occupied: int
    vacancies: int

class CourseInfo:
    """
    CourseInfo dataclass to hold course details and its sections.
    Attributes:
        _name (str): The name of the course.
        _code (str): The code of the course.
        _sections (Dict[str, SectionInfo]): A dictionary mapping section identifiers to SectionInfo instances.
    """
    def __init__(self, name, code):
        self.__name = name
        self.__code = code
        self.__sections: Dict[str, SectionInfo] = {}
    
    def add_section(self, section: str, teachers: str, quota: int, occupied: int, vacancies: int):
        self.__sections[str(section)] = SectionInfo(
            section=str(section),
            teachers=str(teachers),
            quota=int(quota),
            occupied=int(occupied),
            vacancies=int(vacancies),
        )
    def section(self, section: str) -> Optional[SectionInfo]:
        return self.__sections.get(str(section))
    
    @property
    def sections(self) -> Dict[str, SectionInfo]:
        return self.__sections
    @property
    def name(self) -> str:
        return self.__name
    @property
    def code(self) -> str:
        return self.__code
    
    def __str__(self):
        return f"CourseInfo(code={self.__code}, name={self.__name}, sections={list(self.__sections.keys())})"
    

@dataclass
class Metrics:
    """
    Metrics dataclass to hold course metrics details.
    Attributes:
        course_code (str): The code of the course.
        total_sections (int): The total number of sections.
        total_quota (int): The total quota for the course.
        total_occupied (int): The total number of occupied seats.
        total_vacancies (int): The total number of vacancies.
    """
    approval_percentage: float
    total_quota: int
    total_occupied: int
    total_vacancies: int

class CourseMetrics:
    def __init__(self, course_info):
        self.course_info = course_info
        self.__course_metrics = self.calculate_metrics()

    def calculate_metrics(self) -> Metrics:
        total_quota = sum(section.quota for section in self.course_info.sections.values())
        total_occupied = sum(section.occupied for section in self.course_info.sections.values())
        total_vacancies = sum(section.vacancies for section in self.course_info.sections.values())
        
        approval_percentage = (total_occupied / total_quota * 100) if total_quota > 0 else 0.0
        
        return Metrics(
            approval_percentage=approval_percentage,
            total_quota=total_quota,
            total_occupied=total_occupied,
            total_vacancies=total_vacancies
        )

class CoursesMetrics:
    pass