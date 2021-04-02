from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question =  Question(question_text,question_answer)
    question_bank.append(new_question)
print(question_bank[0].question)

quiz = QuizBrain(question_bank)
while QuizBrain.still_has_question(quiz):
    QuizBrain.next_question(quiz)


print("You have completed the quiz successfully")
print(f"Your final score is {quiz.score}/{quiz.quiz_number}")