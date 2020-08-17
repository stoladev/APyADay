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
# from pynput.keyboard import Key, Controller

# VARIABLES
todo_list = pickle.load(open('list', 'rb'))
# keyboard = Controller()
root = tk.Tk()
root.title("ToDo List")
root.resizable(False, False)
app_height = 300
app_width = 600
canvas = tk.Canvas(root, height=app_height, width=app_width, bg='white')
canvas.pack()


# FUNCTIONS
# INPUT FRAME CONTENTS
input_frame = tk.Frame(root, bg='#80c1ff')
input_frame.place(relx=0.5, rely=0.05, relwidth=0.9,
                  relheight=0.15, anchor='n')

new_entry = tk.Entry(input_frame, font='Iosevka')
new_entry.bind("<Return>", (lambda event: add_todo(new_entry.get())))
new_entry.place(relx=0.3625, rely=0.2, relwidth=0.685,
                relheight=0.55, anchor='n')

add_button = tk.Button(input_frame, text='Add ToDo', font='Iosevka',
                       command=lambda: add_todo(new_entry.get()))
add_button.place(relx=0.85, rely=0.2, relwidth=0.25,
                 relheight=0.55, anchor='n')

# LOWER FRAME CONTENTS
lower_frame = tk.Frame(root, bg='#80c1ff')
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.9,
                  relheight=0.7, anchor='n')

remove_button = tk.Button(lower_frame, text='Remove ToDo',
                          font='Iosevka', command=lambda: remove_todo())
remove_button.place(relx=0.4875, rely=0.845, relwidth=0.95,
                    relheight=0.125, anchor='n')

scrollbar = tk.Scrollbar(lower_frame)
scrollbar.pack(side='right', fill='y')
lb = tk.Listbox(lower_frame, yscrollcommand=scrollbar.set, font='Iosevka')

lb.place(relx=0.4875, rely=0.04, relwidth=0.95, relheight=0.775, anchor='n')
scrollbar.config(command=lb.yview)

for i in range(len(todo_list)):
    lb.insert('end', todo_list[i])


# FUNCTIONS
def save():  # Pickle the data
    pickle.dump(todo_list, open('list', 'wb'))
    open('list', 'rb').close()


def add_todo(entry):  # To do list entry adding and saving
    todo_list.append(entry)  # Adds entry to live list
    lb.insert('end', entry)  # Inserts entry to listbox
    save()  # Saves list
    new_entry.delete(0, 'end')  # Clears the entry field


def remove_todo():  # To do list entry removal and saving
    selection = lb.curselection()
    value = (lb.get(selection[0]))
    index = todo_list.index(value)
    del(todo_list[index])  # Deletes from pickled list
    lb.delete(selection[0])  # Deletes from the listbox
    save()  # Saves list
    # keyboard.press(Key.down)
    # keyboard.release(Key.down)


# CALLS
root.mainloop()
