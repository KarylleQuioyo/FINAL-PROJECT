import random

questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "What is the largest mammal?", "answer": "Blue Whale"},
    {"question": "What is the capital of Japan?", "answer": "Tokyo"},
    {"question": "Who was the first President of the United States?", "answer": "George Washington"},
    {"question": "What color is a banana?", "answer": "Yellow"},
    {"question": "How many continents are there?", "answer": "Seven"},
    {"question": "What is the boiling point of water in Celsius?", "answer": "100"},
    {"question": "What is the longest river in the world?", "answer": "Nile"},
    {"question": "What is the smallest continent?", "answer": "Australia"},
    {"question": "What is the largest ocean?", "answer": "Pacific Ocean"},
    {"question": "What is the smallest country in the world?", "answer": "Vatican City"},
    {"question": "Who wrote 'Romeo and Juliet'?", "answer": "William Shakespeare"},
    {"question": "What is the capital of Italy?", "answer": "Rome"},
    {"question": "How many sides does a triangle have?", "answer": "Three"},
    {"question": "What is the primary ingredient in an omelette?", "answer": "Eggs"},
    {"question": "What is the capital of Germany?", "answer": "Berlin"},
    {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
    {"question": "What is the largest bone in the human body?", "answer": "Femur"},
    {"question": "What is the main ingredient in guacamole?", "answer": "Avocado"},
    {"question": "How many letters are there in the English alphabet?", "answer": "Twenty-six"},
    {"question": "What is the name of the toy cowboy in Toy Story?", "answer": "Woody"},
    {"question": "What is the square root of 64?", "answer": "Eight"},
    {"question": "What is the tallest mountain in the world?", "answer": "Mount Everest"},
    {"question": "What is the primary ingredient in bread?", "answer": "Flour"},
    {"question": "What is the capital of Canada?", "answer": "Ottawa"},
    {"question": "How many hours are there in a day?", "answer": "Twenty-four"},
    {"question": "What is the chemical symbol for water?", "answer": "H2O"},
    {"question": "What is the fastest land animal?", "answer": "Cheetah"},
    {"question": "What is the capital of Australia?", "answer": "Canberra"},
    {"question": "How many wheels does a bicycle have?", "answer": "Two"},
    {"question": "What is the capital of Spain?", "answer": "Madrid"},
    {"question": "What do bees produce?", "answer": "Honey"},
    {"question": "What is the capital of Mexico?", "answer": "Mexico City"},
    {"question": "How many days are there in a week?", "answer": "Seven"},
    {"question": "What is the main ingredient in pizza?", "answer": "Dough"},
    {"question": "What is the largest animal in the ocean?", "answer": "Blue Whale"},
    {"question": "Who wrote 'Harry Potter'?", "answer": "J.K. Rowling"},
    {"question": "What is the capital of the United Kingdom?", "answer": "London"},
    {"question": "What planet is known as the Earth's twin?", "answer": "Venus"},
    {"question": "What is the main ingredient in sushi?", "answer": "Rice"},
    {"question": "What is the capital of Brazil?", "answer": "Brasilia"},
    {"question": "What is 5 multiplied by 6?", "answer": "Thirty"},
    {"question": "How many colors are there in a rainbow?", "answer": "Seven"},
    {"question": "What is the primary ingredient in spaghetti?", "answer": "Pasta"},
    {"question": "What is the capital of Russia?", "answer": "Moscow"},
    {"question": "What is the largest desert in the world?", "answer": "Sahara"},
    {"question": "Which ocean is the deepest?", "answer": "Pacific Ocean"},
    {"question": "What is the smallest prime number?", "answer": "Two"},
    {"question": "What is the capital of China?", "answer": "Beijing"},
    {"question": "How many legs does a spider have?", "answer": "Eight"},
    {"question": "What is the main ingredient in a taco?", "answer": "Tortilla"},
    {"question": "What is the capital of Egypt?", "answer": "Cairo"},
    {"question": "What is the chemical symbol for gold?", "answer": "Au"},
    {"question": "What is the capital of India?", "answer": "New Delhi"},
    {"question": "What do cows drink?", "answer": "Water"},
    {"question": "What is the capital of Thailand?", "answer": "Bangkok"},
    {"question": "How many players are there in a soccer team?", "answer": "Eleven"},
    {"question": "What is the capital of Argentina?", "answer": "Buenos Aires"},
    {"question": "What is the freezing point of water in Celsius?", "answer": "Zero"},
    {"question": "What is the primary ingredient in chocolate?", "answer": "Cocoa"},
    {"question": "What is the capital of Kenya?", "answer": "Nairobi"},
    {"question": "What is the main ingredient in a hamburger?", "answer": "Beef"},
    {"question": "What is the capital of Turkey?", "answer": "Ankara"},
    {"question": "What is the primary ingredient in pancakes?", "answer": "Flour"},
    {"question": "What is the capital of South Africa?", "answer": "Pretoria"},
    {"question": "What is the largest island in the world?", "answer": "Greenland"},
    {"question": "What is the main ingredient in French fries?", "answer": "Potatoes"},
    {"question": "What is the capital of Greece?", "answer": "Athens"},
    {"question": "What is the main ingredient in ice cream?", "answer": "Milk"},
    {"question": "What is the capital of Portugal?", "answer": "Lisbon"},
    {"question": "What is the main ingredient in lemonade?", "answer": "Lemon"},
    {"question": "What is the capital of Poland?", "answer": "Warsaw"},
    {"question": "What is the main ingredient in Caesar salad?", "answer": "Romaine lettuce"},
    {"question": "What is the capital of Sweden?", "answer": "Stockholm"},
    {"question": "What is the main ingredient in hummus?", "answer": "Chickpeas"},
    {"question": "What is the capital of Norway?", "answer": "Oslo"},
    {"question": "What is the main ingredient in mayonnaise?", "answer": "Eggs"},
    {"question": "What is the capital of Finland?", "answer": "Helsinki"},
    {"question": "What is the main ingredient in burritos?", "answer": "Tortilla"},
    {"question": "What is the capital of Denmark?", "answer": "Copenhagen"},
    {"question": "What is the main ingredient in chili?", "answer": "Beans"},
    {"question": "What is the capital of the Netherlands?", "answer": "Amsterdam"},
    {"question": "What is the main ingredient in omelets?", "answer": "Eggs"},
    {"question": "What is the capital of Belgium?", "answer": "Brussels"},
    {"question": "What is the main ingredient in sushi?", "answer": "Rice"},
    {"question": "What is the capital of Austria?", "answer": "Vienna"},
    {"question": "What is the main ingredient in risotto?", "answer": "Rice"},
    {"question": "What is the capital of Switzerland?", "answer": "Bern"},
    {"question": "What is the main ingredient in guacamole?", "answer": "Avocado"},
    {"question": "What is the capital of Hungary?", "answer": "Budapest"},
    {"question": "What is the main ingredient in salad?", "answer": "Lettuce"},
    {"question": "What is the capital of Ireland?", "answer": "Dublin"},
    {"question": "What is the main ingredient in pasta?", "answer": "Flour"},
    {"question": "What is the capital of Iceland?", "answer": "Reykjavik"},
    {"question": "What is the main ingredient in ketchup?", "answer": "Tomatoes"},
    {"question": "What is the capital of Luxembourg?", "answer": "Luxembourg City"},
    {"question": "What is the main ingredient in soup?", "answer": "Broth"},
    {"question": "What is the main ingredient in stew?", "answer": "Meat"},
    {"question": "What is the main ingredient in popcorn?", "answer": "Corn"},
]

random.shuffle(questions)  

user_answers = []
correct_count = 0

print("Welcome to the interactive quiz! Let's get started.\n")


def conduct_quiz():
    global correct_count
    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        user_answer = input("Your answer: ")
        user_answers.append({"question": q['question'], "your_answer": user_answer, "correct_answer": q['answer']})
        if user_answer.lower() == q['answer'].lower():
            correct_count += 1



def display_results():
    print("\nQuiz completed!")
    print(f"You got {correct_count} out of {len(questions)} correct.\n")

    while True:
        option = input("Do you want to see you answers? (Y/N):  ")

        if option == 'Y':
            print("Here are your answers:\n")
            for i, ans in enumerate(user_answers, 1):
                print(f"Question {i}: {ans['question']}")
                print(f"Your answer: {ans['your_answer']}")
                print(f"Correct answer: {ans['correct_answer']}\n")
        elif option == 'N':
            print("Quiz session ended.")
            break

conduct_quiz()

display_results()
