"""
Tip 💡: A better approach would be to define these values somewhere
on the top or in a config file to make it easier to modify.
"""

# Define parameters on the top of the file or ideally in a config file
Threshold = 20

# some code

price = 30
if price > Threshold:
    print(True)
else:
    print(False)
