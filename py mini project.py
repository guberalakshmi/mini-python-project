import tkinter as tk
from tkinter import messagebox


FILE_NAME = "contacts.txt"


def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()

    if name == "" or phone == "":
        messagebox.showwarning("Warning", "Please enter all details")
        return

    with open(FILE_NAME, "a") as f:
        f.write(name + "," + phone + "\n")

    messagebox.showinfo("Success", "Contact Saved")
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    view_contacts()


def view_contacts():
    listbox.delete(0, tk.END)
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                name, phone = line.strip().split(",")
                listbox.insert(tk.END, f"{name} - {phone}")
    except FileNotFoundError:
        pass


def delete_contact():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Select a contact")
        return

    contact = listbox.get(selected[0])
    name = contact.split(" - ")[0]

    lines = []
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()

    with open(FILE_NAME, "w") as f:
        for line in lines:
            if not line.startswith(name + ","):
                f.write(line)

    messagebox.showinfo("Deleted", "Contact Deleted")
    view_contacts()


root = tk.Tk()
root.title("Contact Manager")
root.geometry("350x400")


tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Phone").pack()
entry_phone = tk.Entry(root)
entry_phone.pack()


tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)


listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True)


view_contacts()


root.mainloop()
