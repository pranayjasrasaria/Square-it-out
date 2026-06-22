def square_number(n):
    # Ensure n is a valid number (int or float)
    if not isinstance(n, (int, float)):
        raise TypeError("Input must be an integer or float.")
    return n ** 2   # Squaring using exponent operator

try:
    user_input = input("Enter a number: ").strip()

    # Attempt to convert input to float (handles integers & decimals)
    number = float(user_input)

    result = square_number(number)
    print(f"Square of {number} is {result}")

except ValueError:
    print("Invalid input. Please enter a valid numeric value.")
except TypeError as e:
    print(e)
except Exception as e:
    print(f"An unexpected error occurred: {e}")