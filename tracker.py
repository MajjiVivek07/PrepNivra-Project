from datetime import date
from storage import save_data

def get_score():
    while True:
        try:
            n = float(input("Score (0-100): "))
            if 0 <= n <= 100: return n
            print("Score must be from 0 to 100.")
        except ValueError: print("Enter a valid number.")

def add_score(data):
    print("Categories: Aptitude, Python, Technical Interview, HR Interview")
    category = input("Category: ").strip().title()
    allowed = ["Aptitude", "Python", "Technical Interview", "Hr Interview"]
    if category not in allowed:
        print("Please enter one of the listed categories."); return
    score = get_score()
    data["scores"].append({"category": category, "score": score, "date": str(date.today())})
    save_data(data); print("Score saved.")

def add_coding(data):
    title = input("Problem name: ").strip()
    if not title: print("Problem name cannot be empty."); return
    while True:
        status = input("Status (Completed/Practising): ").strip().title()
        if status in ["Completed", "Practising"]: break
        print("Enter Completed or Practising.")
    data["coding"].append({"title": title, "status": status, "date": str(date.today())})
    save_data(data); print("Coding practice saved.")

def show_history(data):
    print("\n--- HISTORY ---")
    if not data["scores"] and not data["coding"]:
        print("No history yet."); return
    for x in data["scores"]: print(f"{x['date']} | {x['category']} | {x['score']:g}%")
    for x in data["coding"]: print(f"{x['date']} | Coding: {x['title']} | {x['status']}")
