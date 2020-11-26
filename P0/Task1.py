"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

records = set()
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for entry in texts:
        records.add(entry[0])  # sending number
        records.add(entry[1])  # receiving number

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for entry in calls:
        records.add(entry[0])  # calling number
        records.add(entry[1])  # receiving number

print("There are {} different telephone numbers in the records.".format(len(records)))
"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
