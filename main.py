from tkinter import messagebox
from tkinter import *
import webbrowser
import pyperclip
import random
import os


root = Tk()
root.title('Contact Book')
background = '#121212'
root.config(bg=background,)
root.geometry('650x300')

# TODO => Contacts have =>
#*                         1- Name 
"""
                                    Name Entry,
                                    Name Label,
                                    Name Row in DB,
"""
#*                         2- Number
"""
                                    Number Entry,
                                    Number Label,
                                    Number Row in DB,
"""

# Functions
def add_contact():
    contact_string = name_entry.get() + ': ' + phone_entry.get()
    listbox.insert(END, contact_string)
    
    name_entry.delete(0,END)
    phone_entry.delete(0,END)

def delete_contact():
    listbox.delete(ANCHOR)
    
def save_list():
    """ Save the list to a simple txt file """
    with open('.\saved_list\saved.txt', 'w') as f:
        # my_list_box.get()
        list_tuple = listbox.get(0,END)
        for item in list_tuple:
            if item.endswith('\n'):
                f.write(item)
            else:
                f.write(item+'\n')
                
def open_list():
    """ Open the list upon opening the app if there is one! """
    try:
        with open('.\saved_list\saved.txt', 'r') as f:
            for line in f:
                listbox.insert(END, line)
    except:
        return

def copy_number():
    content = listbox.get(ANCHOR)
    number = content.split(': ')
    pyperclip.copy(number[1].replace('\n',""))
    
def exit():
    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
    else:
        return
   
# def change_theme():
#     background = '#ffffff' 
#     root.config(bg=background,)
# # create a toplevel menu
# menubar = Menu(root)
# menubar.add_command(label="Change Theme!", command=change_theme)

    

# Labels
name_label = Label(root, text='Contact Name:', bg='#121212', fg='white', font=('Calibri', 12),anchor="w", justify=LEFT)
name_label.place(relx=0.1, rely=0.1, anchor='c')

number_label = Label(root, text='   Contact Number:', bg='#121212', fg='white', font=('Calibri', 12),anchor="w", justify=LEFT )
number_label.place(relx=0.1, rely=0.2, anchor='c')

# Entries
name_entry = Entry(root, bg='white', fg='#121212', borderwidth=2, width=30)
name_entry.place(relx=0.4, rely=0.1, anchor='c')

phone_entry = Entry(root, bg='white', fg='#121212', borderwidth=2, width=30)
phone_entry.place(relx=0.4, rely=0.2, anchor='c')


# Buttons
add_btn = Button(root, text='Add Contact', bg='#121212', fg='white', borderwidth=3, padx=125, command=add_contact)
add_btn.place(relx=0.29, rely=0.35, anchor='c')

save_btn = Button(root, text='  Save List  ', bg='#121212', fg='white', borderwidth=3, padx=130, command=save_list)
save_btn.place(relx=0.29, rely=0.5, anchor='c')

copyPhone =Button(root, text='Copy Phone Number', bg='#121212', fg='white', borderwidth=3, padx=10, command=copy_number)
copyPhone.place(relx=0.15, rely=0.65, anchor='c')

deletePhone =Button(root, text='Delete Contact ', bg='#121212', fg='white', borderwidth=3, padx=25, command=delete_contact)
deletePhone.place(relx=0.15, rely=0.77, anchor='c')

openSaved =Button(root, text='Open Saved File ', bg='#121212', fg='white', borderwidth=3, padx=30, command=lambda: webbrowser.open('.\saved_list'))
openSaved.place(relx=0.42, rely=0.65, anchor='c')

exit =Button(root, text='Exit App', bg='#121212', fg='white', borderwidth=3, padx=50, command=exit)
exit.place(relx=0.42, rely=0.77, anchor='c')
# List Box
listbox = Listbox(root,width=40, height=15)
listbox.place(relx=0.75, rely=0.47, anchor='c')


# root.config(menu=menubar)
open_list()
root.mainloop()