import json

with open("files/questions.json", 'r') as file:
 content = file.read()

data = json.loads(content)
user_answers = [{}]
score = 0
for question in data:
    print(question["question_text"])
    for index, answer in enumerate(question['answers']):
        outputs = f"{index + 1}-{answer}"
        print(outputs)
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score += 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"
    message = f"{result} {index +  1} Your Answer: {question['user_choice']} Correct answer: {question['correct_answer']}"
    print(message)
print(f"{score}/{len(data)}")