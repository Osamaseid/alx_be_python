# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
CELSIUS_TO_FAHRENHEIT_OFFSET = 32
FAHRENHEIT_TO_CELSIUS_OFFSET = 32

def convert_to_celsius(fahrenheit):
 
    global FAHRENHEIT_TO_CELSIUS_FACTOR, FAHRENHEIT_TO_CELSIUS_OFFSET
    return (fahrenheit - FAHRENHEIT_TO_CELSIUS_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
 
    global CELSIUS_TO_FAHRENHEIT_FACTOR, CELSIUS_TO_FAHRENHEIT_OFFSET
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + CELSIUS_TO_FAHRENHEIT_OFFSET

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == 'F':
            converted_temperature = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temperature}°C")
        elif unit == 'C':
            converted_temperature = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temperature}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
