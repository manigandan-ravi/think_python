t = [1,2,3,4]
t2 = [4,5,6]
t.extend(t2)

def add(t):
    sum=0
    for i in t:
        sum += i

    return sum

# print(add(t))
# t[0].capitalize()

print(t)