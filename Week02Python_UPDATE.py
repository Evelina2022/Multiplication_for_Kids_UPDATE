import random

correct = 0
question = []

for i in range(1, 11):
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    answer = num_1 * num_2
    user_answer = int(input(f"Q{i}: {num_1} x {num_2} = "))
    if user_answer == answer:
        question.append(f"Q{i}: {num_1} x {num_2} = {user_answer} (Correct)")
        correct += 1
    else:
        question.append(f"Q{i}: {num_1} x {num_2} = {user_answer} (Incorrect)")

print("\n10 Question Summary:\n")
for questions in question:
    print(questions)

print(f"\nYou answered {correct} out of 10 questions correctly.")
