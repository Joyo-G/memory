import re

def get_code_regex(course_str: str) -> str:
    """
    Generates a regex pattern to match the course code followed by digits and optional uppercase alphanumeric characters.
    """
    match = rf"(?<![a-zA-Z]){re.escape(course_str)}\d[A-Z0-9]*"
    return match