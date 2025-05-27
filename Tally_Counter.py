import customtkinter as ctk


app = ctk.CTk()
app.title("Tally Counter!")
app.geometry("500x400")
app.configure(fg_color="black")

count = [0]

label = ctk.CTkLabel(app, text=str(count[0]),
                     font=("Arial", 60),
                     text_color="white")
label.pack(pady=20)

def add(): 
    count[0] += 1
    label.configure(text=str(count[0]))

def minus():
    if count[0] > 0:
        count[0] -= 1
        label.configure(text=str(count[0]))
    else:
        root = ctk.CTk()
        root.geometry("300x150")
        error_label = ctk.CTkLabel(root, text="Can't go in negative digits!!",
                                   text_color="red",
                                   font=("Arial", 20))
        error_label.pack(pady=50)
        root.mainloop()

def cls():
    count[0] = 0
    label.configure(text=str(count[0]))

button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=20)

button = ctk.CTkButton(button_frame, text="+",
                       corner_radius=50,
                       font=("Arial", 100),
                       command=add,
                       height=150,
                       width=150,
                       fg_color="aqua",
                       text_color="black",
                       hover_color="blue")
button.pack(side="left", padx=10)

button2 = ctk.CTkButton(button_frame, text="-",
                        corner_radius=50,
                        font=("Arial", 100),
                        command=minus,
                        height=150,
                        width=150,
                        fg_color="aqua",
                        text_color="black",
                        hover_color="blue")
button2.pack(side="left", padx=10)

button3 = ctk.CTkButton(app, text="Reset",
                        corner_radius=25,
                        text_color="black",
                        font=("Arial", 15),
                        command=cls,
                        height=50,
                        width=100,
                        fg_color="orange",
                        hover_color="red",)
button3.pack(pady=10)

app.mainloop()
