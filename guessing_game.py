import random

rng = [1, 2, 3, 4, 5, 6, 7, 8, 9]
points = 0
tries = 0

while True:
    num = random.choice(rng)
    print("The number has been generated.\nGuess the number (1 to 9). Or 0 to quit.")
    guess = int(input("Guess: "))
    if guess in rng:
        if guess == num:
            print("Right Guess. Num is "+str(num)+"!\nReceived a point.")
            points += 1
            tries += 1
            continue
        elif guess - num > 5:
            print("Too High! Num is "+str(num)+".")
            tries += 1
            continue
        elif num - guess > 5:
            print("Too Low! Num is "+str(num)+".")
            tries += 1
            continue
        else:
            tries += 1
            print("Wrong Guess! Number is "+str(num)+".")

    elif guess == 0:
        print("Your Score "+str(points)+" / "+str(tries))
        exit()
    else:
        print("Invalid Input! Try Again.")
        continue
