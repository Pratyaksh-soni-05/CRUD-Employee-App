# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Function to run the temperature converter
def temperature_converter():  
    print("                                Welcome to the Temperature Converter!\n")
    print("Choose the conversion direction:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = int(input("Enter your choice (1 or 2): "))

    # Celsius to Fahrenheit
    if choice == 1:
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

    # Fahrenheit to Celsius
    elif choice == 2:
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

    else:
        print("Invalid choice! Please select 1 or 2.")

    # Ask if the user wants to do another conversion
    replay = input("Do you want to convert another temperature? (yes/no): ").lower()
    if replay == 'yes':
        temperature_converter()

# Start the program
temperature_converter()
