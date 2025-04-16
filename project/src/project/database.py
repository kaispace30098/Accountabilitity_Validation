import pyodbc
import pandas as pd
import numpy as np

def fetch_student_data(fiscalyear):
    cnxn_str = (
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=AACTASTPDDBVM02;"
        "Trusted_Connection=yes;"
    )
    sql=f"""
    SELECT Performance
    FROM AccountabilityArchive.static.FinalStaticFile2024 
    WHERE SchoolCode = 79445 and Subject='ELA' and Fiscalyear={fiscalyear}
    """
    cnxn=pyodbc.connect(cnxn_str)
    df = pd.read_sql_query(sql, cnxn)
    data=np.array(df['Performance'])
    return data