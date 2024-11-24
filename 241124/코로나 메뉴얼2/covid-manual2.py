categories = {"A": 0, "B": 0, "C": 0, "D": 0}
emergency_count = 0

for _ in range(3):
    symptom, temperature = input().split()
    temperature = int(temperature)

    if symptom == "Y" and temperature >= 37:
        categories["A"] += 1
        emergency_count += 1
    elif symptom == "N" and temperature >=37:
        categories["B"] += 1
    elif symptom == "Y" and temperature < 37:
        categories["C"] += 1
    else:
        categories["D"] += 1

output = f"{categories['A']} {categories['B']} {categories['C']} {categories['D']}"
if emergency_count >= 2:
    output += " E"

print(output)