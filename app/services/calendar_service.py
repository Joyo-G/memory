import pandas as pd
import re
from app.core.catalog import CoursesCatalog

def generate_new_calendar_xlsx(approval_data: dict, catalog: CoursesCatalog, output_path: str = "new_calendar.xlsx"):
    """
    Generates an Excel file with adjusted quotas based on approval percentages.
    
    Args:
        approval_data (dict): Hierarchical dictionary with approval percentages per course code.
        catalog (CoursesCatalog): Catalog instance containing course and section information.
        output_path (str): Path where the .xlsx file will be saved.
    """
    rows = []
    
    for code, course in catalog.courses.items():
        # Skip if course is not in approval data
        if code not in approval_data:
            continue

        # Get historical percentage from the data
        info = approval_data.get(code, {})
        percentage_str = info.get("historical_average", "0%")
        
        # Clean and convert percentage to float (e.g., "80%" -> 0.8)
        try:
            # Remove everything that is not a digit or a dot
            numeric_part = re.sub(r'[^0-9.]', '', percentage_str)
            approval_rate = float(numeric_part) / 100 if numeric_part else 0.0
        except (ValueError, TypeError):
            approval_rate = 0.0
            
        # Sum occupied seats from all course sections
        total_occupied = sum(section.occupied for section in course.sections.values())
        
        # Calculate new quotas: (occupied * approval_rate)
        # Round to the nearest integer
        new_quotas = int(total_occupied * approval_rate)
        
        # Collect unique teachers from all sections
        unique_teachers = set()
        for section in course.sections.values():
            if section.teachers and section.teachers.lower() != 'nan':
                # Assume teachers might be separated by commas or similar
                for p in re.split(r'[,;/]', section.teachers):
                    teacher_name = p.strip()
                    if teacher_name:
                        unique_teachers.add(teacher_name)
        
        teachers_str = ", ".join(sorted(list(unique_teachers)))
        
        rows.append({
            "Code": code,
            "Course Name": course.name,
            "Teachers": teachers_str,
            "Quotas": new_quotas
        })
        
    df_result = pd.DataFrame(rows)
    df_result.to_excel(output_path, index=False)
    print(f"File successfully generated at: {output_path}")

    return df_result
