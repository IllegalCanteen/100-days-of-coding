from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz:QuizBrain):
        self.no_questions=0
        self.window=Tk()
        self.quiz=quiz
        self.score = quiz.score
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR,pady=20,padx=20)
        self.score_count=Label(text=f"Score : {self.score}",fg="white",bg=THEME_COLOR)
        self.score_count.grid(row=0,column=1)

        self.canvas=Canvas(width=300,height=250,bg="white")
        self.question=self.canvas.create_text((150,125),text=f"yo yo yo",font=("Arial",20,"italic"),fill=THEME_COLOR,width=280)
        self.canvas.grid(row=1,column=0,columnspan=2,padx=50,pady=50)
        self.true_img = PhotoImage(file="images/true.png")
        self.correct=Button(image=self.true_img, command=self.correct,highlightthickness=0)
        self.correct.grid(row=2,column=0)
        self.false_img=PhotoImage(file="images/false.png")
        self.wrong=Button(image=self.false_img,command=self.false,highlightthickness=0)
        self.wrong.grid(row=2,column=1)
        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        self.no_questions+=1
        self.canvas.config(bg="white")
        question_text=self.quiz.next_question()
        self.canvas.itemconfig(self.question,text=question_text)
    def get_feedback(self,user_answer):
        if self.quiz.still_has_questions():
            result = self.quiz.check_answer(user_answer)
            if result:
                self.canvas.config(bg="green")
                self.score+=1
                self.score_count.config(text=f"Score : {self.score}")
                self.window.after(1000,self.get_next_question)



            if not result:
                self.canvas.config( bg="red")
                self.window.after(1000, self.get_next_question)
        else:
            self.canvas.itemconfig(self.question,text=f"Score:{self.score}")
            self.correct.config(state="disabled")
            self.wrong.config(state="disabled")


    def correct(self):
        self.get_feedback("true")
    def false(self):
        self.get_feedback("false")
