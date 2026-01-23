from question_model import Question
from quiz_brain import QuizBrain
import requests
from ui import QuizInterface

parameters={
    "amount":10,
    "type":"boolean",
}
response=requests.get(url="https://opentdb.com/api.php",params=parameters)
data=response.json()["results"]
question_bank = []
for question in data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui=QuizInterface(quiz)

while quiz.still_has_questions():
    quiz.next_question()
