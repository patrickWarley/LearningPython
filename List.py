def ListBasics():
    print("Tuple x List")
    print('  Tuple = immutable - List = mutable ')
    print('  Tuple = () List=[] ')
    print("Lists are just like arrays in javascript.")
    print('\nHow do we add a new element to a list?')
    print('  Using the method append. append(python) = push(javascript)')
    print('\nIn python we can add a new element in the middle of the array')
    print('  Using the method .insert(idx, element). We can do something like it')
    print('  with javascript using the method splice(idx, deletecount =0, element)')

def PlayingWithLists():
    lista = [1,2,3,4,5,6]
    print("  {}".format(lista))
    print('\nAdd element to the end: ')
    print('  list.append(7): ')
    lista.append(7)
    print("  {}".format(lista))
    print('\nAdd element in a spefic idx: ')
    print('  list.insert(2,8)')
    lista.insert(2,8)
    print("Lista:  {}".format(lista))
    print("\nThere are 2 ways to remove an element from an array")
    print('  del list[idx]')
    print('  list.remove(value)')
    print("What is the difference between the 2?")
    print("The first is like the splice method from javascript, and the second works like a find and then splice")
def ListsAreObjects():
    lista = [1,2,3]
    print("\nLists in python are objects so")
    print("  If I make list2 = list1 I'm just making a reference copy")
    print("  How de we make a copy of the values?")
    print("  Using the : (I'm calling it the range operator kkkk)")
    print("  list[startIdx : end] = end does not get in")
    print("  list2 = list1[:]")
    print("  I can also use it to copy part of the list")

ListBasics()
PlayingWithLists()
ListsAreObjects()