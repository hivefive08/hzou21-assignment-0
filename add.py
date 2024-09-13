# add.py
def add_two_numbers(a, b):
    return a + b

if __name__ == "__main__":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = add_two_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")
