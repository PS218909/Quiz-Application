import tkinter as tk
from tkinter import ttk

class QuizWindow(ttk.Frame):

    def load_data(self, question, options):
        self.question_var.set(question)
        self.option1_var.set(options[0])
        self.option2_var.set(options[1])
        self.option3_var.set(options[2])
        self.option4_var.set(options[3])
        self.submit_button.config(state=tk.NORMAL)

    def submit_ans(self):
        if str(self.submit_button['state']) == tk.NORMAL and self.radioButtonOption.get() != -1:
            self.controller.ans.append(self.radioButtonOption.get())
            self.submit_button.config(state=tk.DISABLED)
            self.message_var.set("")
            self.go_to_next_question()
        else:
            self.message_var.set("Select any option")

    def go_to_next_question(self):
        try:
            question_no, question, options = next(self.controller.data)
        except StopIteration:
            return self.controller.load_result()
        if question == "End":
            return self.controller.load_result()
        self.load_data(f"{question_no}. {question}", options)
        self.radioButtonOption.set(-1)

    def __init__(self, parent: tk.Frame, controller: tk.Tk):
        super().__init__(parent)
        self.controller = controller
        self.cnt = -1

        # Question
        self.question_var = tk.StringVar()
        self.question_var.set("Loading Question")
        question_label = tk.Label(
            self, 
            textvariable=self.question_var, 
            font="Consolas 15", 
            background='#334455', 
            wraplength=800, 
            height=10
        )

        self.radioButtonOption = tk.IntVar(value=-1)

        # Options
        self.option1_var = tk.StringVar(value="Loading Option 1")
        option1_radiobutton = ttk.Radiobutton(
            self, 
            variable=self.radioButtonOption, 
            textvariable=self.option1_var, 
            value=0, 
            command = lambda: self.radioButtonOption.set(0),
        )
        self.option2_var = tk.StringVar(value="Loading Option 2")
        option2_radiobutton = ttk.Radiobutton(
            self, 
            variable=self.radioButtonOption, 
            textvariable=self.option2_var, 
            value=1, 
            command = lambda: self.radioButtonOption.set(1)
        )
        self.option3_var = tk.StringVar(value="Loading Option 3")
        option3_radiobutton = ttk.Radiobutton(
            self, 
            variable=self.radioButtonOption, 
            textvariable=self.option3_var, 
            value=2, 
            command = lambda: self.radioButtonOption.set(2)
        )
        self.option4_var = tk.StringVar(value="Loading Option 4")
        option4_radiobutton = ttk.Radiobutton(
            self, 
            variable=self.radioButtonOption, 
            textvariable=self.option4_var, 
            value=3, 
            command = lambda: self.radioButtonOption.set(3)
        )

        # Submit Button
        self.submit_button = ttk.Button(self, text="Next", command=lambda: self.submit_ans())
        self.submit_button['state'] = tk.DISABLED

        # Label
        self.message_var = tk.StringVar()
        message_label = ttk.Label(self, textvariable=self.message_var, foreground='red')

        # Grid Configuration
        self.grid_rowconfigure(0, weight = 2)
        self.grid_rowconfigure((1, 2, 3, 4, 5, 6), weight = 1)
        self.grid_columnconfigure(0, weight = 1)

        # Loading on Screen
        question_label.grid(row=0, column=0, sticky='nsew')
        option1_radiobutton.grid(row=1, column=0)
        option2_radiobutton.grid(row=2, column=0)
        option3_radiobutton.grid(row=3, column=0)
        option4_radiobutton.grid(row=4, column=0)
        self.submit_button.grid(row=5, column=0, sticky='nsew', padx=40, pady=40)
        message_label.grid(row=6, column=0)

        self.bind_all("1", lambda eve: self.radioButtonOption.set(0))
        self.bind_all("2", lambda eve: self.radioButtonOption.set(1))
        self.bind_all("3", lambda eve: self.radioButtonOption.set(2))
        self.bind_all("4", lambda eve: self.radioButtonOption.set(3))
        option1_radiobutton.bind("<Return>", lambda eve: self.submit_ans())
        option2_radiobutton.bind("<Return>", lambda eve: self.submit_ans())
        option3_radiobutton.bind("<Return>", lambda eve: self.submit_ans())
        option4_radiobutton.bind("<Return>", lambda eve: self.submit_ans())
        self.bind("<Return>", lambda eve: self.submit_ans())