
from student import get_profile
from tracker import add_score, add_coding, show_history
from analyzer import show_report, recommendations
from storage import load_data, save_data


def main():
    data = load_data()

    print("\n=== PrepNivra: Placement Preparation Tracker ===")

    # Create a profile only if one does not exist
    if not data.get("profile"):
        data["profile"] = get_profile()
        save_data(data)

    while True:
        print("\n1. Student profile")
        print("2. Add aptitude/Python/interview score")
        print("3. Record coding practice")
        print("4. Progress report")
        print("5. Recommendations")
        print("6. History")
        print("7. Exit")

        choice = input("Choose 1-7: ").strip()

        if choice == "1":
            data["profile"] = get_profile(data["profile"])
            save_data(data)

            print("\n--- Student Profile ---")
            print("Name:", data["profile"]["name"])
            print("Target Role:", data["profile"]["role"])

        elif choice == "2":
            add_score(data)
            save_data(data)

        elif choice == "3":
            add_coding(data)
            save_data(data)

        elif choice == "4":
            show_report(data)

        elif choice == "5":
            recommendations(data)

        elif choice == "6":
            show_history(data)

        elif choice == "7":
            print("Good luck with your placement preparation!")
            break

        else:
            print("Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()

