"""
Prompt the user to enter five names.
Store the names in a list.
Sort the list using the Bubble Sort algorithm.
Reverse the sorted list using a Python list method.
Print both the sorted and reversed lists.
"""
#asks user to input 5 names and stores them in a list
names = [input("enter a name: ") for _ in range(5)]
names = [name.lower() for name in names]
# starts bubble algorithm to sort the list
swapped = True
while swapped:
    swapped = False
    for i in range(len(names) - 1):
        if names[i] > names[i + 1]:
            names[i], names[i + 1] = names[i + 1], names[i]
            swapped = True

#prints sorted list
print("Sorted list:", names)
#reverses the sorted list and then prints the reversed list
names.reverse()
