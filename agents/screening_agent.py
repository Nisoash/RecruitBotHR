# screening_agent.py

# Each candidate is a dictionary with name and skills
def screen_candidates(candidates, required_skill):
    print(f"\n🧠 Screening for skill: {required_skill}")
    
    screened = []
    for person in candidates:
        if required_skill.lower() in [skill.lower() for skill in person["skills"]]:
            screened.append(person)
    
    return screened
