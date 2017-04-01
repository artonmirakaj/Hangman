import random
import turtle

wordList = ['python','programming','university','computer','ganis']
word = list(wordList[random.randint(0,len(wordList) - 1)])
displayWord = list('-' * len(word))

guesses = 6
count = 0
answers = 0

lettersUsed = []
wordFound = False

def initialize():
    turtle.left(180)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(20)

    turtle.penup()
    turtle.home()
    turtle.backward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)

def checkLetter(a):
    isGood = False
    while isGood == False:
        if a.isalpha() == False:
            a = raw_input("not a letter, try again: ")
            a = a.lower()
        elif len(a) != 1:
            a = raw_input("one letter at a time: ")
            a = a.lower()
        elif a in lettersUsed:
            a = raw_input("You already used that letter:  ")
            a = a.lower()
        else:
            lettersUsed.append(a)
            isGood = True
            print
            return a

def checkWord(b):
    global guesses, count, answers
    if b in word:
        i = 0
        for item in word:
            if word[i] == b:
                displayWord[i] = b
                answers = answers + 1
            i = i + 1
        print " %d is in the word" % (answers)
    else:
        print "letter is not in the word"
        guesses = guesses - 1

    print displayWord

    answers = 0
    count = count + 1

def hangMan(c):
    if c == 5:
        turtle.penup()
        turtle.goto(-25,180)
        turtle.right(180)
        turtle.pendown()
        turtle.circle(30)
        turtle.left(180)
    if c == 4:
        turtle.penup()
        turtle.goto(-25,180)
        turtle.right(90)
        turtle.forward(60)
        turtle.pendown()
        turtle.forward(30)
        turtle.left(90)
    if c == 3:
        turtle.penup()
        turtle.goto(-25,180)
        turtle.right(90)
        turtle.forward(70)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(20)
    if c == 2:
        turtle.penup()
        turtle.goto(-25,180)
        turtle.right(90)
        turtle.forward(70)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(20)
        turtle.left(180)
    if c == 1:
        turtle.penup()
        turtle.goto(-25,180)
        turtle.right(90)
        turtle.forward(90)
        turtle.pendown()
        turtle.left(45)
        turtle.forward(20)
        turtle.left(45)
    if c == 0:
        turtle.penup()
        turtle.goto(-25,180)
        turtle.right(90)
        turtle.forward(90)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(20)
        turtle.left(135)

    turtle.penup()
    turtle.goto(-100,-100)


initialize()

print "Guess A Word"
print "The word is %d letters long and you will have %d guesses ..." % (len(word), guesses)

while wordFound == False and guesses > 0:
    print "-" * 50
    print "Guess #%d" % (count + 1)
    print

    turtle.write("Letters Used: " + str(lettersUsed))
    turtle.right(90)
    turtle.forward(20)
    turtle.write("Word: " + str(displayWord))
    turtle.backward(20)
    turtle.left(90)

    letter = raw_input("enter a letter: ")
    letter = letter.lower()

    checkWord(checkLetter(letter))

    for i in range(6):
        turtle.undo()

    hangMan(guesses)

    if '-' not in displayWord:
        wordFound = True


if wordFound == True:
    print "You found the secret word"
    turtle.write("winner",font=(2000))
else:
    print "You have ran out of guesses"
    turtle.write("You Lost",font=(2000))

turtle.exitonclick()
