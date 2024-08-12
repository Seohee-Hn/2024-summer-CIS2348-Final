# 2316411
# Seohee Han

import csv
from datetime import datetime

def find_past_service_dates(file_list):
    found = []
    current_date = datetime.now()

    for filename in file_list:
        with open(filename, 'r') as file:
            content = csv.reader(file)

            for line in content:
                if 'ServiceDatesList' in filename:
                    try:
                        service_date = datetime.strptime(line[1], '%m-%d-%y')
                        if service_date < current_date:
                            found.append(line)
                    except ValueError:
                        continue 

    result = ''
    for item in found:
        result += ', '.join(item) + '\n'
    
    return result if found else "No past service dates."

# file from which to derive results
files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']

# print
result = find_past_service_dates(files)
print(result)

