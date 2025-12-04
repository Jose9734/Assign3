# Prompt the user for mass as an integer (in kilograms)
mass = input(int("Enter mass in kilograms:"))
light = 300,000,000
# Calculate the Einstein formula (don't forget to convert the input from str to
# int)
Einstein = mass * light * light

# Print the result
print(f"Value: {Einstein}")
