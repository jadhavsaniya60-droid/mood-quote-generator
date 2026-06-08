import random
from quotes import quotes

mood = input("Enter your mood (happy, sad, motivated, stressed): ").lower()

if mood in quotes:
    print("\nQuote:")
    print(random.choice(quotes[mood]))
else:
    print("Sorry, mood not found.")
