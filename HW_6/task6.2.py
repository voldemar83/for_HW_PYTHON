values = [1, 2, 3, 6, 9, 3, 2, 1]
min_v = 3
max_v = 7

indx = []

for i in range(len(values)):
    if values[i] >= min_v and values[i] <= max_v:
        indx.append(i)

print(indx)