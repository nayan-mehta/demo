#print "Welcome to Hangman!!! Prepare to die"
# variables lives, word , guess

# hello _ _ _ _ _
'''
while(lives>0)
    guess =input("Enter a letter")
    guess ka list
    if(guess not in word):
        lives-=1

    for (Its part of the length of word)
        if iterator in guess
            print guess
        else:
            print "_"


 lives=6
 hello _ _ _ _ _
 h _ _ _ _
 3

'''

print "hangman game"
lives=6
word="github"
n="_"
l=list(n*len(word))
print "\n",l,
count=0
while(lives>0):
    guess=raw_input("\n enter the guess")
    if guess not in word:
        lives=lives-1
        print "now lives are =",lives
    for i in word:
        if(guess==i):
            print guess
            l[word.index(guess)]=guess
            print l
            count=count+1
    if count==len(word):
        print "you win"
        break
if(lives==0):
    print "you lose"




    
