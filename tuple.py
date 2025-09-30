"""
 Create a tuple named programming_classes with these classes: 
 'Intro to Python', 'Advanced Python', 'Database Essentials', 'Web Development Basics', 
 'Data Structures in Python', 'Web Design Fundamentals'.
Write a program that uses a for loop to print each class in the tuple.
Use the len function to print how many courses are in the tuple.
Make sure to use a main function for this program.
"""
# main function that contains the 
def main():
    # tuple of programming classes
    programming_classes = (
        'intro to python',
        'advanced python',
        'database essentials',
        'web development basics',
        'data structures in python',
        'web design fundamentals'
    )
    # for loop to print each class in the tuple and also the number of classes
    for course in programming_classes:
        print(course)
    print(f"There are {len(programming_classes)} courses available.")
# calling the main function
main()
