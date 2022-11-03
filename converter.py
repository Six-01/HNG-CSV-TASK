import json
import csv
import hashlib

#Reading the NFT.csv file
with open ("NFT Naming csv - All Teams.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    data = []
    for row in reader:
        data.append({"SerialNumber":row[0], "FileName":row[1], "UUID":row[2]})

#Converting the NFT.csv file to JSON
with open ("NFT Naming.json", "w") as f:
    json.dump(data, f, indent=3)

#Hashing and appending each JSON data in the JSON data file 
with open ("NFT Naming.json") as f:
    list = json.load(f)
    for data in list:
        data_2 = f"{data}"
        hashed = hashlib.sha256(data_2.encode()).hexdigest()
        data.update({"Hash":hashed})
    list.append({"Hash":hashed})

#Dumping the Hashed JSON data to a new JSON file
with open ("Hashed NFT Naming.json", "w") as f:
    json.dump(list, f, indent=3)

#Reading the Hashed JSON data file
with open("Hashed NFT Naming.json", "r") as f:
    name = json.load(f)

#Convertung the Hashed JSON data file back to csv format (filename.output.csv)
with open ("NFT Naming csv - All Teams.output.csv", "w", newline="") as f:
    fieldnames = name[0].keys()
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for names in name:
        writer.writerow(names)

    