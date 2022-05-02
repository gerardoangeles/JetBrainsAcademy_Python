def fizzBuzz(n):
    for n in range(1, n + 1):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
            
        elif n % 3 == 0 and n % 5 != 0:
            print("Fizz")

        elif n % 3 == 0 and n % 5 != 0:
            print("Fizz")
                
        elif n % 5 == 0 and n % 3 != 0:
            print("Buzz")
            
        else: #n % 3 == 0 or n % 5 == 0:
            print(n)


if __name__ == '__main__':
    n = int(input().strip())
    fizzBuzz(n)
