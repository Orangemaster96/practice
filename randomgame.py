import random
number = random.randint(1,10)
print(number)
def guess_game():
    guess = int(input('pick a number from 1-10: '))
    if guess == number:
        print("you're a genius")
    else:
        print('Hah fail, try again')
        guess_game()

guess_game()

