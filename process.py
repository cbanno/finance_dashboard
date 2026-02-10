import csv
import json

def data_converter() :
    summary = {} #dictionary to store totals
    transactions = [] #list to store every row from the table

    with open("spending.csv", mode="r") as file: #open file in "read" mode

        reader = csv.DictReader(file) #turns each row into dictionary using first row as the "key"

        for row in reader: #for-loop to go through every line 

            transactions.append(row)