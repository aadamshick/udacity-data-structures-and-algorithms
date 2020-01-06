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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

firstRecord = texts[0]
lastRecord = calls[len(calls)-1]

print("First record of texts, " + firstRecord[0] + " texts " + firstRecord[1] + " at time " + firstRecord[2])
print("Last record of calls, " + lastRecord[0] + " calls " + lastRecord[1] + " at time " + lastRecord[2] + ", lasting " + lastRecord[3] + " seconds")