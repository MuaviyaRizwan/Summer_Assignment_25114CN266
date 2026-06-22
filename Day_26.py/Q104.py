questions = {
    "What is the capital of India?": "Delhi",
    "Which language is used for AI?": "Python",
    "Who is known as the father of computers?": "Charles Babbage"
}

score = 0

print("\n--- Quiz Application ---")

for question, answer in questions.items():
    user_answer = input(question + " ")
    if user_answer.strip().lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Correct answer is {answer}")

print(f"\nYour final score is {score}/{len(questions)}")
