import csv

file_name = "population_data.csv"

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
print("\nSpecies Population Change Analysis\n")

for species, years in data.items():
    if "2020" in years and "2021" in years:
        pop_2020 = years["2020"]
        pop_2021 = years["2021"]

        change = pop_2021 - pop_2020
        percent_change = (change / pop_2020) * 100

        print(f"Species: {species}")
        print(f"  Population change: {change}")
        print(f"  Percentage change: {percent_change:.2f}%")

        if change > 0:
            print("  Interpretation: Population increased 📈\n")
        elif change < 0:
            print("  Interpretation: Population declined 📉\n")
        else:
            print("  Interpretation: No change ⚖️\n")
