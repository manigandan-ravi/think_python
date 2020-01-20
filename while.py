


def countdown(n):
    while n>0:
        print(n)
        n -=1
    print("Blast off")

while True:
    line = input("> ")
    if line == 'done':
        break
    else:
        print (line)
print (line)

