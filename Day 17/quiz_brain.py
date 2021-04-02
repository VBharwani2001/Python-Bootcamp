class QuizBrain:
    def __init__(self, q_list):
        self.quiz_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        if self.quiz_number < len(self.question_list):
            if self.question_list[self.quiz_number].question != "":
                return True
            else:
                return False

    def next_question(self):
        current_question = self.question_list[self.quiz_number]
        self.quiz_number += 1
        answer = input(f"Q.{self.quiz_number}: {current_question.question} (True/False): ")
        self.check_answer(answer, current_question.answer)

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You got that correct")
            self.score += 1
        else:
            print("That's incorrect")
        print(f"Correct answer was {correct_ans}")
        print(f"Your score is {self.score}/{self.quiz_number}")