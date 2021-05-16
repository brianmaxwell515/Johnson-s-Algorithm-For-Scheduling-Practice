import tkinter as tk
import ast
from time import process_time_ns

win = tk.Tk()
win.title("Johnson's Algorithm Scheduling")
machine = []

##################### UI #####################

machine_title_1 = tk.Label(text="機器A 加工時間")
machine_title_1.grid(row=0, column=0, sticky='E')
machine_title_2 = tk.Label(text="機器B 加工時間")
machine_title_2.grid(row=1, column=0, sticky='E')
machine_title_3 = tk.Label(text="機器C 加工時間")
machine_title_3.grid(row=2, column=0, sticky='E')
machine_title_4 = tk.Label(text="機器D 加工時間")
machine_title_4.grid(row=3, column=0, sticky='E')
machine_title_5 = tk.Label(text="機器E 加工時間")
machine_title_5.grid(row=4, column=0, sticky='E')
machine_title_6 = tk.Label(text="機器F 加工時間")
machine_title_6.grid(row=5, column=0, sticky='E')
machine_title_7 = tk.Label(text="機器G 加工時間")
machine_title_7.grid(row=6, column=0, sticky='E')
machine_title_8 = tk.Label(text="機器H 加工時間")
machine_title_8.grid(row=7, column=0, sticky='E')
machine_title_9 = tk.Label(text="機器I 加工時間")
machine_title_9.grid(row=8, column=0, sticky='E')
machine_title_10 = tk.Label(text="機器J 加工時間")
machine_title_10.grid(row=9, column=0, sticky='E')

machine_entry_1 = tk.Entry()
machine_entry_1.grid(row=0, column=1)
machine_entry_2 = tk.Entry()
machine_entry_2.grid(row=1, column=1)
machine_entry_3 = tk.Entry()
machine_entry_3.grid(row=2, column=1)
machine_entry_4 = tk.Entry()
machine_entry_4.grid(row=3, column=1)
machine_entry_5 = tk.Entry()
machine_entry_5.grid(row=4, column=1)
machine_entry_6 = tk.Entry()
machine_entry_6.grid(row=5, column=1)
machine_entry_7 = tk.Entry()
machine_entry_7.grid(row=6, column=1)
machine_entry_8 = tk.Entry()
machine_entry_8.grid(row=7, column=1)
machine_entry_9 = tk.Entry()
machine_entry_9.grid(row=8, column=1)
machine_entry_10 = tk.Entry()
machine_entry_10.grid(row=9, column=1)

best_order_title = tk.Label(text="最佳工作順序 : ")
best_order_title.grid(row=11, column=0, sticky='E')
best_order_result = tk.Label(text="")
best_order_result.grid(row=11, column=1, sticky='W')

makespan_title = tk.Label(text="總時間 (小時) : ")
makespan_title.grid(row=12, column=0, sticky='E')
makespan_result = tk.Label(text="")
makespan_result.grid(row=12, column=1, sticky='W')

idle_title = tk.Label(text="閒置時間 (小時) : ")
idle_title.grid(row=13, column=0, sticky='E')
idle_result = tk.Label(text="")
idle_result.grid(row=13, column=1, sticky='W')

process_title = tk.Label(text="處理時間 : ")
process_title.grid(row=14, column=0, sticky='E')
process_result = tk.Label(text="")
process_result.grid(row=14, column=1, sticky='W')


##################### Function #####################

# Get machine value
def get_val():
    # Start the stopwatch / counter
    t1_start = process_time_ns()
    # Get Value
    global machine
    machine = []
    try:
        machine.append(list(ast.literal_eval(machine_entry_1.get())))
    except SyntaxError:
        print("entry_1 is blank")
    try:
        machine.append(list(ast.literal_eval(machine_entry_2.get())))
    except SyntaxError:
        print("entry_2 is blank")
    try:
        machine.append(list(ast.literal_eval(machine_entry_3.get())))
    except SyntaxError:
        print("entry_3 is blank")
    try:
        machine.append(list(ast.literal_eval(machine_entry_4.get())))
    except SyntaxError:
        print("entry_4 is blank")
    try:
        machine.append(list(ast.literal_eval(machine_entry_5.get())))
    except SyntaxError:
        print("entry_5 is blank")
    try:
        machine.append(list(ast.literal_eval(machine_entry_6.get())))
    except SyntaxError:
        print("entry_6 is blank")
    try:
        machine.append(list(ast.literal_eval(machine_entry_7.get())))
    except SyntaxError:
        print("entry_7 is blank")
    try:
        machine.append(list(ast.literal_eval(machine_entry_8.get())))
    except SyntaxError:
        print("entry_8 is blank")
    try:
        machine.append(list(ast.literal_eval(machine_entry_9.get())))
    except SyntaxError:
        print("entry_9 is blank")
    try:
        machine.append(list(ast.literal_eval(machine_entry_10.get())))
    except SyntaxError:
        print("entry_10 is blank")

    print(f"Machine input : {machine}")
    print(type(machine))

    # Main variable
    job = len(machine[0])
    max_makespan = {}
    # Main
    machine_order = sum_process_time(machine, job)
    makespan = find_all_order(machine, machine_order)
    best_order = find_best_order(makespan, machine_order)
    best_makespan = min(makespan)
    idle_time = find_idle_time(best_makespan, machine)
    # Stop the stopwatch / counter
    t1_stop = process_time_ns()
    t1 = t1_stop-t1_start
    # Print result
    print(best_order)
    print(best_makespan)
    print(idle_time)
    print(t1_stop, t1_start)
    print(t1)
    # Output to UI
    best_order_result.config(text=best_order)
    makespan_result.config(text=best_makespan)
    idle_result.config(text=idle_time)
    process_result.config(text=t1)


# Schdule sort
def schedule_sort(job, machine_A, machine_B):
    sorted_machine = []
    sorted_A = []
    sorted_B = []
    res_1 = []
    res_2 = []

    for i in range(job):
        if machine_A[i] < machine_B[i]:
            sorted_machine.append(0)
        else:
            sorted_machine.append(1)

    for i in range(len(sorted_machine)):
        if sorted_machine[i] == 0:
            sorted_A.append(machine_A[i])
        else:
            sorted_B.append(machine_B[i])

    sorted_A.sort()
    sorted_B.sort()
    # print(sorted_A)
    # print(sorted_B)

    for i in sorted_A:
        res_1.append(machine_A.index(i))

    for i in sorted_B:
        res_2.insert(0, machine_B.index(i))

    res = res_1 + res_2
    res_print = [x+1 for x in res]
    return res_print


# Sum process time
def sum_process_time(machine, job):
    machine_order = []
    for i in range(1, len(machine)):
        machine_1 = machine[:i]
        machine_2 = machine[-i:]
        machine_1 = [sum(x) for x in zip(*machine_1)]
        machine_2 = [sum(x) for x in zip(*machine_2)]
        # print(machine_1)
        # print(machine_2)
        machine_order.append(schedule_sort(job, machine_1, machine_2))
    return machine_order


# Product Input & Ouput Time
def in_and_out_process(machine, machine_order):
    machine_order = [x-1 for x in machine_order]
    intime = [0]*len(machine)
    # outime = [0]*len(machine)
    for i in range(len(machine[0])):
        for j in range(len(machine)):
            current_process = machine[j][machine_order[i]]
            if j > 0:
                if intime[j] < intime[j-1]:
                    intime[j] = intime[j-1]
            intime[j] += current_process
    makespan = max(intime)
    return makespan


# Find all order
def find_all_order(machine, machine_order):
    makespan = []
    for i in range(len(machine_order)):
        makespan.append(in_and_out_process(machine, machine_order[i]))
    return makespan


# Find best order
def find_best_order(makespan, machine_order):
    order = makespan.index(min(makespan))
    return machine_order[order]


# Find idle time
def find_idle_time(best_makespan, machine):
    process_time = 0
    for i in range(len(machine)):
        process_time += sum(machine[i])
    total_makespan = best_makespan*len(machine)
    res = total_makespan - process_time
    return res


btn_start = tk.Button(text="Start", width=30, height=2, command=get_val)
btn_start.grid(row=10, column=0, columnspan=2)


win.mainloop()
