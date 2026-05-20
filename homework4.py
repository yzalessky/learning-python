def analyze_grades(students):
    best = max(students, key=lambda s: s["grade"])
    average = round(sum(s["grade"] for s in students)/len(students), 2)
    students_passed = [s["name"] for s in students if s["grade"] > 70]
    return{
        "best": best,
        "average": average,
        "passed": students_passed
    }

students = [
    {"name": "Анна", "grade": 85},
    {"name": "Борис", "grade": 72},
    {"name": "Вера", "grade": 91},
    {"name": "Григорий", "grade": 64},
    {"name": "Дарья", "grade": 78}
]

result = analyze_grades(students)
print(f"Лидер: {result['best']['name']} ({result['best']['grade']})\n")
print(f"Средний бал: {result['average']}\n")
print("Прошли:")
for name in result["passed"]:
    print(f"• {name}")