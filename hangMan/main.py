import random
import string
from words import words

def get_valid_word(words):
    word=random.choice(words);
    while "-" in word or " " in word:
        word=random.choice(words)
    return word



def hangMan():
    word=get_valid_word(words)
    word_letters=set(word) #letter in the word
    alphabet=set(string.ascii_uppercase)
    used_letters=set() #user guess
    lives=6
    #getting user input
    while len(word_letters) > 0 and lives > 0:
        print(f"You have{lives} lives left..You have used this letter before:",''.join(used_letters))
        word_list=[letter if letter in used_letters else '-' for letter in word]
        print("Current word :", ''.join(word_list))
        user_letter=input('guess something:').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in  word_letters:
                word_letters.remove(user_letter)
            else:
                lives=lives-1
                print("Letter is not in word")
        elif user_letter in used_letters:
            print("You have already used this letter")
        else:
            print("You have enter a wrong letter")

    if lives == 0:
        print("You died")
    print(f'You guess the word', word, '!!!')




hangMan()
#user_input=input("Type Something")
#print(user_input)




#print(words)