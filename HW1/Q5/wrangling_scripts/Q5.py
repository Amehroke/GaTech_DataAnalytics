"""
cse6242 s23
Q5.py - utilities to supply data to the templates.

This file contains a pair of functions for retrieving and manipulating data
that will be supplied to the template for generating the table. """
import csv

def username():
    return 'Amehroke3'

def data_wrangling():
    with open('data/movies.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        table = list()
        # Feel free to add any additional variables
        table_100 = list()
        ...
        
        # Read in the header
        for header in reader:
            break
        
        # Read in each row
        for row in reader:
            table.append(row)
            
            if len(table) <= 100:
                table_100.append(row)
        
        
        
        # Order table by the last column - [3 points] Q5.4.b
        table_100.sort(key=lambda x: float(x[-1]), reverse=True)
        ...
    
    return header, table_100

