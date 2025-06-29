def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return "❌ Divide by zero!" if b == 0 else a / b

def calculate(num1, num2, operator):
    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return subtract(num1, num2)
    elif operator == '*':
        return multiply(num1, num2)
    elif operator == '/':
        return divide(num1, num2)
    else:
        return "❌ Invalid operator!"

def main():
    print("🔢 Aditya's Calculator (Refactored)")
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+ - * /): ")
        num2 = float(input("Enter second number: "))
        result = calculate(num1, num2, operator)
        print("✅ Result:", result)
    except ValueError:
        print("❌ Please enter valid numbers.")

if __name__ == "__main__":
    main()
