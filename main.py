import json

expenses = []

with open("expenses.json", encoding="utf-8") as file:
    expenses_json = json.load(file)

for line in expenses_json:
    expenses.append(line["amount"])

print("------")
print(expenses)
print("------")
