names = ["Anold", "Kudakwashe", "Tinashe", "Rumbidzai", "Munyaradzi","Emildah", "Ambrose"]

# Writing names to the file
with open("names.txt", "w") as file:
    for name in names:
        file.write(f"{name}\n")

with open("names.txt", "r") as file:
    for line in file:
        print(line.strip())

print("Names have been written to and read from names.txt successfully")