import math

def show_menu():
    print("\n🔢 Advanced Calculator")
    print("1️⃣ - Addition (+)")
    print("2️⃣ - Subtraction (-)")
    print("3️⃣ - Multiplication (*)")
    print("4️⃣ - Division (/)")
    print("5️⃣ - Exponentiation (^)")
    print("6️⃣ - Square Root (√)")
    print("7️⃣ - Remainder of division (%)")
    print("0️⃣ - Exit")

while True:
    show_menu()
    try:
        choice = int(input("Select the calculation number: "))  # تحويل الإدخال إلى int
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        continue

    if choice == 0:
        print("👋 Exiting the calculator. Goodbye!")
        break

    if choice in [1, 2, 3, 4, 5, 7]:  # العمليات التي تحتاج إلى رقمين
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Invalid input! Please enter valid numbers.")
            continue

    if choice == 1:
        print(f"✅ Result: {num1} + {num2} = {num1 + num2}")
    elif choice == 2:
        print(f"✅ Result: {num1} - {num2} = {num1 - num2}")
    elif choice == 3:
        print(f"✅ Result: {num1} * {num2} = {num1 * num2}")
    elif choice == 4:
        if num2 == 0:
            print("❌ Error: Division by zero is not allowed!")
        else:
            print(f"✅ Result: {num1} / {num2} = {num1 / num2}")
    elif choice == 5:
        print(f"✅ Result: {num1} ^ {num2} = {num1 ** num2}")
    elif choice == 6:
        try:
            num = float(input("Enter a number: "))
            if num < 0:
                print("❌ Error: Cannot calculate square root of a negative number.")
            else:
                print(f"✅ Result: √{num} = {math.sqrt(num)}")
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
    elif choice == 7:
        print(f"✅ Result: {num1} % {num2} = {num1 % num2}")
    else:
        print("❌ Invalid choice! Please select a valid option.")
