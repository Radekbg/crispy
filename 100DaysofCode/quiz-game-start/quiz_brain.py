class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0 #everytime we create QuizBrain it will start at 0
        self.question_list = question_list
        self.user_score =0

    def next_question(self):     #Retrieve the item and the current quistion_number from the question_list
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number+1}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
        print(f"You answered: {user_answer}")
        self.question_number += 1

    def check_answer(self,user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.user_score += 1
            print(f"Your score is {self.user_score}")
        else:
            print("You got it wrong!")
        print(f"The correct answer was {correct_answer}")