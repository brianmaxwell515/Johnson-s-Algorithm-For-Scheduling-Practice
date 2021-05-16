import tkinter as tk
import ast

win = tk.Tk()
win.title("Johnson's Algorithm Scheduling")


job_title_1 = tk.Label(text="Job 1")
job_title_1.grid(row=0, column=0, sticky='E')
job_title_2 = tk.Label(text="Job 2")
job_title_2.grid(row=1, column=0, sticky='E')
job_title_3 = tk.Label(text="Job 3")
job_title_3.grid(row=2, column=0, sticky='E')
job_title_4 = tk.Label(text="Job 4")
job_title_4.grid(row=3, column=0, sticky='E')
job_title_5 = tk.Label(text="Job 5")
job_title_5.grid(row=4, column=0, sticky='E')
job_title_6 = tk.Label(text="Job 6")
job_title_6.grid(row=5, column=0, sticky='E')
job_title_7 = tk.Label(text="Job 7")
job_title_7.grid(row=6, column=0, sticky='E')
job_title_8 = tk.Label(text="Job 8")
job_title_8.grid(row=7, column=0, sticky='E')
job_title_9 = tk.Label(text="Job 9")
job_title_9.grid(row=8, column=0, sticky='E')
job_title_10 = tk.Label(text="Job 10")
job_title_10.grid(row=9, column=0, sticky='E')

job_entry_1 = tk.Entry()
job_entry_1.grid(row=0, column=1)
job_entry_2 = tk.Entry()
job_entry_2.grid(row=1, column=1)
job_entry_3 = tk.Entry()
job_entry_3.grid(row=2, column=1)
job_entry_4 = tk.Entry()
job_entry_4.grid(row=3, column=1)
job_entry_5 = tk.Entry()
job_entry_5.grid(row=4, column=1)
job_entry_6 = tk.Entry()
job_entry_6.grid(row=5, column=1)
job_entry_7 = tk.Entry()
job_entry_7.grid(row=6, column=1)
job_entry_8 = tk.Entry()
job_entry_8.grid(row=7, column=1)
job_entry_9 = tk.Entry()
job_entry_9.grid(row=8, column=1)
job_entry_10 = tk.Entry()
job_entry_10.grid(row=9, column=1)

best_order_title = tk.Label(text="Best order : ")
best_order_title.grid(row=11, column=0, sticky='E')
best_order_result = tk.Label(text="")
best_order_result.grid(row=11, column=1)

makespan_title = tk.Label(text="Makespan : ")
makespan_title.grid(row=12, column=0, sticky='E')
makespan_result = tk.Label(text="")
makespan_result.grid(row=12, column=1)

idle_title = tk.Label(text="Idle : ")
idle_title.grid(row=13, column=0, sticky='E')
idle_result = tk.Label(text="")
idle_result.grid(row=13, column=1)


def get_val():
    machine = []
    try:
        machine.append(list(ast.literal_eval(job_entry_1.get())))
    except SyntaxError:
        print("entry_1 is blank")
    try:
        machine.append(list(ast.literal_eval(job_entry_2.get())))
    except SyntaxError:
        print("entry_2 is blank")
    try:
        machine.append(list(ast.literal_eval(job_entry_3.get())))
    except SyntaxError:
        print("entry_3 is blank")
    try:
        machine.append(list(ast.literal_eval(job_entry_4.get())))
    except SyntaxError:
        print("entry_4 is blank")
    try:
        machine.append(list(ast.literal_eval(job_entry_5.get())))
    except SyntaxError:
        print("entry_5 is blank")
    try:
        machine.append(list(ast.literal_eval(job_entry_6.get())))
    except SyntaxError:
        print("entry_6 is blank")
    try:
        machine.append(list(ast.literal_eval(job_entry_7.get())))
    except SyntaxError:
        print("entry_7 is blank")
    try:
        machine.append(list(ast.literal_eval(job_entry_8.get())))
    except SyntaxError:
        print("entry_8 is blank")
    try:
        machine.append(list(ast.literal_eval(job_entry_9.get())))
    except SyntaxError:
        print("entry_9 is blank")
    try:
        machine.append(list(ast.literal_eval(job_entry_10.get())))
    except SyntaxError:
        print("entry_10 is blank")

    print(machine)
    print(type(machine))


btn_start = tk.Button(text="Start", width=30, height=2, command=get_val)
btn_start.grid(row=10, column=0, columnspan=2)

win.mainloop()
