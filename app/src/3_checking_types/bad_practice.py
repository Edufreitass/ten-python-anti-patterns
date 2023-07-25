"""
3 — Checking Types

I also have been using type(variable) == type for type checking which is
considered an anti-pattern because it may not handle subclasses properly while
using isinstance(variable, int) is more flexible, accommodating subclasses.
"""

variable: int = 1
if type(variable) == int:
    print(True)
else:
    print(False)
