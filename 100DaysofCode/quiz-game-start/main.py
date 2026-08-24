from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [] #list of Question objects from each entry in data
for item in question_data:
    question = Question(item["question"], item["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.question_number < len(question_bank):
    #quiz = QuizBrain(question_bank) #to start the quiz
    quiz.next_question()
print("You've completed the quiz!")
print(f"Your score is {quiz.user_score}/{quiz.question_number}")