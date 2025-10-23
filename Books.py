"""
In this assignment, you will create a Python program that collects book titles from a user. 
Your program should use a while loop to prompt the user to enter a total of 10 book titles. 
Follow these steps to complete your assignment:

"""
# main function that runs the program
def main():
    # empty list that takes the users input and stores them
    books = []
    # count value that goes up when user inputs a new book name
    count = 0
    # while loop that keeps asking the user for a book title until count is 10
    while count < 10:
        title = input(f"Please enter the name of book {count + 1} " )
        title = title.title()
        books.append(title)
        count += 1
    sorted_books = sorted(books)
    print("Here are your book titles sorted in order:")
    # for loop that prints out the sorted book names
    for book in sorted_books:
     print(book)


main()
