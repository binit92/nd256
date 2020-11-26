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
    called_area_codes = []
    total_fixed_lines_counter = 0
    for entry in calls:

        calling_number = entry[0]
        called_number = entry[1]
        # only for people in Banglore
        if(calling_number.startswith("(080)")):

            if(called_number.startswith("(0")):
                telephone_code = called_number[1:called_number.find(")")]
                called_area_codes.append(telephone_code)
                total_fixed_lines_counter +=1
            elif(called_number.startswith("7") or called_number.startswith("8") or called_number.startswith("9")):
                called_area_codes.append(called_number[:4])
            elif(called_number.startswith("140")):
                called_area_codes.append("140")

    # Part A: area code list in lexicographic order
    area_codes_list = sorted(list(set(called_area_codes)))
    print("The numbers called by people in Bangalore have codes: " )
    for val in area_codes_list:
        print(val)

    # Part B: percentage of calls to fixed line number from Bengaluru
    percentage = total_fixed_lines_counter/len(called_area_codes)
    print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage))
"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
