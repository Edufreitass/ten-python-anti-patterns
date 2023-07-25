"""
9— Manipulating Arguments

This one got me into a lot of trouble at work!!

Modifying the original Arguments, for example, a dataset, inside a function is
considered very bad practice due to unexpected side effects, potential data
integrity issues, and difficulties in traceability and debugging. A better
way is always to pass an argument by copying and returning new values from
the functions.
"""

import pandas as pd


def modify_database(data):
    # Modify the 'age' column in the original DataFrame
    data['age'] = data['age'] + 1
