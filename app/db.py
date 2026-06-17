import pyodbc

def get_connection():
    return pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        r"Server=localhost\SQLEXPRESS;"
        "Database=JobMarketAnalyzer;"
        "Trusted_Connection=yes;"
    )