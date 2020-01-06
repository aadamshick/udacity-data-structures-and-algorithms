"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

# create a list of all phone numbers

list = []

for i in texts:
    list.append(i[0])
    list.append(i[1])

for i in calls:
    list.append(i[0])
    list.append(i[1])

# dedupe the list

length = len(set(list))

print("There are " + str(length) + " different telephone numbers in the records.")