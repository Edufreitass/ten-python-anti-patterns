"""
2 — Inefficient loops

I’ve been programming in Python for over five years now and I have been using
an inefficient way to initialize lists most of the time. Recently, I have
discovered that using list comprehension is not only more concise but also
results in a speed increase. Here is an example:
"""

# For loop for initializing the list
result = []
for i in range(10):
    result.append(i * 2)
print(result)
