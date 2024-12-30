import tkinter as tk
from tkinter import ttk
from ui import settings_ui
from ui import quiz_ui
from ui import result_ui
from utils import file_handler
from logic.quiz_logic import QuizLogic

class MainWindow(tk.Tk):
    '''
        Main GUI Window
    '''

    def show_frame(self, frame_class: ttk.Frame):
        frame_class.tkraise()
        frame_class.focus_set()
    
    def load_quiz(self, amount, category):
        self.show_frame(self.quiz)
        url = f"https://opentdb.com/api.php?amount={amount}&category={category}&type=multiple&encode=base64"
        self.ans = []
        self.quiz_logic = QuizLogic()
        self.quiz_logic.fetch_questions(url)
        self.data = self.quiz_logic.get_question()
        self.quiz.go_to_next_question()
    
    def load_setup(self):
        self.show_frame(self.setup)

    def load_result(self):
        score = self.quiz_logic.calculate_score(self.ans)
        self.result_frame.update_score(score)
        self.show_frame(self.result_frame)

    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}+100+0')

        # Window Frame
        self.frame = tk.Frame(self, background='green')
        self.frame.pack(fill="both", expand=True)

        # Setting UI
        self.setup = settings_ui.SetUpQuizWindow(self.frame, self)
        self.setup.config(width=size[0], height=size[1])
        self.setup.grid_propagate(False)
        self.setup.grid(row = 0, column=0, sticky='nsew')
        
        # Quiz UI
        self.quiz = quiz_ui.QuizWindow(self.frame, self)
        self.quiz.config(width=size[0], height=size[1])
        self.quiz.grid_propagate(False)
        self.quiz.grid(row = 0, column = 0, sticky='nsew')

        # Result UI
        self.result_frame = result_ui.ResultWindow(self.frame, self)
        self.result_frame.config(width = size[0], height=size[1])
        self.result_frame.grid_propagate(False)
        self.result_frame.grid(row=0, column=0, sticky='nsew')

        # Window
        self.show_frame(self.setup)

        # Binding Escape key as exit button
        self.bind("<Escape>", lambda eve: self.quit())
        self.mainloop()

MainWindow("Quiz Application", (800, 600))