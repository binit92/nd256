"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

telemarketers = set()
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    caller_list = set()
    receiver_list = set()

    for entry in calls:
        caller_list.add(entry[0])
        receiver_list.add(entry[1])

    # remove all the numbers who have received the call.
    telemarketers = caller_list.difference(receiver_list)

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    text_sender_list = set()
    text_receiver_list = set()
    for entry in texts:
        text_sender_list.add(entry[0])
        text_receiver_list.add(entry[1])

    # Remove all the texters
    telemarketers = telemarketers.difference(text_sender_list)
    # Remove all the textee, although it is zero, I am still adding it as per rubric requirement.
    telemarketers = telemarketers.difference(text_receiver_list)


print(" These numbers could be telemarketers: ")
for val in sorted(list(telemarketers)):
    print(val)


"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
