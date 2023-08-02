# Write a Program to Print dictionary with age value is more than 45
age = [24, 24, 45, 44, 67]
names = ['Priya', 'Arun', 'Deepak', 'Gopal', 'raja']
d = {}
for i in range(0, len(age)):
    if age[i] >= age[2]:
        for j in range(i, i + 1):
            d.__setitem__(age[i], names[j])
print(d)
