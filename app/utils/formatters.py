import pandas as pd
import re

def get_approval_data(df: pd.DataFrame) -> dict:
    """
    Processes a DataFrame with course information and returns a hierarchical dictionary.
    
    Expected DataFrame columns:
    1. "Course": String containing code and name (e.g., "CC3001 Algorithms")
    2. Middle columns: Semesters (e.g., "2023 Fall", "2023 Spring")
    3. Last column: "Historical Average"
    """
    result = {}
    
    for _, row in df.iterrows():
        # Extract code and name from the "Course" column
        course_text = str(row.iloc[0])
        match = re.search(r'^(\w+)\s+(.*)$', course_text)
        if match:
            code = match.group(1)
            name = match.group(2)
        else:
            code = course_text
            name = course_text
            
        # The historical average is the last column
        historical_average = str(row.iloc[-1])
        
        # The semester columns are all the intermediate ones
        # Structure: "2023 Fall" -> { "2023": { "Fall": "..." } }
        hierarchical_percentages = {}
        for col in df.columns[1:-1]:
            val = row[col]
            if pd.notna(val):
                # Try to separate year from semester (e.g., "2023 Fall")
                col_match = re.search(r'^(\d{4})\s+(.*)$', col)
                if col_match:
                    year = col_match.group(1)
                    semester = col_match.group(2)
                    if year not in hierarchical_percentages:
                        hierarchical_percentages[year] = {}
                    hierarchical_percentages[year][semester] = str(val)
                else:
                    # Fallback if the column name doesn't follow the expected pattern
                    hierarchical_percentages[col] = str(val)
        
        result[code] = {
            "name": name,
            "historical_average": historical_average,
            "percentages": hierarchical_percentages
        }
        
    return result