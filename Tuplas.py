#Tuplas are immutable
#We can declare a parameter as a tuple to do it we just put the * before
#the name of the parameter
#example
#It works like the 3 dots in javascript
def tupleParam(*test):
    print('\n# 3 dots javascript is does something like the * in python')
    print('the * is called the splat operator\n')
    print(test)
    print('\n# the thing is that if we pass a tuple to a function that has a param with the *name format')
    print('#the tuple will just be an item inside another tuple')
#can we concat a empty tuple with one that has some items?
def concatEmptyWithFull():
    print('\n# empty tuple + one with some elements')
    empty=()
    full=('patrick', 'adrielle')

    print(empty+full)
    print('# We can use it to make a copy of the tuple or to add new elements')

def usingSplatToMixTuples():
    first =('patrick', 'warley')
    second =(1,2,4,5,6)
    print("\nfirst tuple : {}\n second tuple:{}".format(first, second))
    print("\nfirst+second: {}".format(first+second))
    print("\nsame result as first+second but in a new tuple using the splat operator\n")
    print("(*first, *second): {}".format((*first, *second)))

concatEmptyWithFull()

#here the list of params you be considered a tuple right
tupleParam(1,2,3,4,5,6,7,8)

#but what happens when I pass a tuple?
test = ('patrick', 'warley')
tupleParam(test)
# It does not spread the items of the tuple

usingSplatToMixTuples()
