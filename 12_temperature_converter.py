def fah_to_cels(temp):
    celsius = ((temp - 32) * 5/9)
    print("Temperature in fahrenheit: ",temp)
    print("Temperature in celsius: ",celsius)
def cels_to_fah(temp):
    fahrenheit = ((temp * 9/5) + 32)
    print("Temperature in celsius: ",temp)
    print("Temperature in fahrenheit: ",fahrenheit)

print("*** WELCOME TO TEMPERATURE CONVERTER ***")
print("""
      1. Fahrenheit to Celsius
      2. Celsius to Fahrenheit
""")
choice = int(input("Select your choice: "))
if choice == 1:
    temp = eval(input("Enter your temperature: "))
    fah_to_cels(temp)
elif choice == 2:
    temp = eval(input("Enter your temperature: "))
    cels_to_fah(temp)
else:
    print("Invalid choice!")