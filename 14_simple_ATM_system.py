correct_PIN = "1234"
balance = 5000

wrong_attempt = 3

for i in range(wrong_attempt):
    user_PIN = input("Enter PIN: ")

    if user_PIN == correct_PIN:
        break
    else:
        print("Wrong PIN!")

    if i == wrong_attempt - 1:
        print("Card Blocked!")
        exit()


print("\n1. Check balance")
print("2. Deposit money")
print("3. Withdraw money")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Balance:", balance)

elif choice == 2:
    deposit = float(input("Enter amount to deposit: "))
    if deposit <= 0:
        print("Invalid amount!")
        exit()
    balance += deposit
    print("Deposit successful! New balance:", balance)

elif choice == 3:
    withdraw = float(input("Enter amount to withdraw: "))
    if withdraw <= 0:
        print("Invalid amount!")
        exit()
    elif withdraw > balance:
        print("Insufficient balance!")
    elif withdraw % 100 != 0:
        print("ATM only allows multiples of 100")
    else:
        balance -= withdraw
        print("Withdraw successful! Remaining balance:", balance)

else:
    print("Invalid choice!")
