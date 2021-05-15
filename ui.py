import tkinter as tk

win = tk.Tk()
win.title("Johnson's Algorithm Scheduling")


job_1 = tk.Label(text="Job 1")
job_1.grid(row=0, column=0, sticky='E')
job_2 = tk.Label(text="Job 2")
job_2.grid(row=1, column=0, sticky='E')
job_3 = tk.Label(text="Job 3")
job_3.grid(row=2, column=0, sticky='E')
job_4 = tk.Label(text="Job 4")
job_4.grid(row=3, column=0, sticky='E')
job_5 = tk.Label(text="Job 5")
job_5.grid(row=4, column=0, sticky='E')
job_6 = tk.Label(text="Job 6")
job_6.grid(row=5, column=0, sticky='E')
job_7 = tk.Label(text="Job 7")
job_7.grid(row=6, column=0, sticky='E')
job_8 = tk.Label(text="Job 8")
job_8.grid(row=7, column=0, sticky='E')
job_9 = tk.Label(text="Job 9")
job_9.grid(row=8, column=0, sticky='E')
job_10 = tk.Label(text="Job 10")
job_10.grid(row=9, column=0, sticky='E')

entry_1 = tk.Entry()
entry_1.grid(row=0, column=1)
entry_2 = tk.Entry()
entry_2.grid(row=1, column=1)
entry_3 = tk.Entry()
entry_3.grid(row=2, column=1)
entry_4 = tk.Entry()
entry_4.grid(row=3, column=1)
entry_5 = tk.Entry()
entry_5.grid(row=4, column=1)
entry_6 = tk.Entry()
entry_6.grid(row=5, column=1)
entry_7 = tk.Entry()
entry_7.grid(row=6, column=1)
entry_8 = tk.Entry()
entry_8.grid(row=7, column=1)
entry_9 = tk.Entry()
entry_9.grid(row=8, column=1)
entry_10 = tk.Entry()
entry_10.grid(row=9, column=1)

btn_addrow = tk.Button(text="Start", width=30, height=2)
btn_addrow.grid(row=10, column=0, columnspan=2)

best_order_title = tk.Label(text="Best order: ")
best_order_title.grid(row=11, column=0, sticky='E')
best_order_result = tk.Label(text="")
best_order_result.grid(row=11, column=1)

makespan_title = tk.Label(text="Makespan: ")
makespan_title.grid(row=12, column=0, sticky='E')
makespan_result = tk.Label(text="")
makespan_result.grid(row=12, column=1)

idle_title = tk.Label(text="Idle: ")
idle_title.grid(row=13, column=0, sticky='E')
idle_result = tk.Label(text="")
idle_result.grid(row=13, column=1)

win.mainloop()