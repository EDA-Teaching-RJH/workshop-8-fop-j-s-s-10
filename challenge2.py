import re

a = input()
print(re.search(r"^[a-zA-Z]{4}\d{4}$", a))
