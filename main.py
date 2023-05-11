from tkinter import *
from tkinter import messagebox
import base64

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def save_and_encrypt():
    title = entry_title.get()
    message = input_text.get("1.0", END)
    master_secret = entry_master_secret.get()

    if len(title) == 0 or len(message) == 0 or len(master_secret) == 0:
        messagebox.showwarning(title="Error", message="Please enter all info.")
    else:
        message_encrypted = encode(master_secret, message)
        try:
            with open("my_secrets.txt", "a") as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")
        except FileNotFoundError:
            with open("my_secrets.txt", "w") as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")
        finally:
            entry_title.delete(0, END)
            entry_master_secret.delete(0, END)
            input_text.delete("1.0", END)


def decrypt_note():
    message_encrypted = input_text.get("1.0", END)
    master_secret = entry_master_secret.get()

    if len(message_encrypted) == 0 or len(master_secret) == 0:
        messagebox.showwarning(title="Error", message="Please enter all info.")
    else:
        try:
            decrypted_message = decode(master_secret, message_encrypted)
            input_text.delete("1.0", END)
            input_text.insert("1.0", decrypted_message)
        except:
            messagebox.showwarning(title="Error", message="Please give encrypted note!")



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

button_decrypt = Button(text="Decrypt", pady=5, command=decrypt_note)
button_decrypt.pack()


window.mainloop()