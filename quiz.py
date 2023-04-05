q1={
    "description" : "What's the answer of 1+1?",
    "options": [1, 2, 3, 4],
    "correct_answer": 2,
    "score" : 1
}

q2={
    "description" : "What's the answer of 6*4?",
    "options": [21, 22, 24, 28],
    "correct_answer": 24,
    "score" : 1
}

questions = []
questions.append(q1)
questions.append(q2)

class Quiz():
    def __init__(self) -> None:
        pass

    def ask_question(self, question):
        description = question["description"]
        options = question["options"]
        print(description)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer: "))
        while user_answer not in range(1, len(options) + 1):
            print(f"Invalid answer. Please enter a number between 1 and {len(options)}.")
            user_answer = int(input("Enter your answer: "))
        return options[user_answer-1]
    
    def check_question(self, question, answer):
        if answer==question["correct_answer"]:
            return True
        else:
            return False

quiz = Quiz()

for question in questions:
    answer = quiz.ask_question(question)
    if quiz.check_question(question, answer):
        print(f"you are correct: {answer}")
    else:
        print(f"you are incorrect: {answer}")