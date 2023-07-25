"""
Tip 💡: The same applies when using the "inplace" argument when performing
operations on data frames in the Pandas library.
"""


def modify_database(data):
    # Create a copy of the DataFrame and modify the 'age' column in the copy
    modified_data = data.copy()
    modified_data['age'] = modified_data['age'] + 1

    return modified_data
