"""
1 — Using in for searching inside a list

One of the first anti-patterns that I was shocked to learn was using in for
searching, if a specific word is inside a list. I was doing this all the time
until I realized that this could be much quicker if we use set rather than
list. Here is an example to clarify what I mean:
"""

list_of_jobs = ["Machine learning",
                "Data Science",
                "Developer",
                "CTO",
                "Writer",
                "Product Manager"]

found = "CEO" in list_of_jobs
print(found)
