import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.geometry("600x600")
root.resizable(width=False, height=False)
root.configure(bg="orange")
root.title("IQ")

# VARIABLES
user_name = tk.StringVar()
question_index = tk.StringVar()
questions = ["What is 9+7?", "What is 7+7?", "What is 7*3?",
             "What is 8*2?", "What is 9/9?", "What is 9/3?",
             "What is 5-5?", "What is 9-7?", "What is 25+25?", "What is 2*2?"]
options = [["16", "15", "14", "13"], ["12", "14", "11", "10"], ["20", "19", "21", "17"],
           ["11", "5", "4", "16"], ["1", "3", "5", "0"], ["0", "3", "1", "2"],
           ["1", "2", "0", "3"], ["4", "5", "6", "2"], ["50", "51", "49", "47"], ["2", "4", "3", "1"]]
answers = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1]
current_question = 0
score = 0
selected_question = []
# VARIABLES

def reset():
    global current_question, score, selected_question, f6
    current_question = 0
    score = 0
    selected_question = []
    for widget in main_design_instance.f5.winfo_children():
        widget.destroy()
    main_design_instance.l1.config(text="Welcome to IQ Programmed By Python")
    l4 = tk.Label(main_design_instance.f5, bg="orange", text="Enter Your Name: ", font=("arial", 16))
    l5 = tk.Entry(main_design_instance.f5, bg="grey", textvariable=user_name, font=("arial", 16), width=16)
    l6 = tk.Label(main_design_instance.f6, bg="orange", text="Enter Question Index (3-5): ", font=("arial", 16))
    l7 = tk.Entry(main_design_instance.f6, bg="grey", textvariable=question_index, font=("arial", 16), width=16)
    l4.pack(side="left")
    l5.pack(side="left")
    l6.pack(side="left")
    l7.pack(side="left")
    main_design_instance.b1.config(text="Submit", command=submit_name)

def show_result():
    global current_question, score, user_name, question_index, selected_question
    for widget in main_design_instance.f5.winfo_children():
        widget.destroy()
    result_label = tk.Label(main_design_instance.f5, text=f"{user_name.get()} Scored {score} Points", bg="orange", font=("Arial", 16))
    result_label.pack()
    main_design_instance.b1.config(state=tk.NORMAL, text="Play Again", command=reset)

def check_answer(selected_option):
    global user_name, question_index, selected_question, current_question, score

    if selected_option == answers[selected_question[current_question]]:
        messagebox.showinfo("Correct!", "Correct answer!")
        score += 1
    else:
        messagebox.showerror("Incorrect!", "Incorrect answer!")
    current_question += 1
    show_questions()

def show_questions():
    global user_name, question_index, selected_question
    for widget in main_design_instance.f5.winfo_children():
        widget.destroy()

    if current_question < len(selected_question):
        question_label = tk.Label(main_design_instance.f5, text=questions[selected_question[current_question]], bg="orange", font=("Arial", 16))
        question_label.pack()

        for i, option in enumerate(options[selected_question[current_question]]):
            option_button = tk.Button(
                main_design_instance.f5,
                text=option,
                bg="red",
                fg="white",
                font=("Arial", 16, "bold"),
                borderwidth=0,
                command=lambda idx=i: check_answer(idx)
            )
            option_button.pack(pady=5)
    else:
        show_result()

def play():
    global user_name, question_index, selected_question
    selected_question = random.sample(range(len(questions)), int(question_index.get()))
    main_design_instance.b1.config(state=tk.DISABLED)
    show_questions()

def submit_name():
    global user_name, question_index, f6
    if user_name.get() == "":
        messagebox.showerror("Error", "Please enter your name")
    elif question_index.get() == "":
        messagebox.showerror("Error", "Please select question index")
    elif int(question_index.get()) < 3 or int(question_index.get()) > 5:
        messagebox.showerror("Error", "Please enter between 3 and 5")
    else:
        messagebox.showinfo("Success", "Name and Question Index submitted")
        main_design_instance.l1.config(text=f"Welcome {user_name.get()} You Will Face {question_index.get()} Questions")

        for widget in main_design_instance.f5.winfo_children():
            widget.destroy()
        for widget in main_design_instance.f6.winfo_children():
            widget.destroy()

        main_design_instance.b1.config(text="Start", command=play)

class main_design:
    def __init__(self, master):
        self.f1 = tk.Frame(master, bg="black")
        self.f2 = tk.Frame(master, bg="black")
        self.f3 = tk.Frame(master, bg="black")
        self.f4 = tk.Frame(master, bg="black")
        self.f5 = tk.Frame(master, bg="orange")
        self.f6 = tk.Frame(master, bg="orange")
        self.l1 = tk.Label(self.f1, bg="black", fg="white", text="Welcome to IQ Programmed By Python", font=("arial", 16))
        self.l2 = tk.Label(self.f2, bg="black", fg="white", text="   ", font=("arial", 16))
        self.l3 = tk.Label(self.f3, bg="black", fg="white", text="   ", font=("arial", 16))
        self.l4 = tk.Label(self.f5, bg="orange", text="Enter Your Name: ", font=("arial", 16))
        self.l5 = tk.Entry(self.f5, bg="grey", textvariable=user_name, font=("arial", 16), width=16)
        self.l6 = tk.Label(self.f6, bg="orange", text="Enter Question Index (3-5): ", font=("arial", 16))
        self.l7 = tk.Entry(self.f6, bg="grey", textvariable=question_index, font=("arial", 16), width=16)
        self.b1 = tk.Button(self.f4, bg="black", fg="white", text="Submit", font=("arial", 16), borderwidth=0, command=submit_name)
        self.f1.pack(side="top", fill="x")
        self.f2.pack(side="left", fill="y")
        self.f3.pack(side="right", fill="y")
        self.f4.pack(side="bottom", fill="x")
        self.f5.pack(side="top", fill="x")
        self.f6.pack(side="top", fill="x")
        self.l1.pack(side="top", fill="x")
        self.l2.pack(side="left", fill="y")
        self.l3.pack(side="right", fill="y")
        self.l4.pack(side="left")
        self.l5.pack(side="left", padx=87)
        self.l6.pack(side="left")
        self.l7.pack(side="left")
        self.b1.pack(side="bottom", fill="x")

main_design_instance = main_design(root)

root.mainloop()