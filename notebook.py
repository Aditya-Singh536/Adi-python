import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
customtkinter.set_default_color_theme(
    "dark-blue"
)  # Themes: "blue" (default), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("500x500")
app.title("Notebook!")

label = customtkinter.CTkLabel(app, text="Enter the Notes here!", font=("Arial", 24))
label.pack(pady=20)

textbox = customtkinter.CTkTextbox(app, width=400, height=350, font=("Arial", 20))
textbox.insert(
    "0.0", "This is a CTkTextbox widget.\nYou can type here."
)  # insert text at line 0 character 0
textbox.insert("0.0", "new text to insert")  # insert at line 0 character 0
text = textbox.get("0.0", "end")  # get text from line 0 character 0 till the end
textbox.delete("0.0", "end")  # delete all text
textbox.configure(state="normal")  # configure textbox to be read-only
textbox.pack(padx=20, pady=20)

app.mainloop()
