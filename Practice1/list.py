""" 
list comprehension is a way to create a new list with less syntax.
Can mimic certain lambda functions, easier to read.
list = [expression for item in iterable]
list = [expression for item in iterable if conditional]
list = [expression if/else for item in iterable]
"""
# Example

# Using range and for

square = []
for i in range(1,11):
    square.append(i * i)

print(square)

# Same using list comprehension

squares = [i *i for i in range(1, 11)]
print(squares)

# Using lambda & filter
student = [100,90,80,70,60,50,40,30,20,10,0]
passed = list(filter(lambda x: x >= 60, student))
print(passed)

# Using list comprehension
passed_student = [i if i >= 60 else "FAILED" for i in student]
print(passed_student)