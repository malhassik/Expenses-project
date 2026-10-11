import json
import csv

expenses_amount = []

with open("expenses.json", encoding="utf-8") as file:
    expenses_json = json.load(file)

for line in expenses_json:
    expenses_amount.append(line["amount"])

# Вывод всех сумм
print(f"Всего расходов: {len(expenses_json)}")
print(f"Общая сумма: {sum(expenses_amount)}")

expenses_category_sums = {}

for expense in expenses_json:
    cat = expense["category"]
    amount = expense["amount"]
    if cat in expenses_category_sums:
        expenses_category_sums[cat] += amount
    else:
        expenses_category_sums[cat] = amount

# Выводит суммы по категориям
print(expenses_category_sums)

# Сохраняет сводку в summary.json
summary = {
    "total_count": len(expenses_json),
    "total_sum": sum(expenses_amount),
    "average": round(sum(expenses_amount) / len(expenses_json), 2),
    "max_expense": max(expenses_json, key=lambda e: e["amount"]),
    "by_category": expenses_category_sums,
}

with open("summary.json", "w", encoding="utf-8") as file:
    json.dump(summary, file, ensure_ascii=False, indent=2)

# Экспортирует все расходы в expenses.csv
with open("expenses.csv", "w", encoding="utf-8", newline="") as file:
    write = csv.DictWriter(file, fieldnames=["date", "category", "amount"])
    write.writeheader()
    write.writerows(expenses_json)
