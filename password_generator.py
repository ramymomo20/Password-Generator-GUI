from generator_logic import *
from tkinter import *
from tkinter import messagebox

#Initialize Window
root = Tk()
root.geometry("400x400") #size of the window by default

#title of our window
root.title("Password Generator")

pass_len = IntVar()
output_pass = StringVar()
name = StringVar()
 
def randPassGen():
    password = passwordCreator(pass_len.get())
    output_pass.set(password)

def passStorage():
    messagebox.showinfo("Information","Your password has been saved to Password Storage.txt")
    passwordStorage(output_pass.get(), name.get())

# ----------- Copy to clipboard function
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(output_pass.get())
    label1 = Label(root, text="")

    label1.configure(text = "Copied to Clipboard", font = 'arial 10 italic')
    label1.place(x=265,y=331)

#-----------------------Front-end Designing (GUI)
pass_head = Label(root, text = 'Customized Password Length: 8-32', font = 'arial 12 bold').pack(pady=10)

length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 12, font='arial 16',justify='center').pack()

#Generate password button
Button(root, command = randPassGen, text = "Generate Password", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5 ).pack()

pass_label = Label(root, text = 'Your Generated Password', font = 'arial 12 bold').pack(pady="20 10")
Entry(root, textvariable = output_pass, width = 40, font='arial 10',justify='center').pack()

reason = Label(root, text = "What's the password for?", font = 'arial 10').pack(pady="20 5")
Entry(root, textvariable = name, width = 20, font='arial 10',justify='center').pack()


Button(root, text = "Save Password to Directory", command = passStorage,font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=10 ).pack(pady= 10)


#Copy to clipboard button
Button(root, text = 'Copy to Clipboard', command = copy_password, font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=10 ).pack(pady= 10)

root.mainloop()  #to bundle pack the code for tkinter