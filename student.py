

def get_profile(old=None):
    old = old or {}

    print("\n--- Student Profile ---")

    name = input(
        f"Enter your name: ").strip()

    if not name:
        name = old.get("name", "")

    while not name:
        print("Name cannot be empty.")
        name = input("Enter your name: ").strip()

    roles = {
        "1": "Python Developer",
        "2": "Java Developer",
        "3": "Data Analyst",
        "4": "Data Scientist",
        "5": "Full Stack Developer",
        "6": "Other"
    }

    print("\nChoose your target role:")
    for number, role_name in roles.items():
        print(f"{number}. {role_name}")

    choice = input("Enter your choice (1-6): ").strip()

    while choice not in roles:
        print("Please choose a number from 1 to 6.")
        choice = input("Enter your choice (1-6): ").strip()

    role = roles[choice]

    if role == "Other":
        role = input("Enter your target role: ").strip()
        while not role:
            print("Target role cannot be empty.")
            role = input("Enter your target role: ").strip()

    return {"name": name, "role": role}


