"""
Tip 💡: Searching in sets is quicker than searching in lists because sets are
implemented using hash tables, which provide constant-time average-case
complexity for searching (O(1))
"""

list_of_jobs = {"Machine learning",
                "Data Science",
                "Developer",
                "CTO",
                "Writer",
                "Product Manager"}

found = "CEO" in list_of_jobs
print(found)
