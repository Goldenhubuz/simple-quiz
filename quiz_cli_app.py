import json

QUESTIONS_FILE = "questions.json"

def load_questions():
    """Load questions from a file."""
    try:
        with open(QUESTIONS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def ask_questions(questions):
    """Ask multiple-choice questions and provide feedback."""
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for idx, option in enumerate(q['options'], 1):
            print(f"{idx}. {option}")
        
        try:
            answer = int(input("Enter your choice: ")) - 1
            if 0 <= answer < len(q['options']) and q['options'][answer] == q['answer']:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Incorrect! The correct answer is: {q['answer']}")
        except ValueError:
            print("❌ Invalid input. Skipping question.")
    
    print(f"\nYour final score: {score}/{len(questions)}")

def main():
    """Main function to run the quiz application."""
    questions = load_questions()
    if not questions:
        print("No questions found! Please add some questions in questions.json.")
        return
    
    ask_questions(questions)

if __name__ == "__main__":
    main()