def factorial(n):
    """Calculate the factorial of a non-negative integer n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    # Test the factorial function
    number = 5
    print(f"The factorial of {number} is {factorial(number)}")

if __name__ == "__main__":
    main()
