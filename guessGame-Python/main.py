import random;

def guess(x):
    random_number=random.randint(1,x);
    guess=0
    while guess != random_number:
        guess=int(input(f'Enter a number between 1 and {x}:'))
        print(guess)
        print("the random number generated is {}".format(random_number))

guess(10)









