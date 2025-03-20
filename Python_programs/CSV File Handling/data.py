import csv

# with open("/home/vignesh/VS/GitHub/Python/Python_programs/CSV/sample.csv","r") as file:
#     reader = csv.reader(file)
#     for n in reader:
#         print(reader)

with open("/home/vignesh/VS/GitHub/Python/Python_programs/CSV/sample.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['Name']} is {row['Age']} years old and lives in {row['City']} ")