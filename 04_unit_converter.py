def length_converter(value, from_unit, to_unit):
    units = {'meter': 1, 'kilometer': 1000, 'centimeter': 0.01, 'mile': 1609.34, 'inch': 0.0254, 'foot': 0.3048}
    return value * units[from_unit] / units[to_unit]

def weight_converter(value, from_unit, to_unit):
    units = {'gram': 1, 'kilogram': 1000, 'pound': 453.592, 'ounce': 28.3495}
    return value * units[from_unit] / units[to_unit]

def volume_converter(value, from_unit, to_unit):
    units = {'liter': 1, 'milliliter': 0.001, 'gallon': 3.78541, 'cup': 0.24}
    return value * units[from_unit] / units[to_unit]

def main():
    print("Unit Converter")
    print("1. Length\n2. Weight\n3. Volume")
    choice = input("Choose conversion type (1/2/3): ")
    try:
        value = float(input("Enter value to convert: "))
        if choice == '1':
            print("Units: meter, kilometer, centimeter, mile, inch, foot")
            from_unit = input("From unit: ").lower()
            to_unit = input("To unit: ").lower()
            result = length_converter(value, from_unit, to_unit)
        elif choice == '2':
            print("Units: gram, kilogram, pound, ounce")
            from_unit = input("From unit: ").lower()
            to_unit = input("To unit: ").lower()
            result = weight_converter(value, from_unit, to_unit)
        elif choice == '3':
            print("Units: liter, milliliter, gallon, cup")
            from_unit = input("From unit: ").lower()
            to_unit = input("To unit: ").lower()
            result = volume_converter(value, from_unit, to_unit)
        else:
            print("Invalid choice.")
            return
        print(f"{value} {from_unit} = {result:.4f} {to_unit}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()