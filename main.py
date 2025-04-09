questions = {
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "What language is this game written in?": "Python"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question + " ")
    if user_answer.strip().lower() == answer.lower():
        print("Correct!")
        score = 1
    else:
        print("Wrong!")

print(f"You scored {score} out of {len(questions)}.")
