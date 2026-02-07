import csv

print("Species Population Analysis\n")

with open("species_data.csv", "r") as file:
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
        elif average < 200:
            status = "Vulnerable"
        else:
            status = "Least Concern"

        print(f"Species: {species}")
        print(f"  Total Population: {total}")
        print(f"  Average Population: {average}")
        print(f"  Conservation Status: {status}\n")
