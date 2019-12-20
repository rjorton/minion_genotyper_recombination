# read in strain codes
# convert to uppercase
# create code that can be pasted in
import csv

filename = "/Users/richardorton/Downloads/depositedSequences_codes.txt"
strain_dict = {}
row_count = 0

print("strain_codes = {", end='')

with open(filename) as file_handler:
    reader = csv.reader(file_handler, delimiter='\t')

    for row in reader:
        row_count += 1

        if(row_count > 1):
            print(",\n\t\t\t\t", end='')

        print("\"" + row[0].upper() + "\": \"" + row[1].upper() + "\"", end='')
        strain_dict[row[0]] = row[1]

print("}\n", end='')

print("Dictionary length = " + str(len(strain_dict)))
print("Row count = " + str(row_count))

if row_count != len(strain_dict):
    print("Error - possible duplicate in dictionary as lengths not the same")