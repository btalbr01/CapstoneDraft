#This file calls the other python files to run their scrapers and export .csv files
import subprocess

subprocess.run(["python","zillow.py"])
subprocess.run(["python","zillow_land.py"])
subprocess.run(["python","realtor.py"])
subprocess.run(["python","realtor_land.py"])
