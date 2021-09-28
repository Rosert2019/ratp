#!/usr/bin/env python

"""
    Script to import data from .csv file to Model Database DJango
    To execute this script run: 
                                1) python manage.py shell
                                2) exec(open('csv_import_data.py').read())
"""

import csv
from gares.models import Station

CSV_PATH = './data/exports-des-gares-idf.csv'      # Csv file path  


with open(CSV_PATH, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        #row[0], row[6], row[26]
        if row[26] != 'ligne':
            print(row[0], row[6], row[26])
            Station.objects.create(name=row[6], line=row[26], geo_location=row[0])
