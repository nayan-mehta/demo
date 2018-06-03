import random
user = input("Enter username:  ")
print('welcome '+user)
print('Let\'s play Hangman')
print("Start.....")
a = ["python","hello","welcome","nice"]
w = random.choice(a)
word = list(w)
list1 =[]
#print(word)
lives = 5
length=0
print('_ '*len(w))
print('Enter any letter to fill these spaces')
while(lives>0 and len(w)!=length):
    guess = input()
    if guess not in list1:
        if(guess in word):
            n=word.count(guess)
            length = length+n
            list1.append(guess)
            print('spaces left=>')
            print('_ '*(len(w)-length))
        else:
            lives = lives - 1
            print("left lives: ", lives)
if(lives==0):
    print("You Loss")
    print("word was: "+w)
else:
    print("You win")