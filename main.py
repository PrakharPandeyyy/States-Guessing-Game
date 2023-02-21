from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank=[]
for question in question_data:
    text = question["text"]
    answer = question["answer"]
    new_question = Question(text,answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_ques():
    quiz.next_question()

print("You Have completed The Quiz , Congrats!!😘😘")


print(f"Your Final Score is {quiz.score}/{quiz.q_number}")
