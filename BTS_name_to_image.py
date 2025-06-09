import customtkinter as ctk
from PIL import Image, ImageTk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


def image_rm():
    # Create a new window
    new_window = ctk.CTkToplevel(app)
    new_window.title("RM")
    new_window.geometry("165x175")

    try:
        # For a standard image file
        my_image = Image.open(
            "/home/aditya-singh536/Aditya-Singh536/BTS_name_to_image/rm.png"
        )
        # Convert to a CustomTkinter-compatible format
        my_ctk_image = ctk.CTkImage(
            light_image=my_image,
            dark_image=my_image,  # Use same for light/dark mode if not specified
            size=(100, 100),
        )  # Specify desired display size
    except FileNotFoundError:
        print(
            "Error: 'your_image.png' not found. Please place an image file in the script directory or provide the full path."
        )
    # Create a label to display the image
    label = ctk.CTkLabel(new_window, text="RM", image=my_ctk_image, compound="top")
    label.pack(pady=20, padx=20)


def image_jin():
    # Create a new window
    new_window = ctk.CTkToplevel(app)
    new_window.title("Jin")
    new_window.geometry("165x175")

    try:
        # For a standard image file
        my_image = Image.open(
            "/home/aditya-singh536/Aditya-Singh536/BTS_name_to_image/jin.png"
        )
        # Convert to a CustomTkinter-compatible format
        my_ctk_image = ctk.CTkImage(
            light_image=my_image,
            dark_image=my_image,  # Use same for light/dark mode if not specified
            size=(100, 100),
        )  # Specify desired display size
    except FileNotFoundError:
        print(
            "Error: 'your_image.png' not found. Please place an image file in the script directory or provide the full path."
        )
    # Create a label to display the image
    label = ctk.CTkLabel(new_window, text="Jin", image=my_ctk_image, compound="top")
    label.pack(pady=20, padx=20)


def image_suga():
    # Create a new window
    new_window = ctk.CTkToplevel(app)
    new_window.title("Suga")
    new_window.geometry("165x175")

    try:
        # For a standard image file
        my_image = Image.open(
            "/home/aditya-singh536/Aditya-Singh536/BTS_name_to_image/suga.png"
        )
        # Convert to a CustomTkinter-compatible format
        my_ctk_image = ctk.CTkImage(
            light_image=my_image,
            dark_image=my_image,  # Use same for light/dark mode if not specified
            size=(100, 100),
        )  # Specify desired display size
    except FileNotFoundError:
        print(
            "Error: 'your_image.png' not found. Please place an image file in the script directory or provide the full path."
        )
    # Create a label to display the image
    label = ctk.CTkLabel(new_window, text="Suga", image=my_ctk_image, compound="top")
    label.pack(pady=20, padx=20)


def image_jhope():
    # Create a new window
    new_window = ctk.CTkToplevel(app)
    new_window.title("J-Hope")
    new_window.geometry("165x175")

    try:
        # For a standard image file
        my_image = Image.open(
            "/home/aditya-singh536/Aditya-Singh536/BTS_name_to_image/jhope.png"
        )
        # Convert to a CustomTkinter-compatible format
        my_ctk_image = ctk.CTkImage(
            light_image=my_image,
            dark_image=my_image,  # Use same for light/dark mode if not specified
            size=(100, 100),
        )  # Specify desired display size
    except FileNotFoundError:
        print(
            "Error: 'your_image.png' not found. Please place an image file in the script directory or provide the full path."
        )
    # Create a label to display the image
    label = ctk.CTkLabel(new_window, text="J-Hope", image=my_ctk_image, compound="top")
    label.pack(pady=20, padx=20)


def image_jimin():
    # Create a new window
    new_window = ctk.CTkToplevel(app)
    new_window.title("Jimin")
    new_window.geometry("165x175")

    try:
        # For a standard image file
        my_image = Image.open(
            "/home/aditya-singh536/Aditya-Singh536/BTS_name_to_image/jimin.png"
        )
        # Convert to a CustomTkinter-compatible format
        my_ctk_image = ctk.CTkImage(
            light_image=my_image,
            dark_image=my_image,  # Use same for light/dark mode if not specified
            size=(100, 100),
        )  # Specify desired display size
    except FileNotFoundError:
        print(
            "Error: 'your_image.png' not found. Please place an image file in the script directory or provide the full path."
        )
    # Create a label to display the image
    label = ctk.CTkLabel(new_window, text="Jimin", image=my_ctk_image, compound="top")
    label.pack(pady=20, padx=20)


def image_v():
    # Create a new window
    new_window = ctk.CTkToplevel(app)
    new_window.title("V")
    new_window.geometry("165x175")

    try:
        # For a standard image file
        my_image = Image.open(
            "/home/aditya-singh536/Aditya-Singh536/BTS_name_to_image/v.png"
        )
        # Convert to a CustomTkinter-compatible format
        my_ctk_image = ctk.CTkImage(
            light_image=my_image,
            dark_image=my_image,  # Use same for light/dark mode if not specified
            size=(100, 100),
        )  # Specify desired display size
    except FileNotFoundError:
        print(
            "Error: 'your_image.png' not found. Please place an image file in the script directory or provide the full path."
        )
    # Create a label to display the image
    label = ctk.CTkLabel(new_window, text="V", image=my_ctk_image, compound="top")
    label.pack(pady=20, padx=20)


def image_jungkook():
    # Create a new window
    new_window = ctk.CTkToplevel(app)
    new_window.title("Jungkook")
    new_window.geometry("165x175")

    try:
        # For a standard image file
        my_image = Image.open(
            "/home/aditya-singh536/Aditya-Singh536/BTS_name_to_image/jungkook.png"
        )
        # Convert to a CustomTkinter-compatible format
        my_ctk_image = ctk.CTkImage(
            light_image=my_image,
            dark_image=my_image,  # Use same for light/dark mode if not specified
            size=(100, 100),
        )  # Specify desired display size
    except FileNotFoundError:
        print(
            "Error: 'your_image.png' not found. Please place an image file in the script directory or provide the full path."
        )
    # Create a label to display the image
    label = ctk.CTkLabel(
        new_window, text="Jungkook", image=my_ctk_image, compound="top"
    )
    label.pack(pady=20, padx=20)


app = ctk.CTk()
app.title("BTS name to image!!")
app.geometry("300x400")


frame = ctk.CTkFrame(app, fg_color="#dd0531")
frame.pack(pady=20, padx=20, fill="both", expand=False)

bt1 = ctk.CTkButton(frame, text="RM", command=image_rm)
bt1.pack(pady=10, padx=10)

bt2 = ctk.CTkButton(frame, text="Jin", command=image_jin)
bt2.pack(pady=10, padx=10)

bt3 = ctk.CTkButton(frame, text="Suga", command=image_suga)
bt3.pack(pady=10, padx=10)

bt4 = ctk.CTkButton(frame, text="J-Hope", command=image_jhope)
bt4.pack(pady=10, padx=10)

bt5 = ctk.CTkButton(frame, text="Jimin", command=image_jimin)
bt5.pack(pady=10, padx=10)

bt6 = ctk.CTkButton(frame, text="V", command=image_v)
bt6.pack(pady=10, padx=10)

bt7 = ctk.CTkButton(frame, text="Jungkook", command=image_jungkook)
bt7.pack(pady=10, padx=10)

app.mainloop()
