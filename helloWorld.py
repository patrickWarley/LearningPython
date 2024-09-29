
def calcAge():
    x =input('Digite o ano atual e o seu ano de nascimento no formato (anoAtual:anoNascimento): ')
    #inclusive:exlusive
    anoNascimento = int(x[5:])
    anoAtual =int(x[0:4])
    idade =anoAtual-anoNascimento
    print('Sua idade e {}'.format(idade))

    if(idade > 18):
        print('Voce ja pode dirigir!')
    else:
        print('Voce e um bebe safadao!')

# Python uses elif instead of elseif

#for variable in range(initialValue for i, final Value for i, increment)
#The end value I think is always exclusive
def printAHundredTimes():
    for i in range(0,100,1):
        print('Oh my god this is easier?')


#lets go through a string
#to make a parameter optional you just define a default value
def printStr(x=0):
    str = "vai tomar no cu!"
    for i in range(0, len(str), 1):
        print("{} {}".format(str[i], x))

#let's deal with exceptions
def exceptionsTest():
    try:
        return 10/0
    #I can get specific errors 
        #And Can I get any error? yes I can I just don't write anything after except
    except :
        print('Deu merda')
    finally:
        print('Deu merda mas olha só da para sair de boa na lagoa!')

#we can create lambda functions
#they can span multiple line you just need to put the 
#lambda or it's contents inside parentheses
doubleIt = lambda x:x*2
doubleItMultipleLine =(
    lambda x:
         x*2
)
doubleItMultipleLineButDifferent = lambda x:(
    x*2
)
#all three work

#tuplas = immutable arrays, fuck it!
def playingWithTuplas():
    tuplaTest = ('patrick', 'warley')
    tuplaTest2 = ('veronica', 'warley')
    for item in tuplaTest:
        print(item)
    #that's gonna print a range
    print(tuplaTest[0:1])
    #what is gonna happen below
    #the range selection return a tuple so it cannot be changed
    test = tuplaTest[0:1]
    #we can concatenate tuples just like strings
    print(tuplaTest+tuplaTest2)

playingWithTuplas()
