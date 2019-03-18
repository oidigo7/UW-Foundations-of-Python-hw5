# -------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   Obi Idigo
# Date:  March 11, 2018
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   <Obi Idigo>, ???, Added code to complete assignment 5
# https://www.tutorialspoint.com/python/python_dictionary.htm
# -------------------------------------------------#

# -- Data --#
# declare variables and constants
# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

# -- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

# -- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.

# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo items to user

# Step 4
# Add a new item to the list/Table

# Step 5
# Remove a new item to the list/Table

# Step 6
# Save tasks to the ToDo.txt file

# Step 7
# Exit program
# -------------------------------

objFileName = "C:\_PythonClass\Todo.txt"
strData = ""
dicRow = {}
lstTable = []

# Step 1 - Load data from a file
# When the program starts, load each "row" of data
# in "ToDo.txt" into a python Dictionary.
# Add the each dictionary "row" to a python list "table"

with open("Todo.txt", "r") as f:
    strData = f.readlines()
    print(strData)

    dicRow = {}

for x in strData:
    task = x.split(".")[0].strip()
    priority = x.split(".")[1].strip()

    dicRow[task] = priority

print(dicRow)


# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)

    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()  # adding a new line

    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        for task, priority in dicRow.items():
            print(task,priority)

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        new_task = input("Please enter a new task name: ").title()
        new_priority = input("Please enter the priority of your new task, either high or low: ").lower()

        dicRow[new_task] = new_priority
        print(dicRow)

    # Step 5 - Remove a new item to the list/Table
    elif (strChoice == '3'):
        remove_task = input("Please enter the task name to remove: ").title()
        if remove_task in dicRow.keys():
            del dicRow[remove_task]

    # Step 6 - Save tasks to the ToDo.txt file
    elif (strChoice == '4'):
        with open("Todo.txt", "w") as f:
            for task, priority in dicRow.items():
                f.write("{}.{}\n".format(task,priority))

    elif (strChoice == '5'):
        break  # and Exit the program

