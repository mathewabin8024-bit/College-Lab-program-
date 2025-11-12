import csv
# Define the header (field names) for the CSV file
field_name = ['No', 'Company', 'Car Model']
# Create a list of dictionaries, each representing a row
car = [
 {'No': 1, 'Company': 'Ferrari', 'Car Model': 'GH'},
 {'No': 2, 'Company': 'BMW', 'Car Model': 'X5'},
 {'No': 3, 'Company': 'Maruti Suzuki', 'Car Model': 'Swift'},
 {'No': 4, 'Company': 'Audi', 'Car Model': 'RS7'},
 {'No': 5, 'Company': 'Toyota', 'Car Model': 'Fortuner'}
]
# ------------------ Writing to the CSV file ------------------
with open('car.csv', 'w', newline='') as csvfile:
 write = csv.DictWriter(csvfile, fieldnames=field_name) # Create DictWriter 
object
 write.writeheader() # Write header row
 write.writerows(car) # Write multiple rows from list of dictionaries


with open('car.csv', newline='') as csvfile:
 d = csv.reader(csvfile) # Create a CSV reader object
 for r in d: # Iterate through each row in the CSV file
 print(','.join(r)) # Join each element in row with commas and print
 print(r)