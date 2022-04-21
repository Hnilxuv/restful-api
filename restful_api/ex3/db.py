import pyodbc

conx_string = "driver={SQL Server Native Client 11.0}; server=hnilxuv; database=ex3; trusted_connection=YES;"

cnx = pyodbc.connect(conx_string)
cursor = cnx.cursor()
