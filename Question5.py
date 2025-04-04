celsius_temps = [0, 25, 37, 100, -5, 15]

fahrenheit_temps = list(map(lambda c: c * 9/5 + 32, celsius_temps))

print("Celsius temperatures:", celsius_temps)
print("Fahrenheit temperatures:", fahrenheit_temps)

print("\nTemperature conversion table:")
print("Celsius\tFahrenheit")
print("-" * 20)
for c, f in zip(celsius_temps, fahrenheit_temps):
    print(f"{c}\t{f}")