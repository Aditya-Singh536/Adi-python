import customtkinter as ctk
import tkinter.messagebox as tkmb


class ContactManager:
    def __init__(self):
        self.contacts = {"A": "845845", "B": "34983"}

    def add_contact(self, name, phone_num):
        if not name or not phone_num:
            return "Name and phone number cannot be empty.", False
        if not phone_num.isdigit() or len(phone_num) != 10:
            return (
                "Invalid Indian phone number. It must be 10 digits and contain only numbers.",
                False,
            )

        self.contacts[name] = phone_num
        return f"Contact '{name}' with number '{phone_num}' stored successfully!", True

    def search_contact(self, name):
        if not name:
            return "Name cannot be empty.", None
        if name in self.contacts:
            return (
                f"The number for '{name}' is: {self.contacts[name]}.",
                self.contacts[name],
            )
        else:
            return f"'{name}' does not exist in your contact list.", None

    def delete_contact(self, name):
        if not name:
            return "Name cannot be empty.", False
        if name in self.contacts:
            del self.contacts[name]
            return f"Contact '{name}' deleted successfully.", True
        else:
            return f"'{name}' does not exist in your contact list.", False

    def get_all_contacts(self):
        return self.contacts


class ContactApp(ctk.CTk):
    def __init__(self, manager):
        super().__init__()
        self.manager = manager
        self.title("Contact List Manager")
        self.geometry("600x680")  # Increased height slightly for the new button
        self.resizable(False, False)

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self._create_widgets()
        self._update_contact_display()  # Display contacts on startup

    def _create_widgets(self):
        # --- Add Contact Section ---
        add_frame = ctk.CTkFrame(self)
        add_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(
            add_frame, text="Add New Contact", font=("Arial", 16, "bold")
        ).pack(pady=5)

        ctk.CTkLabel(add_frame, text="Name:").pack(pady=(5, 0))
        self.name_entry = ctk.CTkEntry(add_frame, width=250)
        self.name_entry.pack(pady=(0, 5))

        ctk.CTkLabel(add_frame, text="Phone Number (10 digits):").pack(pady=(5, 0))
        self.phone_entry = ctk.CTkEntry(add_frame, width=250)
        self.phone_entry.pack(pady=(0, 10))

        ctk.CTkButton(
            add_frame, text="Add Contact", command=self._add_contact_gui
        ).pack(pady=5)

        # --- Search Contact Section ---
        search_frame = ctk.CTkFrame(self)
        search_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(
            search_frame, text="Search Contact", font=("Arial", 16, "bold")
        ).pack(pady=5)

        ctk.CTkLabel(search_frame, text="Name to Search:").pack(pady=(5, 0))
        self.search_entry = ctk.CTkEntry(search_frame, width=250)
        self.search_entry.pack(pady=(0, 5))

        ctk.CTkButton(
            search_frame, text="Search Contact", command=self._search_contact_gui
        ).pack(pady=5)
        self.search_result_label = ctk.CTkLabel(search_frame, text="", wraplength=400)
        self.search_result_label.pack(pady=5)

        # --- Delete Contact Section ---
        delete_frame = ctk.CTkFrame(self)
        delete_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(
            delete_frame, text="Delete Contact", font=("Arial", 16, "bold")
        ).pack(pady=5)

        ctk.CTkLabel(delete_frame, text="Name to Delete:").pack(pady=(5, 0))
        self.delete_entry = ctk.CTkEntry(delete_frame, width=250)
        self.delete_entry.pack(pady=(0, 10))

        ctk.CTkButton(
            delete_frame, text="Delete Contact", command=self._delete_contact_gui
        ).pack(pady=5)

        # --- Display Contacts Section ---
        display_frame = ctk.CTkFrame(self)
        display_frame.pack(pady=10, padx=20, fill="both", expand=True)

        ctk.CTkLabel(
            display_frame, text="All Contacts", font=("Arial", 16, "bold")
        ).pack(pady=5)

        # Button to explicitly show all contacts
        ctk.CTkButton(
            display_frame,
            text="Refresh All Contacts",
            command=self._update_contact_display,
        ).pack(pady=(0, 10))

        self.contact_textbox = ctk.CTkTextbox(
            display_frame, width=500, height=150, wrap="word"
        )
        self.contact_textbox.pack(pady=5, fill="both", expand=True)
        self.contact_textbox.configure(state="disabled")

    def _add_contact_gui(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        message, success = self.manager.add_contact(name, phone)
        if success:
            tkmb.showinfo("Success", message)
            self._clear_entries([self.name_entry, self.phone_entry])
            self._update_contact_display()
        else:
            tkmb.showerror("Error", message)

    def _search_contact_gui(self):
        name = self.search_entry.get().strip()
        message, phone = self.manager.search_contact(name)
        self.search_result_label.configure(text=message)
        if phone:
            self.search_result_label.configure(text_color="green")
        else:
            self.search_result_label.configure(text_color="red")
        self._clear_entries([self.search_entry])

    def _delete_contact_gui(self):
        name = self.delete_entry.get().strip()
        message, success = self.manager.delete_contact(name)
        if success:
            tkmb.showinfo("Success", message)
            self._clear_entries([self.delete_entry])
            self._update_contact_display()
        else:
            tkmb.showerror("Error", message)

    def _update_contact_display(self):
        self.contact_textbox.configure(state="normal")
        self.contact_textbox.delete("1.0", "end")
        contacts = self.manager.get_all_contacts()
        if not contacts:
            self.contact_textbox.insert("end", "No contacts stored yet.")
        else:
            for name, phone in contacts.items():
                self.contact_textbox.insert("end", f"Name: {name}, Phone: {phone}\n")
        self.contact_textbox.configure(state="disabled")

    def _clear_entries(self, entries):
        for entry in entries:
            entry.delete(0, ctk.END)


# --- Main execution ---
if __name__ == "__main__":
    contact_manager = ContactManager()
    app = ContactApp(contact_manager)
    app.mainloop()
