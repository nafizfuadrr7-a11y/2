def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Taking input from user
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("GCD of", x, "and", y, "is:", gcd(x, y))
