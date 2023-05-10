from tkinter import *
from tkinter import messagebox

def save_and_encrypt():
    title = entry_title.get()
    message = input_text.get("1.0", END)
    master_secret = entry_master_secret.get()

    if len(title) == 0 or len(message) == 0 or len(master_secret) == 0:
        messagebox.showwarning(title="Error", message="Please enter all info.")
    else:
        try:
            with open("my_secrets.txt", "a") as data_file:
                data_file.write(f"\n{title}\n{message}")
        except FileNotFoundError:
            with open("my_secrets.txt", "w") as data_file:
                data_file.write(f"\n{title}\n{message}")
        finally:
            entry_title.delete(0, END)
            entry_master_secret.delete(0, END)
            input_text.delete("1.0", END)


my_font = ("Verdena", 15, "italic")

window = Tk()
window.title("Top Secret!")
window.minsize(500,700)

image_secret = PhotoImage(file="src/confidential.png")
label_image = Label(image=image_secret)
label_image.pack()

label_info_entry = Label(text="Enter title:", font=my_font)
label_info_entry.pack()

entry_title = Entry(width=30)
entry_title.pack()

label_info_input = Label(text="Enter your secret thing:", font=my_font)
label_info_input.pack()

input_text = Text(width=50, height=25)
input_text.pack()

label_info_master_secret = Label(text="Enter master key:", font=my_font)
label_info_master_secret.pack()

entry_master_secret = Entry(width=30)
entry_master_secret.pack()

button_save = Button(text="Save & Encrypt", pady=5, command=save_and_encrypt)
button_save.pack()

button_decrypt = Button(text="Decrypt", pady=5)
button_decrypt.pack()


window.mainloop()