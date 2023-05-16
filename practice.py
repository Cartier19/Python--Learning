## Print 1 to 100
## Multiples of 3 = Fizz
## Multiples of 5 = Buzz
## Multiples of 3&5 = FizzBuzz

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
         print(i)