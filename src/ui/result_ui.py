import tkinter as tk
from tkinter import ttk

class ResultWindow(ttk.Frame):

    def update_score(self, score):
        self.score_var.set(f"Score: {score}")

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Label Frame
        label_frame = ttk.Frame(self)

        # Button Frame
        button_frame = ttk.Frame(self)

        # Score Label
        self.score_var = tk.StringVar(value="Score: ")
        score_label = tk.Label(label_frame, textvariable=self.score_var, font="Consolas 18")

        # Exit Button
        exit_button = ttk.Button(button_frame, text="Exit", command=lambda: controller.quit())
        restart_button = ttk.Button(button_frame, text="Restart", command=lambda: controller.load_setup())


        # Load on Screen
        score_label.pack(expand=True)
        label_frame.pack(expand=True, fill='both')
        exit_button.pack(expand=True, side='left')
        restart_button.pack(expand=True, side='left')
        button_frame.pack(expand=True, fill='both')
        
        restart_button.focus_set()

        # Key Bindings
        self.bind("<Control-r>", lambda eve: controller.load_setup())
        for children in self.winfo_children():
            children.bind("<Control-r>", lambda eve: controller.load_setup())