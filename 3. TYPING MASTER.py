import time
import difflib
import random

texts = ["The raindrops danced on the window pain like a chorus of applause.",
         "The moon's soft glow cast long shadows on the cobble-stoned street.",
         "A flock of birds soared through the sapphire sky like a graceful ballerina.",
         "The ocean waves sang a soothing lullaby, gently coaxing the sand to sleep.",
         "The autumn leaves danced in the crisp air, fluttering like colorful butterflies.",
         "The forest whispered secrets to the wind, as if sharing ancient tales."]

text = random.choice(texts)

print("Welcome to the typing master!")
print("You will be shown a text. Type it as accurately and quickly as possible.\n")

print("Here is your text:")
print(text)
print("\nStart typing after pressing Enter...")

input() 
start_time = time.time()  

user_input = input("\nYour input: ") 

end_time = time.time()

time_taken = end_time - start_time

def calculate_accuracy(prompt, input_text):
    matcher = difflib.SequenceMatcher(None, prompt, input_text)
    return round(matcher.ratio() * 100, 2)

accuracy = calculate_accuracy(text, user_input)

print("\nTyping test completed!")
print(f"Time taken: {time_taken:.2f} seconds")
print(f"Accuracy: {accuracy}%")

if accuracy == 100:
    print("Perfect! Well done.")
elif accuracy >= 90:
    print("Great job! Very accurate.")
elif accuracy >= 75:
    print("Good effort! Keep practicing to improve your accuracy.")
else:
    print("Keep practicing! You'll get better with more practice.")

