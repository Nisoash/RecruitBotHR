# interview_agent.py

import random

# Fake time slots to choose from
TIME_SLOTS = [
    "Monday 10:00 AM",
    "Monday 2:00 PM",
    "Tuesday 11:00 AM",
    "Wednesday 3:00 PM"
]

def schedule_interviews(candidates):
    print("\n📅 Scheduling interviews...")

    schedule = {}
    for person in candidates:
        time = random.choice(TIME_SLOTS)
        schedule[person["name"]] = time
        print(f"✅ Scheduled {person['name']} at {time}")

    return schedule
