lst = [12, 14, 3, 2, 56, 54, 2, 45]
print("Before Sorting :: ", lst)

for i in range(0, len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            get = (lst[i], lst[j])
            (lst[j], lst[i]) = get
print("After Sorting :: ", lst)

print("2nd Largest Num is ::", lst[len(lst) - 2])
