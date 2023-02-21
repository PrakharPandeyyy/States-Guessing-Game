class QuizBrain:
    def __init__(self,q_list):
        self.q_number=0
        self.ques_list = q_list
        self.score = 0
    def still_has_ques(self):
        if self.q_number < len(self.ques_list):
            return True
        else:
            return False
    def next_question(self):
        current_ques = self.ques_list[self.q_number]
        self.q_number +=1
        user_answer = input(f"Q.{self.q_number}: {current_ques.text} (True/False): ")
        self.check_answer(user_answer,current_ques.answer)


    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You are Right")
        else :
            print("You are Wrong")

        print(f"Your Current Score is {self.score}/{self.q_number}")
        print("\n")