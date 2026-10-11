import json

expenses_amount = []

with open("expenses.json", encoding="utf-8") as file:
    expenses_json = json.load(file)

for line in expenses_json:
    expenses_amount.append(line["amount"])

print("------")
print(f"Все суммы: {expenses_amount}")  # Вывод всех сумм
print("------")
