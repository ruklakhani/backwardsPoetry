<<<<<<< HEAD
import random as random
=======
import random 
>>>>>>> 377ef537196a508bd8522c5fd1c3cdc384a29655

poem ="""Our generation will be known for nothing.
Never will anybody say,
We were the peak of mankind.
That is wrong, the truth is
Our generation was a failure.
Thinking that
We actually succeeded
Is a waste. And we know
Living only for money and power
Is the way to go.
Being loving, respectful, and kind
Is a dumb thing to do.
Forgetting about that time,
Will not be easy, but we will try.
Changing our world for the better
Is something we never did.
Giving up
Was how we handled our problems.
Working hard
Was a joke.
We knew that
People thought we couldn’t come back
That might be true,
Unless we turn things around"""

poems = poem.split("\n")
<<<<<<< HEAD

#TODO: get a list of strings that contains lines of poem

def printBackwards(poems):
    ''' Arrange poem backwards'''
    index = len(poems)
    poems.reverse()

    for i in poems:
        print(f'{str(index)} {i}')
        index -= 1


def printRandom(poem_lines_list):
    ''' Arrange poem random  '''
    for i in poems:
        linesRandom = random.randint(0, (len(poems)-1)) 
        print(poems[linesRandom])

 
def rearrange():
    ''' This function will print 3 random lines'''
    for poem in poems:
        print(poem[::-1])
    

#TODO: get a list of strings that contains lines of poem
#Use lines = poem.split("\n")
 
 
#Testing code
printBackwards(poems)
printRandom(poems)
rearrange()
=======
>>>>>>> 377ef537196a508bd8522c5fd1c3cdc384a29655
