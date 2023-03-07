# This function takes an integer n as input and returns the sum of numbers from 1 to n
def find_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

# Ask the user for input and call the function
n = int(input("Enter an integer: "))
result = find_sum(n)

# Output the result
print("The sum of numbers from 1 to", n, "is", result)