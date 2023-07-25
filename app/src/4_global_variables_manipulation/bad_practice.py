"""
4 — Global Variables Manipulation

This might not be surprising but manipulating global variables directly inside
functions is considered bad practice because it can lead to code that is harder
to understand, maintain, and debug. Using function parameters and return
values, on the other hand, provides a more controlled and modular approach,
promoting better code organization and reusability.
"""

# global variable
count = 0


def increment_count():
    global count
    count += 1
    print(count)


if __name__ == '__main__':
    increment_count()
