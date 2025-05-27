import customtkinter as ctk

app = ctk.CTk()
app.title("Runs Counter!")
app.geometry("600x735")
app.configure(fg_color="black")

count_runs = [0]
count_wickets = [0]
count_overs = [0]

label_frame = ctk.CTkFrame(app,fg_color="black")
label_frame.pack(pady=20)
button_frame = ctk.CTkFrame(app,fg_color="black")
button_frame.pack(pady=20)


label_runs = ctk.CTkLabel(label_frame, text=str(count_runs[0]),
                          font=("Arial", 60),
                          text_color="white")
label_runs.grid(column=0, row=0, pady=20)

label_wickets = ctk.CTkLabel(label_frame, text=(f" - {str(count_wickets[0])}"),
                             font=("Arial", 60),
                             text_color="white")
label_wickets.grid(column=1, row=0, pady=20)

label_overs = ctk.CTkLabel(button_frame, text=str(count_overs[0]),
                          font=("Arial", 60),
                          text_color="white")
label_overs.grid(column=2, row=1, pady=20)

def one():
    if count_wickets[0] < 10:
        count_runs[0] += 1
        label_runs.configure(text=str(count_runs[0]))
    else:
        root = ctk.CTk()
        root.geometry("552x216")
        label = ctk.CTkLabel(root, text="All Batsman are out!!",
                             text_color="red",
                             font=("Arial", 50))
        label.pack(pady=50)
        root.mainloop()

def two():
    if count_wickets[0] < 10:
        count_runs[0] += 2
        label_runs.configure(text=str(count_runs[0]))
    else:
        root = ctk.CTk()
        root.geometry("552x216")
        label = ctk.CTkLabel(root, text="All Batsman are out!!",
                             text_color="red",
                             font=("Arial", 50))
        label.pack(pady=50)
        root.mainloop()

def three():
    if count_wickets[0] < 10:
        count_runs[0] += 3
        label_runs.configure(text=str(count_runs[0]))
    else:
        root = ctk.CTk()
        root.geometry("552x216")
        label = ctk.CTkLabel(root, text="All Batsman are out!!",
                             text_color="red",
                             font=("Arial", 50))
        label.pack(pady=50)
        root.mainloop()

def four():
    if count_wickets[0] < 10:
        count_runs[0] += 4
        label_runs.configure(text=str(count_runs[0]))
    else:
        root = ctk.CTk()
        root.geometry("552x216")
        label = ctk.CTkLabel(root, text="All Batsman are out!!",
                             text_color="red",
                             font=("Arial", 50))
        label.pack(pady=50)
        root.mainloop()

def five():
    if count_wickets[0] < 10:
        count_runs[0] += 5
        label_runs.configure(text=str(count_runs[0]))
    else:
        root = ctk.CTk()
        root.geometry("552x216")
        label = ctk.CTkLabel(root, text="All Batsman are out!!",
                             text_color="red",
                             font=("Arial", 50))
        label.pack(pady=50)
        root.mainloop()

def six():
    if count_wickets[0] < 10:
        count_runs[0] += 6
        label_runs.configure(text=str(count_runs[0]))
    else:
        root = ctk.CTk()
        root.geometry("552x216")
        label = ctk.CTkLabel(root, text="All Batsman are out!!",
                             text_color="red",
                             font=("Arial", 50))
        label.pack(pady=50)
        root.mainloop()

def wicket():
    if count_wickets[0] < 10:
        count_wickets[0] += 1
        label_wickets.configure(text=f" - {str(count_wickets[0])}")
    else:
        root = ctk.CTk()
        root.geometry("552x216")
        label = ctk.CTkLabel(root, text="All Batsman are out!!",
                             text_color="red",
                             font=("Arial", 50))
        label.pack(pady=50)
        root.mainloop()

def over():
    if count_wickets[0] < 10:
        count_overs[0] += 1
        label_overs.configure(text=str(count_overs[0]))
    else:
        root = ctk.CTk()
        root.geometry("552x216")
        label = ctk.CTkLabel(root, text="All Batsman are out!!",
                             text_color="red",
                             font=("Arial", 50))
        label.pack(pady=50)
        root.mainloop()

button1 = ctk.CTkButton(button_frame, text="+1", font=("Arial", 40), command=one, width=100, height=100)
button1.grid(row=0, column=1, padx=10, pady=10)

button2 = ctk.CTkButton(button_frame, text="+2", font=("Arial", 40), command=two, width=100, height=100)
button2.grid(row=0, column=3, padx=10, pady=10)

button3 = ctk.CTkButton(button_frame, text="+3", font=("Arial", 40), command=three, width=100, height=100)
button3.grid(row=1, column=1, padx=10, pady=10)

button4 = ctk.CTkButton(button_frame, text="+4", font=("Arial", 40), command=four, width=100, height=100)
button4.grid(row=1, column=3, padx=10, pady=10)

button5 = ctk.CTkButton(button_frame, text="+5", font=("Arial", 40), command=five, width=100, height=100)
button5.grid(row=2, column=1, padx=10, pady=10)
button6 = ctk.CTkButton(button_frame, text="+6", font=("Arial", 40), command=six, width=100, height=100)
button6.grid(row=2, column=3, padx=10, pady=10)

button7 = ctk.CTkButton(button_frame, text="Wicket", font=("Arial", 40), command=wicket, width=300, height=100)
button7.grid(row=3, column=2, padx=10, pady=10)

button8 = ctk.CTkButton(button_frame, text="Over", font=("Arial", 40), command=over, width=300, height=100)
button8.grid(row=2, column=2, padx=10, pady=10)

app.mainloop()
