d = {"a": 2, "b": 8, "c": 4}
# # #Output:{"a" : 2 ,"c": 4,"b" : 8}

output = {}
keys = list(d.keys())
values = list(d.values())
print(values)
for i in range(0, len(values)):
    for j in range(i, len(values)):
        if values[i] > values[j]:
            get = (values[i], values[j])
            (values[j], values[i]) = get
print(values)
print(keys)
for x in range(0, len(keys)):
    for y in range(x, x + 1):
        output.__setitem__(keys[x], values[y])

print(output)


# lst = [1, 2, 3]
#
# for i in range(0, len(lst)):
#     print(lst[i] ** lst[i])

# //tagName[@locator = "value "]
#
# tagName#idValue
# tagName.classValue
# tagName["attribute", ""]
