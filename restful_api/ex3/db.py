import pyodbc


cnx = pyodbc.connect(Trusted_Connection='yes',
                     Driver='{ODBC Driver 17 for SQL Server}',
                     Server='DESKTOP-09AHFD3',
                     Database='sale_manage')
cursor = cnx.cursor()