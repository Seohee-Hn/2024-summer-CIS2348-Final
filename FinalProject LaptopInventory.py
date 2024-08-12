# 2316411
# Seohee Han

import csv

def find_laptop(file_list, keyword):
    found = []
 
# read the contents of each file
    for filename in file_list:
        with open(filename, 'r') as file: 
            content = csv.reader(file)

            for line in content: # convert row to string
                if isinstance(keyword, str):
                    if keyword in ', '.join(line): # check if word exists
                        found.append(line)
                else:
                    if len(set(keyword) & set(line)) == len(keyword):
                        found.append(line)

    result = ''
    for item in found:
        result += ', '.join(item) + '\n'
    
    return result if found else f"'{keyword}' doesn't exist in any files"


files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv'] # list files to search for words
search_term = 'laptop'

# print
result = find_laptop(files, search_term)
print(result)


