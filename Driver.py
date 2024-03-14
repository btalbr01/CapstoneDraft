#This file calls the other python files to run their scrapers and export .csv files
import subprocess
import MySQLdb
import csv
import mysql.connector

host = 'localhost'
user = 'root'
password = 'ansgtyze'

schema_name = 'properties'

conn = mysql.connector.connect(host=host, user=user, password=password)

cursor = conn.cursor()

create_schema_query = f'CREATE DATABASE IF NOT EXISTS {schema_name}'

cursor.execute(create_schema_query)

conn.commit()

cursor.close()
conn.close()

subprocess.run(["python","zillow.py"])
subprocess.run(["python","zillow_land.py"])
subprocess.run(["python","realtor.py"])
subprocess.run(["python","realtor_land.py"])

subprocess.Popen("D:\Dbeaver\dbeaver.exe")