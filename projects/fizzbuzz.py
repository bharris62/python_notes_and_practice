# Fizz buzz, using input().  Added a while loop that will keep the user in the game until they supply a valid integer.

while True:
    try:
        n = int(input("Pick a number to be buzzed:  "))
        for i in range(1, n+1):
            if i % 15 == 0:
                print("FizzBuzz!")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)
        break

    except ValueError:
        print("that is not a valid integer, try again.")
