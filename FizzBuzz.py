for i in range(100):
    n = i+1
    if n%15 == 0:
        print(n,'Fizz Buzz')
    elif n%3 == 0:
        print(n,'Fizz')
    elif n%5 == 0:
        print(n,'Buzz')
    else:
        print(n)
    