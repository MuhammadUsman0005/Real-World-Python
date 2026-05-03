HISTORY_FILE = "calculation_history.txt"

def show_history():
   file = open(HISTORY_FILE, "r")
   lines = file.readlines()
   if len(lines) == 0:
      print("No history found.")
   else:
      print("Calculation History:")
      for line in lines:
         print(line.strip())
   file.close()
   
def clear_history():
   file = open(HISTORY_FILE, "w")
   file.write("")
   file.close()
   print("History cleared.")

def save_to_history(num1,operation,num2,result):
   file = open(HISTORY_FILE, "a")
   file.write(f"{num1} {operation} {num2} = {result}\n")
   file.close()

def calculation(num1, operation, num2):
   if operation == "+":
      return num1 + num2
   elif operation == "-":
      return num1 - num2
   elif operation == "*":
      return num1 * num2
   elif operation == "/":
      if num2 != 0:
         return num1 / num2
      else:
         print("Error: Division by zero.")
         return None
   else:
      print("Invalid operation.")
      return None

def main():
    while True:
        print("\nSimple Calculator")
        print("1. Perform Calculation")
        print("2. Show History")
        print("3. Clear History")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            try:
                num1 = float(input("Enter first number: "))
                operation = input("Enter operation (+, -, *, /): ")
                num2 = float(input("Enter second number: "))
                result = calculation(num1, operation, num2)
                if result is not None:
                    print(f"Result: {result}")
                    save_to_history(num1, operation, num2, result)
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        elif choice == "2":
            show_history()
        elif choice == "3":
            clear_history()
        elif choice == "4":
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
