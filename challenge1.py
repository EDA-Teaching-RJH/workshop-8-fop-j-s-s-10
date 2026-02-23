import re

a = input()
print(re.search(r"^07\d{9}", a))
