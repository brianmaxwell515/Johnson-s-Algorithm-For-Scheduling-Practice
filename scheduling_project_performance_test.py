from time import process_time
import numpy as np

machine = [[6, 17, 3, 10, 5],
           [10, 14, 10, 26, 15],
           [1, 17, 13, 31, 13],
           [13, 12, 17, 20, 15]]

# machine = [[5, 4, 8, 2, 6, 12],
#            [5, 3, 9, 7, 8, 15]]

# machine = [[5, 13, 6, 7], [3, 5, 4, 2], [7, 9, 5, 6]]

# machine = np.random.random_integers(1, 20, (100, 100))
# machine = machine.tolist()
# print(machine)


job = len(machine[0])
max_makespan = {}


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
    print(f"Machine group 1 (After compare) : {sorted_A}")
    print(f"Machine group 2 (After compare) : {sorted_B}")

    for i in sorted_A:
        res_1.append(machine_A.index(i))

    for i in sorted_B:
        res_2.insert(0, machine_B.index(i))

    res = res_1 + res_2
    res_print = [x+1 for x in res]
    print(f"Machine order result : {res_print} \n")
    return res_print


# Sum process time
def sum_process_time(machine):
    machine_order = []
    for i in range(1, len(machine)):
        machine_1 = machine[:i]
        machine_2 = machine[-i:]
        machine_1 = [sum(x) for x in zip(*machine_1)]
        machine_2 = [sum(x) for x in zip(*machine_2)]
        print(f"Machine group 1 : {machine_1}")
        print(f"Machine group 2 : {machine_2}")
        machine_order.append(schedule_sort(job, machine_1, machine_2))
    print(f"All machine order : {machine_order}")
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


def find_idle_time(best_makespan, machine):
    process_time = 0
    for i in range(len(machine)):
        process_time += sum(machine[i])
    total_makespan = best_makespan*len(machine)
    res = total_makespan - process_time
    return res


# ---- Main -----

# Start the stopwatch / counter
t1_start = process_time()

machine_order = sum_process_time(machine)
# print(machine_order)
makespan = find_all_order(machine, machine_order)
# print(makespan)
best_order = find_best_order(makespan, machine_order)
best_makespan = min(makespan)
idle_time = find_idle_time(best_makespan, machine)
print(f"Best order : {best_order}")
print(f"Makespan : {best_makespan}")
print(f"Idle time : {idle_time}")

# Stop the stopwatch / counter
t1_stop = process_time()
t1 = t1_stop-t1_start
print(f"Process start time : {t1_start}, stop time : {t1_stop}")
print(f"Total process time : {t1:.3f} seconds")
