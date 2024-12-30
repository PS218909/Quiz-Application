import tkinter as tk
from tkinter import ttk
import random

AMOUNT = [10, 20, 50]

CATEGORY = [
    ["Any", random.randint(16, 20)],
    ["Entertainment: Board Games", 16],
    ["Science & Nature", 17],
    ["Science: Computers", 18],
    ["Science: Mathematics", 19],
    ["Mythology", 20]
]

TYPE = "multiple"

class SetUpQuizWindow(ttk.Frame):
    """
        Quiz Form
    """

    def start_command(self, selected_amount, selected_category):
        selected_category_index = CATEGORY[0][0]
        for category in CATEGORY:
            if category[0] == selected_category:
                selected_category_index = category[1]
        self.controller.load_quiz(selected_amount, selected_category_index)

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.configure(width=800, height=600)
        self.propagate(False)

        # Setting Amount Combobox
        amount_label = ttk.Label(self, text="Number of Question\'s: ")
        amount_var = tk.IntVar(value=AMOUNT[0])
        amount_combo = ttk.Combobox(
            self, 
            textvariable=amount_var, 
            state="readonly"
        )
        amount_combo['values'] = AMOUNT
        
        # Setting Category Combobox
        category_label = ttk.Label(self, text="Category: ")
        category_var = tk.StringVar(value = CATEGORY[0][0])
        category_combo = ttk.Combobox(
            self, 
            textvariable=category_var, 
            state="readonly"
        )
        
        category_combo['values'] = tuple([category[0] for category in CATEGORY])
        
        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure((0, 1, 2), weight=1)

        # Button
        button_start = ttk.Button(
            self, 
            text="Start", 
            command=lambda: self.start_command(amount_var.get(), category_var.get()),
            width=100
        )
        
        # Placing Objects
        amount_label.grid(row=0, column=0, sticky='e', pady=5,)
        amount_combo.grid(row=0, column=1, sticky='w', pady=5)
        category_label.grid(row=1, column=0, sticky='e', pady=5)
        category_combo.grid(row=1, column=1, sticky='w', pady=5)
        button_start.grid(row=2, column=0, columnspan=2, pady=5)
        
        # Key Bindings
        self.bind("<Return>", lambda eve: self.start_command(amount_var.get(), category_var.get()))