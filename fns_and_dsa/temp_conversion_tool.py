

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
def main():
    """Main function to demonstrate temperature conversion."""
    temperature = int(input("Enter temperature to convert: "))
    a = input("Is this in Fahrenheit (F) or Celsius (C)? ").strip().upper()
    if a == 'F':
            fahrenheit = fahrenheit_to_celsius(temperature)
            print(f"{temperature}°F is {fahrenheit:.2f}°C")
    elif a == 'C':
             celsius = celsius_to_fahrenheit(temperature)
             print(f"{temperature}°C is {celsius:.2f}°F")
    else:
        print("Invalid input. Please enter 'F' for Fahrenheit or 'C' for Celsius.")
        return
if __name__ == "__main__":
    main()
