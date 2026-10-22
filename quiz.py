"""
The General Knowledge Quiz
A terminal-based trivia game built with Python.
Features a pool of trivia questions, random non-repeating question selection,
robust input normalization, score tracking, and replay options.
"""

import random

# A question bank of trivia questions.
# Each entry contains:
# - 'question': The question prompt.
# - 'answers': A list of accepted valid answers (all lowercased).
# - 'correct_display': The nicely formatted answer revealed if incorrect.
QUESTION_BANK = [
    {
        "question": "What is the capital of France?",
        "answers": ["paris"],
        "correct_display": "Paris",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "answers": ["mars"],
        "correct_display": "Mars",
    },
    {
        "question": "What is the largest ocean on Earth?",
        "answers": ["pacific", "pacific ocean"],
        "correct_display": "the Pacific Ocean",
    },
    {
        "question": "How many days are there in a standard leap year?",
        "answers": ["366", "366 days"],
        "correct_display": "366",
    },
    {
        "question": "What is the chemical symbol for water?",
        "answers": ["h2o"],
        "correct_display": "H2O",
    },
    {
        "question": "Who painted the Mona Lisa?",
        "answers": ["leonardo da vinci", "da vinci", "leonardo"],
        "correct_display": "Leonardo da Vinci",
    },
    {
        "question": "What is the hardest natural mineral on Earth?",
        "answers": ["diamond"],
        "correct_display": "Diamond",
    },
    {
        "question": "Which gas do plants absorb from the atmosphere for photosynthesis?",
        "answers": ["carbon dioxide", "co2"],
        "correct_display": "Carbon dioxide",
    },
    {
        "question": "How many continents are there on Earth?",
        "answers": ["7", "seven"],
        "correct_display": "7",
    },
    {
        "question": "What is the smallest prime number?",
        "answers": ["2", "two"],
        "correct_display": "2",
    },
    {
        "question": "Which element does the symbol 'O' represent on the periodic table?",
        "answers": ["oxygen"],
        "correct_display": "Oxygen",
    },
    {
        "question": "What is the tallest living animal in the world?",
        "answers": ["giraffe"],
        "correct_display": "Giraffe",
    },
]


def play_round(round_questions):
    """Plays a single 3-question round of the quiz."""
    print("\n" + "=" * 45)
    print("         THE GENERAL KNOWLEDGE QUIZ         ")
    print("=" * 45)
    print("Answer the 3 questions below:\n")

    # Initialize the score tracking variable
    score = 0
    total_questions = len(round_questions)

    # Ask each question sequentially
    for index, item in enumerate(round_questions, start=1):
        print(f"Question {index}: {item['question']}")

        # Clean input defensively: remove leading/trailing spaces and convert to lowercase
        user_answer = input("Your answer: ").strip().lower()

        # Check if user's sanitized answer matches any accepted valid answer
        if user_answer in item["answers"]:
            print("Correct! Excellent job! (+1 point)\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {item['correct_display']}.\n")

    # Display final score
    print("=" * 45)
    print(f"Quiz Complete! Your Final Score: {score}/{total_questions}")

    # Display a custom closing message based on the user's score
    if score == 3:
        print("Feedback: Outstanding! You got a perfect score!")
    elif score == 2:
        print("Feedback: Great job! You really know your general knowledge!")
    elif score == 1:
        print("Feedback: Good effort! A little more practice and you'll nail it!")
    else:
        print("Feedback: Better luck next time! Keep learning and try again!")
    print("=" * 45)


def main():
    # Maintain an active pool of remaining questions to prevent questions from repeating
    available_questions = list(QUESTION_BANK)
    random.shuffle(available_questions)

    while True:
        # If there are fewer than 3 questions left, replenish and reshuffle the pool
        if len(available_questions) < 3:
            available_questions = list(QUESTION_BANK)
            random.shuffle(available_questions)

        # Draw 3 unique, non-repeating questions for this round
        round_questions = [available_questions.pop() for _ in range(3)]

        # Play the 3-question quiz
        play_round(round_questions)

        # Prompt the player if they want another round
        play_again = input("\nWould you like to play another round? (yes/no): ").strip().lower()
        if play_again not in ("yes", "y"):
            print("\nThank you for playing The General Knowledge Quiz! Goodbye!\n")
            break


if __name__ == "__main__":
    main()
