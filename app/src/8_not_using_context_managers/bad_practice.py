"""
8 — Not using Context Managers

Context managers, implemented using the with statement in Python provide a
clean and reliable way to handle resources such as file handles, network
connections, error handling, and locks. Opening and closing files without
it could lead to data leakage, unsecured file handling, and other
unpredictable problems.
"""

file = open('myfile.txt', 'r')
# Do something with the file
file.close()
