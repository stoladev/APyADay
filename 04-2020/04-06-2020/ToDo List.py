# No tutorial to-do list
# Took me quite a while to figure this out, but it was good practice
# I need to start using PEP8 guidelines (or so I've heard)
# Tomorrow I will finish this to-do list tracker and make it save + load from a .txt


# VARIABLES
todo_list = []


# FUNCTIONS
# Menu with options and input for user's choice
def menu():
    print("1 = See todo list")
    print("2 = Add to todo list")
    print("3 = Remove from todo list")
    print()
    choice: str = input("Your choice: ")
    options(choice)


# Options displayed to user
def options(choice):
    if choice == "1":
        print("Here is your todo list:")
        print(list(todo_list))
        print()
        return menu()
    elif choice == "2":
        new_item = input("Please enter a new todo item: ")
        todo_list.append(new_item)
        print("New todo item '" + new_item + "' has been added.")
        print()
        return menu()
    elif choice == "3":
        print(list(todo_list))
        del_item = input("Item to remove (0-" + str(len(todo_list) - 1) + "): ")
        del (todo_list[int(del_item)])
        print()
        return menu()
    else:
        print("Incorrect choice. Please choose 1, 2, or 3.")
        print()
        return menu()


# Call
menu()
