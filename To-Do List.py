import customtkinter as ctk
import CTkListbox as ctkLb
import CTkMessagebox as ctkMb

app = ctk.CTk()
app.geometry("400x600x400")
app.title("To-Do List")
app.iconbitmap("to-do-list.ico")
app.config(bg="#FFCA3A")

Label1 = ctk.CTkLabel(app, text="To-Do List", bg_color="#FFCA3A", font=("Roboto Medium", 35))
Label1.pack()

Entry1 = ctk.CTkEntry(app, width=250, height=35, bg_color="#FFCA3A", text_color="#FFCA3A")
Entry1.place(x=75, y=145)


def Add_Task():
    task = Entry1.get()
    if task:
        Listbox1.insert(ctk.END, task)
        Entry1.delete(0, ctk.END)
    else:
        message = ctkMb.CTkMessagebox(app, title="Error", message="You Need To Enter Task First.", icon="cancel",
                                      option_focus="")

def Remove_Task():
    selected = Listbox1.curselection()
    if selected == 0 or selected:
        Listbox1.delete(selected)
    elif not selected:
        message = ctkMb.CTkMessagebox(app, title="Info", message="You Need To Select Task First To Remove.",
                                      icon="info", option_focus="")

def Done_Task():
    selected = Listbox1.curselection()
    task = Listbox1.get(selected)
    if selected == 0 or selected:
        Listbox1.delete(selected)
        Listbox1.insert(ctk.END, f"{task}️✔️")
    else:
        message = ctkMb.CTkMessagebox(app, title="Warning", message="You Need To Select Task Who You Finished it.",
                                      icon="warning", option_focus="")



Button1 = ctk.CTkButton(app, text="Add Task", fg_color="#8AC926", bg_color="#FFCA3A", font=("Roboto Medium", 24),
                        command=lambda: Add_Task())
Button1.place(x=50, y=100)

Button2 = ctk.CTkButton(app, text="Remove Task", fg_color="#FF595E", bg_color="#FFCA3A", font=("Roboto Medium", 24),
                        command=lambda: print(Remove_Task()))
Button2.place(x=200, y=100)

Listbox1 = ctkLb.CTkListbox(app, width=225, height=250, text_color="#FFCA3A", font=("Roboto Medium", 16))
Listbox1.place(x=75, y=225)

Button3 = ctk.CTkButton(app, text="Done", fg_color="#6A4C93", bg_color="#FFCA3A", font=("Roboto Medium", 24),
                        command=lambda: print(Done_Task()))
Button3.place(x=130, y=500)

app.mainloop()