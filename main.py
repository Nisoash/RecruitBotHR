# main.py

from agents.sourcing_agent import find_candidates
from agents.screening_agent import screen_candidates
from agents.interview_agent import schedule_interviews

def main():
    print("🤖 Welcome to RecruitBot!")
    
    # STEP 1: Source raw names (fake data)
    keyword = "Python Developer"
    print(f"\n🔍 Looking for candidates with: {keyword}")
    raw_names = find_candidates(keyword)

    # STEP 2: Create fake profiles from those names
    candidates = [
        {"name": "Alice Johnson", "skills": ["Python", "Django", "SQL"]},
        {"name": "Bob Smith", "skills": ["JavaScript", "React"]},
        {"name": "Clara Lee", "skills": ["Python", "FastAPI", "Azure"]}
    ]

    print("\n📋 All candidates:")
    for c in candidates:
        print(f" - {c['name']} ({', '.join(c['skills'])})")

    # STEP 3: Screen for required skill
    required_skill = "Python"
    screened = screen_candidates(candidates, required_skill)

    print("\n✅ Screened candidates (with Python):")
    for c in screened:
        print(f" - {c['name']}")

    # STEP 4: Schedule interviews
    schedule = schedule_interviews(screened)

    print("\n📨 Interview confirmations sent!")

if __name__ == "__main__":
    main()
