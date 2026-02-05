
import csv
import os

print("Species Population Analysis\n")

# Get the absolute path to the CSV file relative to this script
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "species_data.csv")

with open(csv_path, "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        species = row["Species"]
        site1 = int(row["Site1"])
        site2 = int(row["Site2"])
        site3 = int(row["Site3"])

        total = site1 + site2 + site3
        average = round(total / 3, 2)

        if average < 50:
            status = "Endangered"
            trend= "Declining"
        elif average < 200:
            status = "Vulnerable"
            trend= "Stable"
        else:
            status = "Least Concern"
            trend= "Least Concerning"

        print(f"Species: {species}")
        print(f"  Total Population: {total}")
        print(f"  Average Population: {average}")
        print(f"  Conservation Status: {status}")
        print(f"  Population Trend: {trend}\n")
        