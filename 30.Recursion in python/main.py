var = int(input("Enter the number: "))

def fibonacci(a, b, c):
    if c >= var:
        return 
    else:
        print(a, end=", ")
        fibonacci(b, a + b, c + 1)

fibonacci(0, 1, 0)
