import matplotlib.pyplot as plt
import csv

file_name = "extinction_data.csv"

data = {}

with open(file_name, newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        species = row["Species"]
        year = row["Year"]
        population = int(row["Population"])
      
        if species not in data:
            data[species] = {}

        data[species][year] = population

species_list = []
decline_percent_list = []
print("\nSpecies Extinction Risk Analysis\n")

for species, years in data.items():
    if "2015" in years and "2025" in years:
        old_pop = years["2015"]
        new_pop = years["2025"]

        decline = old_pop - new_pop
        decline_percent = (decline / old_pop) * 100

        species_list.append(species)
        decline_percent_list.append(decline_percent)

        print(f"Species: {species}")
        print(f"  Population change: -{decline}")
        print(f"  Decline percentage: {decline_percent:.2f}%")

        if decline_percent < 10:
            status = "Stable"
        elif decline_percent < 30:
            status = "Vulnerable"
        else:
            status = "Endangered"

        print(f"  Risk status: {status}\n")
plt.figure()
plt.bar(species_list, decline_percent_list)
plt.xlabel("Species")
plt.ylabel("Population Decline (%)")
plt.title("Species Extinction Risk Based on Population Decline")
plt.show()
plt.figure()
plt.pie(
    decline_percent_list,
    labels=species_list,
    autopct='%1.1f%%',
    startangle=90
)
plt.title("Proportion of Population Decline by Species")
plt.show()
