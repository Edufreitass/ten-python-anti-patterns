"""
7 — Deep Nested Code

This is considered an anti-pattern because it makes the code harder to read
and maintain, increasing the risk of introducing bugs or overlooking certain
conditions. Instead, we could use logical operators that flatten the code
structure and increase the readability of our code.
"""

condition1 = None
condition2 = None
condition3 = None
if condition1:
    if condition2:
        if condition3:
            # Perform some action
            pass
