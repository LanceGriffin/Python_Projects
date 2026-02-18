#Lance Griffin
# 2/22/26
# This is a temperature conversion in python that allows the user to convert between Celsius, Fahrenheit, and Kelvin

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Function to convert Celsius to Kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Main function that the user interacts with
def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius and Fahrenheit to Kelvin")
    print("4. Kelvin to Celsius and Fahrenheit")
    choice = input("Choose a conversion (1-4): ")

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius}°C")
    elif choice == "3":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F and {kelvin}K")
    elif choice == "4":
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{kelvin}K is equal to {celsius}°C and {fahrenheit}°F")
    else:
        print("Invalid choice. Choose a number between 1 and 4.")

main()