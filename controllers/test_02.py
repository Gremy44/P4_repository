import tkinter
import customtkinter

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"

app = customtkinter.CTk()
app.geometry("400x580")
app.title("Player profile creation.py")


def button_callback():
    mes_entrees = []
    mes_entrees.append(entry_1.get())
    print(mes_entrees)
    
    return entry_1.get


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT)
label_1.pack(pady=12, padx=10)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="CTkEntry",justify=tkinter.LEFT)
entry_1.pack(pady=12, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1,text="Valider", command=button_callback)
button_1.pack(pady=12, padx=10)

mes_entrees = []
mes_entrees.append(entry_1.get())
print(mes_entrees)

app.mainloop()
