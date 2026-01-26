# Memoria

A data processing and planning tool for the Department of Computer Science (DCC).

## Overview

**Memoria** is a Python application designed to automate the management and analysis of academic data. Its primary goal is to assist academic coordinators in planning course capacities (quotas) for upcoming semesters by analyzing historical student performance and current enrollment trends.

The application processes raw Excel spreadsheets, normalizes inconsistent data formats, and applies metric-driven formulas to suggest optimized enrollment limits for each course.

## Key Features

- **Data Processing**: Filters and normalizes complex Excel files, handling inconsistent formatting and column shifts.
- **Catalog Management**: Builds a structured internal catalog of courses, sections, and faculty.
- **Quota Calculation**: Predicts required course capacities by combining current occupancy with historical approval rates.
- **Automated Reporting**: Generates consolidated Excel reports ready for academic administrative review.

## Data Sources

The project processes the following data sources:

- **Student Enrollment (d01)**: Historical data of students entering the DCC per year, categorized by program, year, and gender.
- **Course Catalog (d02)**: Detailed information about courses, including:
    - Course Name and Code (CCXXXX).
    - Faculty/Professors.
    - Quotas, Occupancy, and Vacancies.
    - Section-specific breakdowns.
- **Approval Metrics (d03)**: Historical approval percentages per course and year, used to forecast student flow and future demand.

## Project Structure

- `app/core/`: Core logic for the course catalog and data models.
- `app/services/`: Implementation of data processing, metric analysis, and report generation.
- `app/utils/`: Formatting and helper utilities for data manipulation.
- `data/`: Directory for input Excel files.
- `processed_data/`: Directory for intermediate and final output files.

## Getting Started

### Prerequisites

- Python 3.13 or higher
- [Poetry](https://python-poetry.org/docs/#installation) (recommended)

### Installation

1. Clone the repository.
2. Install the dependencies using Poetry:
   ```bash
   poetry install
   ```

### Running the Application

1. Ensure the input files (`d02.xls`, `d03.xls`) are located in the `data/` directory.
2. Execute the processing pipeline:
   ```bash
   poetry run python -m app
   ```

The application will process the data and generate a `new_calendar.xlsx` file in the project root with the optimized course quotas.
