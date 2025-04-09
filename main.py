name = input("Enter your name: ")

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
        score += 1
    else:
        print("Wrong!")

print(f"{name}, you scored {score} out of {len(questions)}.")

if score == len(questions):
    print("Excellent! 🎉 You got all answers right!")
elif score >= len(questions) // 2:
    print("Good job! 👍 But there's room for improvement.")
else:
    print("Keep practicing! 💪 You'll get better.")
