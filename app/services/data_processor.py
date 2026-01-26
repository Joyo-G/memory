import pandas as pd
from app.utils.helpers import get_code_regex
from app.config.paths import PROCESSED_DATA_DIR

def filter_course_code(code: str, file: pd.DataFrame) -> pd.DataFrame:

    pattern = get_code_regex(code)

    filtered_df = file[file.iloc[:, 0].astype(str).str.contains(pattern, na=False)] 

    output_path = PROCESSED_DATA_DIR / f"{code}_filtered.xlsx"
    filtered_df.to_excel(output_path, index=False)

    return filtered_df

def normalize_course_xlsx(df: pd.DataFrame)-> pd.DataFrame:
    
    col_idx = 3
    print("shift data in column index", col_idx)

    n_cols = df.shape[1]
    # Iterate rows and shift row-wise from col_idx to the right by one
    for row_idx in range(len(df)):
        value = df.iat[row_idx, col_idx]
        # Shift when there is any non-missing value in the target column
        if not pd.isna(value):
            print(f"shifting row {row_idx} value {value} to the right starting at col {col_idx}")
            # Shift values to the right, iterating columns backwards to avoid overwrite
            for c in range(n_cols - 1, col_idx, -1):
                df.iat[row_idx, c] = df.iat[row_idx, c - 1]
            # Clear original position
            df.iat[row_idx, col_idx] = pd.NA

    # Delete columns 4, 6, 8
    cols_to_delete = [3, 5, 7]
    df.drop(df.columns[cols_to_delete], axis=1, inplace=True)

    # Save the modified DataFrame to a new Excel file to avoid overwriting
    output_path = PROCESSED_DATA_DIR / "CC_Final.xlsx"
    try:
        df.to_excel(output_path, index=False)
        print(f"Saved shifted DataFrame to {output_path}")
    except Exception as e:
        print(f"Error saving shifted DataFrame: {e}")
    return df
