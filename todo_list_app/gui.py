"""Todo list application that saves via pickle.
Requires Iosevka font."""

import pickle
import tkinter as tk
from pynput.keyboard import Key, Controller

# General settings.
root = tk.Tk()
root.title("ToDo List")
root.resizable(False, False)
APP_HEIGHT = 300
APP_WIDTH = 600
todo_list = pickle.load(open('list', 'rb'))
keyboard = Controller()

# Program canvas settings.
canvas = tk.Canvas(root, height=APP_HEIGHT, width=APP_WIDTH, bg='white')
canvas.pack()

# Upper frame settings.
upper_frame = tk.Frame(root, bg='#80c1ff')
upper_frame.place(relx=0.5,
                  rely=0.05,
                  relwidth=0.9,
                  relheight=0.15,
                  anchor='n')

# Lower frame settings.
lower_frame = tk.Frame(root, bg='#80c1ff')
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.7, anchor='n')

# Entry field settings.
new_entry = tk.Entry(upper_frame, font='Iosevka')
new_entry.place(relx=0.3625,
                rely=0.2,
                relwidth=0.685,
                relheight=0.55,
                anchor='n')

# Adding/removing tasks via button and <Enter>.
add_task_button = tk.Button(upper_frame,
                            text='Add ToDo',
                            font='Iosevka',
                            command=lambda: add_todo(new_entry.get()))
add_task_button.place(relx=0.85,
                      rely=0.2,
                      relwidth=0.25,
                      relheight=0.55,
                      anchor='n')
delete_button = tk.Button(lower_frame,
                          text='Remove ToDo',
                          font='Iosevka',
                          command=lambda: remove_todo(lb.curselection()))
delete_button.place(relx=0.4875,
                    rely=0.845,
                    relwidth=0.95,
                    relheight=0.125,
                    anchor='n')
new_entry.bind("<Return>", (lambda event: add_todo(new_entry.get())))

# Scrollbar and listbox settings.
scrollbar = tk.Scrollbar(lower_frame)
scrollbar.pack(side='right', fill='y')
lb = tk.Listbox(lower_frame, yscrollcommand=scrollbar.set, font='Iosevka')
lb.place(relx=0.4875, rely=0.04, relwidth=0.95, relheight=0.775, anchor='n')
scrollbar.config(command=lb.yview)

# Loads list from pickle file.
for i, _ in enumerate(todo_list):
    lb.insert('end', todo_list[i])


def save():
    """Pickles data.
    """

    pickle.dump(todo_list, open('list', 'wb'))
    open('list', 'rb').close()


def add_todo(entry):
    """Adds todo list items.

    Args:
        entry: Task to be added from the textbox.
    """

    todo_list.append(entry)
    lb.insert('end', entry)
    save()

    new_entry.delete(0, 'end')


def remove_todo(selection):
    """Removes selected list item.

    Args:
        selection: The currently selected list item.
    """

    value = (lb.get(selection[0]))
    index = todo_list.index(value)

    del todo_list[index]
    lb.delete(selection[0])

    save()

    keyboard.press(Key.down)
    keyboard.release(Key.down)


root.mainloop()
