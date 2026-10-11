import json

expenses_amount = []

with open("expenses.json", encoding="utf-8") as file:
    expenses_json = json.load(file)

for line in expenses_json:
    expenses_amount.append(line["amount"])

# Вывод всех сумм
print("------")
print(f"Все суммы: {expenses_amount}")
print("------")

expenses_category_eda = []
expenses_category_transport = []
expenses_category_razvlechenia = []

for line in expenses_json:
    if line["category"] == "еда":
        expenses_category_eda.append(line["amount"])
    elif line["category"] == "транспорт":
        expenses_category_transport.append(line["amount"])
    elif line["category"] == "развлечения":
        expenses_category_razvlechenia.append(line["amount"])

# Выводит суммы по категориям
print("------")
print(f"Сумма еды: {sum(expenses_category_eda)}")
print(f"Сумма транспорта: {sum(expenses_category_transport)}")
print(f"Сумма развлечений: {sum(expenses_category_razvlechenia)}")
print("------")
