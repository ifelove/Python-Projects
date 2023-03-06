import random


def play():
    feedback = input("Enter r,s or p(r for rock,p for paper and s scissors):")
    computer = random.choice(["r", "s", "p"]);
    if feedback == computer:
        return "tie"
    if is_win(feedback, computer):
        return "You Won"
    return "You Lost"


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())
