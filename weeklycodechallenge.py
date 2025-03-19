#Personalised greeting app.
def personalized_greeting():
    name = input("Enter your name: ")
    color = input("What's your fav color? ")
    print(f"hello, {name}! Your fav color, {color}, is dope!")

#personalised_greeting()

#Simple quiz game.
def quiz_game():
    questions = {
        "What's the capital of France?": "b",
        "What is the full definition of 4K UHD?": "c",
        "What does CPU stand for?": "a",
    }

    options = [
        "\na) Nairobi  b) Paris  c) Tokyo",
        "\na) Ultra Heavy Display  b) Unanimous High Display  c) Ultra High Display",
        "\na) Central Processing Unit  b) Computer Personal Unit  c) Central Police Unit"
    ]

    score = 0
    print("Welcome to the trivia! Answer with a, b, or c.\n")

    for i, (question, answer) in enumerate(questions.items()):  
        print(question)
        print(options[i])  # Using the index to get the correct options
        user_answer = input("Your answer: ").lower()

        if user_answer == answer:
            print("✔️ Correct!\n")
            score += 1
        else:
            print(f"✖️ Wrong answer. The correct answer was {answer.upper()}.\n")

    print(f"Game over! Your final score is {score}/{len(questions)}")

quiz_game()

#quiz_game

import random
def joke_generator():
    jokes = [
        "Why do coders prefer dark mode? For light attracts bugs!",
        "Why did the coder quit his/her job? For he didn't get their arrays",
        "What do you call a snake in a computer? Python"
    ]
    print(random.choice(jokes))

joke_generator