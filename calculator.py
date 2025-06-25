import time
print(" Welcome to Aditya's Python Calculator ")

def calculate():
    while True:
        print("\nChoose an operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '5':
            print(" Exiting calculator... Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print(" Invalid choice. Please select a valid option.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print(" Invalid input! Please enter numeric values only.")
            continue

        if choice == '1':
            result = num1 + num2
            op = '+'
        elif choice == '2':
            result = num1 - num2
            op = '-'
        elif choice == '3':
            result = num1 * num2
            op = '*'
        elif choice == '4':
            if num2 == 0:
                print(" Cannot divide by zero.")
                continue
            result = num1 / num2
            op = '/'

        print(f" Result: {num1} {op} {num2} = {round(result, 2)}")
        time.sleep(1.5)

calculate()
