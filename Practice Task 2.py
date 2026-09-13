total_age = 0.0
avg_age = 0.0
eyes = []

with open("optometry.txt", "r") as infile:
    for line in infile:
        line = line.strip()
        if not line or not line.startswith("#"):
            colour, age = line.split(",")
            eyes.append((colour.strip().lower(), int(age.strip())))

print(eyes)

total_age = sum(age for _, age in eyes)
avg_age = total_age / len(eyes)
print(f"Average age: {avg_age:.1f}")

for colour in ["brown", "blue", "green", "hazel"]:
    count = sum(1 for eye, _ in eyes if eye == colour)
    percentage = (count / len(eyes)) * 100
    print(f"{colour.capitalize()} eyes: {percentage:.1f}%")


