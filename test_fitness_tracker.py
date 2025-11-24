def test_add_workout():
    workouts = []
    workout = {"name": "Running", "duration": 30, "calories": 300}
    workouts.append(workout)
    assert len(workouts) == 1
    assert workouts[0]["name"] == "Running"
    assert workouts[0]["duration"] == 30
    assert workouts[0]["calories"] == 300
    print("test_add_workout passed")

def test_calculate_summary():
    workouts = [
        {"name": "Running", "duration": 30, "calories": 300},
        {"name": "Cycling", "duration": 45, "calories": 400}
    ]
    total_duration = sum(w['duration'] for w in workouts)
    total_calories = sum(w['calories'] for w in workouts)

    assert total_duration == 75
    assert total_calories == 700
    print("test_calculate_summary passed")

def test_empty_workouts():
    workouts = []
    total_duration = sum(w['duration'] for w in workouts)
    total_calories = sum(w['calories'] for w in workouts)

    assert total_duration == 0
    assert total_calories == 0
    print("test_empty_workouts passed")

def test_invalid_input():
    def validate_input(duration, calories):
        try:
            duration_int = int(duration)
            calories_int = int(calories)
            return duration_int > 0 and calories_int > 0
        except:
            return False

    assert not validate_input("abc", "300")
    assert not validate_input("-5", "100")
    assert validate_input("30", "400")
    print("test_invalid_input passed")

if _name_ == "_main_":
    test_add_workout()
    test_calculate_summary()
    test_empty_workouts()
    test_invalid_input()
    print("All tests passed!")
