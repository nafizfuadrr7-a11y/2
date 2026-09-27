def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

a, b = 50, 15
g, x, y = extended_gcd(a, b)
print(f"GCD({a},{b}) = {g}")
print(f"x = {x}, y = {y}")
print(f"Check: {a}*{x} + {b}*{y} = {a*x + b*y}")
