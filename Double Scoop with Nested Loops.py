import random

each_day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

moods = ["Happy", "Sad", "Energetic", "Calm"]
times_of_day = ['morning', 'afternoon', 'evening']

for i in range(len(each_day_of_week)):
    # mood = random.choice(moods)
    for j in range(len(times_of_day)):
        mood = random.choice(moods)

    print(f"On {each_day_of_week[i]} {times_of_day[j]} you were feeling {mood.lower()}.")


