# 1
length = lambda x: len(x)
print(length("Hello, World!"))

# 2
positive_or_negative = lambda x: "Positive" if x > 0 else "Negative"
print(positive_or_negative(10))
print(positive_or_negative(-5))

# 3
surface_triangle = lambda b, h: 0.5 * b * h
print(surface_triangle(10, 5))

# 4
is_even = lambda x: True if x % 2 == 0 else False
print(is_even(4))
print(is_even(7))

# 5
greater_than_10 = lambda x: True if x > 10 else False
print(greater_than_10(15))
print(greater_than_10(5))   
