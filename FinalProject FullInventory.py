# 2316411
# Seohee Han

from collections import defaultdict

# Create dictionary
data = defaultdict(dict)

# Clean up the first file
with open('ManufacturerList.csv', 'r') as ML: # load file
    for line in ML:
        fields = line.strip().split(',') # Organize each line
        item_id = fields[0] 
        manufacturer = fields[1]  
        item_type = fields[2]  
        damaged = fields[3]  
        data[item_id] = {'Manufacturer': manufacturer, 'Item Type': item_type, 'Damaged': damaged}

# Clean up the second file
with open('PriceList.csv', 'r') as PL: # load file
    for line in PL:
        fields = line.strip().split(',') # Organize each line
        item_id = fields[0] 
        price = fields[1]  
        data[item_id]['Price'] = price

# Clean up the third file
with open('ServiceDatesList.csv', 'r') as SL: # load file
    for line in SL:
        fields = line.strip().split(',') # Organize each line
        item_id = fields[0]  
        service_date = fields[1]  
        data[item_id]['Service Date'] = service_date

# Sort alphabetically by manufacturer name
sorted_data = sorted(data.items(), key=lambda x: x[1]['Manufacturer'])

# print
for item_id, details in sorted_data:
    print(f"{item_id}, {details['Manufacturer']}, {details['Item Type']}, {details['Price']}, {details['Service Date']}, {details['Damaged']}")


