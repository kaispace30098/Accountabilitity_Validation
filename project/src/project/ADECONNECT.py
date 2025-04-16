from project.database import fetch_student_data
from project.calculation import calcuate_average
from project.source import FiscalYear
import pyodbc
import pandas as pd
fy=FiscalYear
def generate_summary():
    
    data=fetch_student_data(fiscalyear=fy)
    avg = calcuate_average(data)
    return avg