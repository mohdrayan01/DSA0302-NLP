# 18.Implement a simple FOPC parser for basic logical expressions using python program.

import re
expression = input("Enter Expression: ")
pattern = r'([A-Za-z]+)\(([A-Za-z, ]+)\)'
match = re.match(pattern, expression)
if match:
    predicate = match.group(1)
    arguments = match.group(2).split(",")
    print("Predicate :", predicate)
    print("Arguments :", [arg.strip() for arg in arguments])
else:
    print("Invalid Expression")