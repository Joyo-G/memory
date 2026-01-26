import pandas as pd
from .config.paths import DATA_DIR
from .core.catalog import CoursesCatalog
from .services.data_processor import filter_course_code, normalize_course_xlsx
from .services.calendar_service import generate_new_calendar_xlsx
from .utils.formatters import get_approval_data

def run_pipeline():
    # 1. Load & Process
    raw_df = pd.read_excel(DATA_DIR / "d02.xls", engine="calamine")
    clean_df = normalize_course_xlsx(filter_course_code("CC", raw_df))
    
    # 2. Build Catalog
    catalog = CoursesCatalog(code="CC")
    catalog.build_catalog(clean_df)
    
    # 3. Handle Metrics
    metrics_df = pd.read_excel(DATA_DIR / "d03.xls", engine="calamine")
    approval_data = get_approval_data(filter_course_code("CC", metrics_df))
    
    # 4. Export
    generate_new_calendar_xlsx(approval_data, catalog)

def main():
    try:
        run_pipeline()
        print("Success")
    except Exception as e:
        print(f"Error: {e}")
