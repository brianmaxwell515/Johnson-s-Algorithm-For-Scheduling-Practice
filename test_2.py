# machine = [[6, 17, 3, 10, 5],
#            [10, 14, 10, 26, 15],
#            [1, 17, 13, 31, 13],
#            [13, 12, 17, 20, 15]]

machine = [[6, 17, 3, 10, 5],
           [10, 14, 10, 26, 15],
           [1, 17, 13, 31, 13],
           [13, 12, 17, 20, 15]]

# machine = [6, 17, 3, 10, 5]
res = 0
for i in range(len(machine)):
    res += sum(machine[i])

print(res)