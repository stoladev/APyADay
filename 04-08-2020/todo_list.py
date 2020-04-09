# No tutorial to-do list
# Took me quite a while to figure this out, but it was good practice
# I need to start using PEP8 guidelines (or so I've heard)

# todo translate functions to work with tkinter
# todo finish by end of tomorrow

# DONE todo add save and exit option
# DONE todo research on how to make gui for this app

# IMPORTS
import pickle
import tkinter as tk

# VARIABLES
todo_list = pickle.load(open('list', 'rb'))


# GUI VARIABLES
root = tk.Tk()
root.resizable(False, False)
app_height = 300
app_width = 600
canvas = tk.Canvas(root, height=app_height, width=app_width, bg='white')
canvas.pack()


# INPUT FRAME CONTENTS
input_frame = tk.Frame(root, bg='#80c1ff')
input_frame.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.15, anchor='n')

new_entry = tk.Entry(input_frame, font='Iosevka')
new_entry.place(relx=0.3625, rely=0.2, relwidth=0.685, relheight=0.55, anchor='n')

add_button = tk.Button(input_frame, text='Add ToDo', font='Iosevka', command=lambda: add_todo(new_entry.get()))
add_button.place(relx=0.85, rely=0.2, relwidth=0.25, relheight=0.55, anchor='n')

# LOWER FRAME CONTENTS
lower_frame = tk.Frame(root, bg='#80c1ff')
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.7, anchor='n')

remove_button = tk.Button(lower_frame, text='Remove ToDo', font='Iosevka')
remove_button.place(relx=0.4875, rely=0.845, relwidth=0.95, relheight=0.125, anchor='n')

scrollbar = tk.Scrollbar(lower_frame)
scrollbar.pack(side='right', fill='y')
my_list = tk.Listbox(lower_frame, yscrollcommand=scrollbar.set, font='Iosevka')

for line in range(10):
    my_list.insert('end', "This is line number " + str(line))

my_list.place(relx=0.4875, rely=0.04, relwidth=0.95, relheight=0.775, anchor='n')
scrollbar.config(command=my_list.yview)


# FUNCTIONS
# GUI test functions
def add_todo(entry):
    print("This is the entry: ", entry)


# Menu with options and input for user's choice
def menu():
    pickle.dump(todo_list, open('list', 'wb'))
    open('list', 'rb').close()
    print('1 = See todo list')
    print('2 = Add to todo list')
    print('3 = Remove from todo list')
    print('4 = Save and exit\n')
    choice: str = input('Your choice: ')
    options(choice)


# Options displayed to user
def options(choice):
    if choice == '1':
        print('\nHere is your todo list:')
        print(list(todo_list))
        print()
    elif choice == '2':
        new_item = input('Please enter a new todo item: ')
        todo_list.append(new_item)
        print('New todo item ' + new_item + ' has been added.')
        print()
    elif choice == '3':
        print(list(todo_list))
        del_item = input('Item to remove (0-' + str(len(todo_list) - 1) + '): ')
        del(todo_list[int(del_item)])
        print()
    elif choice == '4':
        print('Data saved. Exiting...')  # Data already saved from menu() call
        exit()
    else:
        print('Incorrect choice. Please choose 1, 2, or 3.\n')
    return menu()


# CALLS
root.mainloop()
menu()