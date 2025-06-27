print("Multiplication Table Generator ")

def generate_table(number, upto):
    print(f"\nMultiplication Table for {number} (up to {upto}):\n")
    table = ""
    for i in range(1, upto + 1):
        line = f"{number} x {i} = {number * i}"
        print(line)
        table += line + "\n"
    return table

def save_to_file(number, content):
    filename = f"table_{number}.txt"
    with open(filename, "w") as file:
        file.write(content)
    print(f"\nTable saved as '{filename}'")

try:
    num = int(input("Enter the number for the table: "))
    limit = int(input("Enter how far you want the table (e.g., 10, 20, 50): "))

    output = generate_table(num, limit)

    choice = input("\nDo you want to save this table to a file? (y/n): ").lower()
    if choice == 'y':
        save_to_file(num, output)

except ValueError:
    print("Invalid input! Please enter numeric values only.")
