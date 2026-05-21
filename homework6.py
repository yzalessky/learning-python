def analyze_transactions(transactions):
    total_income = sum(i["amount"] for i in transactions if i["type"] == "income")
    total_expense = sum(e["amount"] for e in transactions if e["type"] == "expense")
    balance = total_income - total_expense
    max_expense = max((e for e in transactions if e["type"] == "expense"), key=lambda e: e["amount"])
    return{
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance,
        "max_expense": max_expense
    }

transactions = [
    {"date": "2026-01-01", "amount": 1500, "type": "income"},
    {"date": "2026-01-03", "amount": 200, "type": "expense"},
    {"date": "2026-01-05", "amount": 3000, "type": "income"},
    {"date": "2026-01-07", "amount": 450, "type": "expense"},
    {"date": "2026-01-10", "amount": 800, "type": "expense"},
    {"date": "2026-01-15", "amount": 2000, "type": "income"},
]

result = analyze_transactions(transactions)
print(f"Доход итого: {result['total_income']}")
print(f"Расход итого: {result['total_expense']}")
print(f"Сальдо: {result['balance']}\n")
print("Самый большой расход:")
print(result["max_expense"]["date"])
print(result["max_expense"]["amount"])