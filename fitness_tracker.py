workouts = []

def main_menu():
    print("\n FITNESS TRACKER")
    print("1. Add Workout")
    print("2. View Workouts")
    print("3. Calculate Total Duration & Calories")
    print("4. Exit")

    choice = input("Enter your choice: ")
    return choice


def add_workout():
    print("\n ADD WORKOUT")
    name = input("Enter workout name: ")
    duration = input("Enter duration (minutes): ")
    calories = input("Enter calories burned: ")

    workout = {
        "name": name,
        "duration": int(duration),
        "calories": int(calories)
    }

    workouts.append(workout)
    print("Workout added successfully!")


def view_workouts():
    print("\n YOUR WORKOUTS")

    if not workouts:
        print("No workouts recorded yet.")
        return

    for i, w in enumerate(workouts, start=1):
        print(f"{i}. {w['name']} - {w['duration']} min - {w['calories']} cal")


def calculate_summary():
    print("\n TOTAL WORKOUT SUMMARY")

    if not workouts:
        print("No workouts to calculate.")
        return

    total_duration = sum(w['duration'] for w in workouts)
    total_calories = sum(w['calories'] for w in workouts)

    print(f"Total Duration: {total_duration} minutes")
    print(f"Total Calories Burned: {total_calories} calories")


def start():
    while True:
        choice = main_menu()

        if choice == "1":
            add_workout()

        elif choice == "2":
            view_workouts()

        elif choice == "3":
            calculate_summary()

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")


start()
