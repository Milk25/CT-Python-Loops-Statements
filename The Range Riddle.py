import random






each_day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

moods = ["Happy", "Sad", "Energetic", "Calm"]

for i in range(len(each_day_of_week)):
    mood = random.choice(moods)

    print(f"On {each_day_of_week[i]}, you were feeling {mood.lower()}.")







