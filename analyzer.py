def show_report(data):
    p = data.get("profile", {})
    print("\n=== PREPNIVRA PROGRESS REPORT ===")
    print("Student:", p.get("name", "Student"))
    print("Target role:", p.get("role", "Python Developer"))
    print("Scores recorded:", len(data["scores"]))
    print("Coding problems recorded:", len(data["coding"]))
    print("Coding problems completed:", sum(x["status"] == "Completed" for x in data["coding"]))
    if data["scores"]:
        latest = {}
        for x in data["scores"]: latest[x["category"]] = x
        for category, item in latest.items(): print(f"{category}: {item['score']:g}% (latest)")
        avg = sum(x["score"] for x in data["scores"]) / len(data["scores"])
        print(f"Average of all recorded scores: {avg:.1f}%")
    else: print("Add scores to start tracking progress.")
    print("This is a practice indicator, not a guarantee of placement.")

def recommendations(data):
    if not data["scores"]:
        print("Add some scores first to receive recommendations."); return
    latest = {}
    for x in data["scores"]: latest[x["category"]] = x
    print("\n--- PRACTICE RECOMMENDATIONS ---")
    for category, item in sorted(latest.items(), key=lambda pair: pair[1]["score"]):
        score = item["score"]
        if score < 50: advice = "High priority: revise basics and practise 5-10 questions."
        elif score < 75: advice = "Medium priority: practise regularly and review mistakes."
        else: advice = "Maintain this skill with revision and timed practice."
        print(f"{category} ({score:g}%): {advice}")
