import string
from collections import Counter

word='hello'
lives = 4
letters = list(string.ascii_lowercase)
guess = input('Enter a guess:')
cor_guess_list= []

while lives > 0:
    letters.remove(guess)
    flag = 0
    for i in word:
        if guess == i:
            print(i)
            cor_guess_list.append(guess)
            flag = 1
        elif i in cor_guess_list:
            print(i)
        else:
            print('_')
    # print('Correct guess list', cor_guess_list)
    if not flag:
        lives = lives -1

    print('Number of lives', lives)
    if lives == 0:
        break

    final_guess= ''.join(cor_guess_list)
    print('Final guess',final_guess)

    if Counter(final_guess) == Counter(word): #hello ehllo
        break
    guess = input('Enter a guess:')
    if guess not in letters:
        guess = input('Enter guess again:')


if lives == 0:
    print('LOSERRR... YOU HAVE BEEN HANGED')

if lives !=0:
    print('Winner winner chicken dinner')
