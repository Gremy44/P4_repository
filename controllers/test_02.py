import tkinter
from unittest.util import strclass
import customtkinter  # <- import the CustomTkinter module
from tinydb import TinyDB

root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.geometry("400x240")
root_tk.title("Fenêtre test")

def champ(xrelx = .5, yrely = .5, placement = tkinter.CENTER):
    entry = customtkinter.CTkEntry(master=root_tk,
                                    width=120,
                                    height=25,
                                    corner_radius=10)
    entry.place(relx=xrelx, rely=yrely, anchor=placement)

    t_tape = entry.get
        
    return t_tape

def button_event():
    print("button pressed")
    print(entre_1)

button = customtkinter.CTkButton(master=root_tk,
                                 text="Add",
                                 command=button_event,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8)
button.place(relx=0.5, rely=0.8, anchor=tkinter.S)

entre_1 = champ()

root_tk.mainloop()
