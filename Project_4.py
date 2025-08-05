# RECOMMENDATION SYSTEM
# Create a simple recommendation system that suggests items to
#  users based on their preferences. You can use techniques like
#  collaborative filtering or content-based filtering to recommend
#  movies, books, or products to users

from collections import defaultdict

print("===WELCOME TO RECOMMENDATION SYSTEM===")

mood_tags = {
    1:["anger","stress","calm","relax"],
    2:["bored","fun","learn","adventure"],
    3:["frustration","motivation","focus","calm"],
    4:["joy","celebration","fun","travel"],
    5:["peace","mindfulness","health","outdoors"]
}

item_dataset = {
    "Books":{
        "Anger Management":["anger", "calm", "relax"],
        "The Anger Trap":["anger", "stress"],
        "The Power of Boredom":["bored","learn"],
        "Atomic Habits":["motivation","focus"],
        "Ikigai":["peace", "mindfulness", "health"]
    },
    "Movies":{
        "Inside Out": ["anger", "joy", "calm"],
        "Inception": ["adventure", "fun", "learn"],
        "Soul": ["peace", "calm", "mindfulness"],
        "La La Land": ["joy", "celebration"],
        "Chef": ["peace", "fun", "outdoors"]
    },
    "Products":{
        "Stress Ball": ["anger", "stress", "calm"],
        "Meditation App": ["calm", "mindfulness"],
        "Puzzle Game": ["bored", "fun", "learn"],
        "Yoga Mat": ["peace", "health", "calm"],
        "Travel Backpack": ["travel", "adventure"]
    },
    "Things to do":{
        "Go for a walk": ["peace", "outdoors", "relax"],
        "Learn a new language": ["bored", "learn", "fun"],
        "Meditate": ["calm", "mindfulness"],
        "Plan a trip": ["travel", "fun"],
        "Dance": ["joy", "celebration", "fun"]
    }
}

print("Choose your mood")
print("1.Angry")
print("2.Bored")
print("3.Frustrated")
print("4.Happy")
print("5.Good/Peaceful")

mood = int(input("Enter number from above: "))

if mood in mood_tags:
    selected_tags = mood_tags[mood]

    print("\n === Suggestions for you ===\n")
    for category,items in item_dataset.items():
        scores = defaultdict(int)
        for item,tags in items.items():
            # Count for matching mood
            scores[item] = len(set(tags) & set(selected_tags))

        sorted_item = sorted(scores.items(),key=lambda x:x[1],reverse=True)

        best_item = [item for item,score in sorted_item if score > 0][:3]

        if best_item:
            print(f"{category}:{', '.join(best_item)}")
        else:
            print(f"{category}:No strong match found.")
else:
    print("\nInvalid choice.Please select a valid number")
