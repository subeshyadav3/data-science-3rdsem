import os
import json
import time

def clearscreen():
    """Clears the screen based on the operating system."""
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux/Mac
        os.system('clear')

def header():
    """Prints the game header."""
    print("**************** Welcome to the Python Quiz Game ********************\n")

def load_questions(filename):
    """Loads questions from a JSON file."""
    with open(filename, 'r') as file:
        questions = json.load(file)
    return questions

def start_quiz():
    """Starts the quiz game."""
    timer_limit = 300  # 5 minutes in seconds
    start_time = time.time()  # Record the start time
    score = 0

    # Display rules and instructions
    header()
    print("Rules of the Game:\n")
    print("1) Total number of questions: 25")
    print("2) Total Time: 5 minutes")
    print("3) Scores will be displayed at the end")
    print("4) Scoring system:")
    print("   a) Correct answer: 1 point")
    print("   b) Incorrect answer: 0 points")
    input("\nPress Enter to start the Quiz...")

    clearscreen()
    header()

    # Load questions from the file
    questions = load_questions('questions.json')

    for idx, question in enumerate(questions):
        # Calculate remaining time
        elapsed_time = time.time() - start_time
        remaining_time = timer_limit - elapsed_time

        if remaining_time <= 0:
            print("\nTime's Up!")
            break

        clearscreen()
        header()
        print(f"Remaining Time: {int(remaining_time)} seconds")
        print(f"Score: {score}")

        # Display the current question and options
        print(f"\nQuestion {idx + 1}: {question['question']}")
        for i, option in enumerate(question['options']):
            print(f"{i + 1}. {option}")

        # Get the user's answer
        get_useranswer = input("\nYour answer (1/2/3/4): ").strip()

        if get_useranswer not in ['1', '2', '3', '4']:
            print("Invalid input! Please select a valid option (1-4).")
            time.sleep(1)
            continue

        # Validate the answer
        correct_answer = question['answer']
        if question['options'][int(get_useranswer) - 1] == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer is: {correct_answer}")

        time.sleep(2)

    # Display the final score
    clearscreen()
    print("**************** Quiz Over ****************")
    print(f"Your final score is: {score}/{len(questions)}")
    print(f"Your percentage: {(score / len(questions)) * 100:.2f}%")

if __name__ == "__main__":
    start_quiz()
