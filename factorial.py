def factorial(n):
    if not isinstance(n,int):
        print("Factorial is only defined for integers")
        return None
    elif n<0:
        print("Enter a positive integer")
        return None
    elif n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(6))
