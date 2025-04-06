from data import question_data 
from question_model import Question 
from quiz_brain import QuizBrain

question_bank =[]

for question in question_data:
    question_text = question["text"]
    question_ans = question["answer"]
    new_question = Question(question_text, question_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.new_question()
while quiz.still_has_question():
    quiz.new_question()
    
print("You've completed the Quiz.")
print(f"Your final score is : {quiz.score}/{quiz.question_number}")