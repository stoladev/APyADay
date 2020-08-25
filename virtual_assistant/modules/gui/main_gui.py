import tkinter as tk
from commands.command_handler import check_cmnd

window_height = 200
window_width = 500
btn_txt = "Send Command"

root = tk.Tk()
canvas = tk.Canvas(root, height=window_height, width=window_width, bg="white")
canvas.pack()

upper_frame = tk.Frame(root, bg="#80c1ff")
upper_frame.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.15, anchor="n")

lower_frame = tk.Frame(root, bg="#80c1ff")
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.7, anchor="n")

cmnd_field = tk.Entry(upper_frame)
cmnd_field.place(relx=0.3625, rely=0.2, relwidth=0.685, relheight=0.55, anchor="n")
cmnd_field.bind("<Return>", (lambda event: btn_cmnd()))

cmnd_btn = tk.Button(upper_frame, text=btn_txt, command=lambda: btn_cmnd())
cmnd_btn.place(relx=0.85, rely=0.2, relwidth=0.25, relheight=0.55, anchor="n")



def btn_cmnd():
    return check_cmnd(cmnd_field.get())
