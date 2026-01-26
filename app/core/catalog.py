import pandas as pd
import re
from typing import Dict, Optional

from app.utils.helpers import get_code_regex

from .models import CourseInfo



class CoursesCatalog:
    """
    CoursesCatalog dataclass to hold multiple CourseInfo instances
    by their course codes.

    Attributes:
        __courses (Dict[str, CourseInfo]): A dictionary mapping course codes to CourseInfo instances.
        __code (str): The code used for filtering courses.
    """
    
    def __init__(self, code: str = ""):
        self.__courses: Dict[str, CourseInfo] = {}
        self.__code = code

    def _extract_course_column_data(self, course_info:str) -> Dict[str, str|int]:
        """
        Extract course code, name, and section from a course information string.
        """
        course_code = ""
        course_name = ""
        course_section = ""

        # Extract entire course code using regex
        # Build a regex that matches the full word starting from the code
        # e.g. if self._code == "CC" we want to match "CC123" or "CC-ABC" (word chars after the code)
        # Extract entire course code using regex with strict constraints:
        # 1. No letter before the code
        # 2. Exact match with self._code (case-sensitive)
        # 3. Next character after self._code must be a digit
        # 4. Extract the full sequence (digits and letters following)
        pattern = get_code_regex(self.__code)
        # Case-sensitive search: self._code is expected to be defined and uppercase-sensitive
        match = re.search(pattern, course_info)
        if match:
            course_code = match.group(0)

        # Extract course name only if we found a course_code
        if course_code:
            # Capture the course name that follows the code up to the word 'Sección' or end of string.
            # Accept an optional separator (dash or similar) or just whitespace between code and name.
            name_pattern = rf"{re.escape(course_code)}\s*[-–—]?\s*(.*?)(?:\bSecci[oó]n\b|$)"
            name_match = re.search(name_pattern, course_info, flags=re.IGNORECASE | re.DOTALL)
            if name_match:
                course_name = name_match.group(1).strip()
                # Normalize excessive internal spacing
                course_name = re.sub(r"\s{2,}", " ", course_name)
                
        # Extract section number anywhere in the string (e.g. "Sección 3", "Sección:3", "Sección-3")
        sec_pattern = r"Secci[oó]n\s*[:\-]?\s*(\d+)"
        sec_match = re.search(sec_pattern, course_info, flags=re.IGNORECASE)
        if sec_match:
            course_section = sec_match.group(1)

        return {"course_code": course_code, "course_name": course_name, "course_section": course_section}



    def build_catalog(self, data: pd.DataFrame) -> None:
        """
        Build the course catalog from a DataFrame.
        Args:
            data (pd.DataFrame): DataFrame containing course data.
        """
        for _, row in data.iterrows():
            course = str(row["Curso"])
            teacher = str(row["Profesor"])
            quota = int(row["Cupos"])
            occupied = int(row["Ocupados"])
            vacancies = int(row["Vacantes"])

            extracted = self._extract_course_column_data(course)

            self.add_course_section(
                code=extracted["course_code"],
                name=extracted["course_name"],
                section=extracted["course_section"],
                teachers=teacher,
                quota=quota,
                occupied=occupied,
                vacancies=vacancies,
            )

    def build_metrics(self, data: pd.DataFrame) -> None:
        pass

    def add_course_section(
        self,
        code: str,
        name: str,
        section: str,
        teachers: str,
        quota: int,
        occupied: int,
        vacancies: int,
    ) -> None:
        """
        Add a section to a course in the catalog.
        Args:
            code (str): Course code.
            name (str): Course name.
            section (str): Section identifier.
            teachers (str): Teachers for the section.
            quota (int): Quota for the section.
            occupied (int): Occupied seats in the section.
            vacancies (int): Vacancies in the section.
        """
        if code not in self.__courses:
            self.__courses[code] = CourseInfo(code=code, name=name)
        
        self.__courses[code].add_section(
            section=section,
            teachers=teachers,
            quota=quota,
            occupied=occupied,
            vacancies=vacancies,
        )
    
    @property
    def courses(self) -> Dict[str, CourseInfo]:
        """
        Returns the dictionary of courses in the catalog.
        """
        return self.__courses

    def find_course(self, code: str) -> Optional[CourseInfo]:
        return self.__courses.get(code)
    
    def __str__(self):
        return f"CoursesCatalog(courses={list(self.__courses.keys())})"