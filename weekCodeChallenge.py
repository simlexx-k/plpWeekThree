# Coding Challenge 1: Large Power
def large_power(base, exponent):
    # Calculate the result of base to the power of exponent
    result = base ** exponent
    # Check if the result is greater than 5000
    if result > 5000:
        return True
    else:
        return False

# Test the function
print(large_power(10, 3))  # Output: False
print(large_power(2, 10))  # Output: True

# Coding Challenge 2: Divisible By Ten
def divisible_by_ten(num):
    # Calculate the remainder of the input divided by 10
    remainder = num % 10
    # Check if the remainder is 0
    if remainder == 0:
        return True
    else:
        return False

# Test the function
print(divisible_by_ten(25))  # Output: False
print(divisible_by_ten(100))  # Output: True
