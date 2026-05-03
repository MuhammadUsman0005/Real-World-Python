import random


sports_subjects = [
    "Local Team", "Star Athlete", "Coach", "Rival Team", "Underdog"
]
sports_actions = [
    "wins championship", "suffers shocking defeat", "announces retirement", "signs record-breaking deal", "faces doping scandal"
]
sports_objects = [
    "after thrilling match", "in front of home crowd", "amidst controversy", "with last-minute goal", "in stunning upset"
]
celebrity_subjects = [
    "Famous Actor", "Pop Star", "Reality TV Star", "Renowned Director", "Social Media Influencer"
]
celebrity_actions = [
    "caught in scandal", "announces surprise engagement", "reveals shocking secret", "involved in bizarre incident", "wins unexpected award"
]
celebrity_objects = [
    "during live interview", "at exclusive party", "on social media", "in new movie", "amidst rumors"
]
government_subjects = [
    "President", "Prime Minister", "Senator", "Mayor", "Government Official"
]
government_actions = [
    "resigns amid controversy", "announces groundbreaking policy", "caught in corruption scandal", "faces impeachment", "wins landslide election"
]
government_objects = [
    "after leaked documents", "during press conference", "amidst protests", "in surprise move", "with international allies"
]
science_subjects = [
    "Renowned Scientist", "Research Team", "University", "Tech Company", "Government Agency"
]
science_actions = [
    "makes groundbreaking discovery", "faces ethical dilemma", "announces cure for disease", "involved in data fabrication scandal", "wins prestigious award"
]
science_objects = [
    "after years of research", "during international conference", "amidst controversy", "with revolutionary technology", "in unexpected breakthrough"
]
technology_subjects = [
    "Tech Giant", "Innovative Startup", "Famous CEO", "Renowned Engineer", "Government Agency"
]
technology_actions = [
    "launches revolutionary product", "faces massive data breach", "announces unexpected partnership", "involved in patent lawsuit", "wins innovation award"
]
technology_objects = [
    "after years of development", "during product launch event", "amidst controversy", "with cutting-edge technology", "in surprise announcement"
]
print("***** Welcome To FAKE NEWS HEADLINE Generator *****")
while True:
    print('''
        1. Sports Headline
        2. Celebrities Headline
        3. Government Headline
        4. Science Headline
        5. Technology Headline
        6. Exit Generator
    ''')
    user_choice = input("Select a category (1-5): ").strip()

    if user_choice == '1':
        sub = random.choice(sports_subjects)
        act = random.choice(sports_actions)
        obj = random.choice(sports_objects)
        
        headline = f"BREAKING NEWS: {sub} {act} {obj}."
        print("\n" + headline)
    elif user_choice == '2':
        sub = random.choice(celebrity_subjects)
        act = random.choice(celebrity_actions)
        obj = random.choice(celebrity_objects)
        
        headline = f"BREAKING NEWS: {sub} {act} {obj}."
        print("\n" + headline)
    elif user_choice == '3':
        sub = random.choice(government_subjects)
        act = random.choice(government_actions)
        obj = random.choice(government_objects)
        
        headline = f"BREAKING NEWS: {sub} {act} {obj}."
        print("\n" + headline)
    elif user_choice == '4':
        sub = random.choice(science_subjects)
        act = random.choice(science_actions)
        obj = random.choice(science_objects)
        
        headline = f"BREAKING NEWS: {sub} {act} {obj}."
        print("\n" + headline)
    elif user_choice == '5':
        sub = random.choice(technology_subjects)
        act = random.choice(technology_actions)
        obj = random.choice(technology_objects)
        
        headline = f"BREAKING NEWS: {sub} {act} {obj}."
        print("\n" + headline)
    elif user_choice == '6':
        break
    else:
        print("Invalide choice! Please enter between 1-5.")

print("\nThanks for using the FAKE NEWS HEADLINE Generator!")
