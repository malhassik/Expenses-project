import json
import csv

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

# Сохраняет сводку в summary.json
summary = {
    "amounts": expenses_amount,
    "sum_eda": expenses_category_eda,
    "sum_transport": expenses_category_transport,
    "sum_eazvlechenia": expenses_category_razvlechenia,
}

with open("summary.json", "w", encoding="utf-8") as file:
    json.dump(summary, file, ensure_ascii=False, indent=2)

# Экспортирует все расходы в expenses.csv
with open("expenses.csv", "w", encoding="utf-8", newline="") as file:
    write = csv.DictWriter(file, fieldnames=["date", "category", "amount"])
    write.writeheader()
    write.writerows(expenses_json)
