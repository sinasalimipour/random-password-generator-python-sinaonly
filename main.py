
from tkinter import *
import tkinter
import random

root = Tk()


e = Entry(root,borderwidth=10,).grid(row=5, column=0)



def myClick():
    txtforpassword = Label(root, text="here your password with length of:"+ e.get()).grid()


welcometext = Label(root, text="welcome to the password generator").grid(row=0, column=0)
lengthtext = Label(root, text="what length would you like to your password be:").grid(row=1, column=0)
Buttonforpassword = Button(root, text="find me a random password",command=myClick,fg="blue",bg="black").grid()


root.mainloop()




# #password-GENRATOR start

# chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+}{"
# while 1:
#     password_len = int(input("what length would you like to your password be:"))
#     password_count = int(input("how many password would you like :"))
#     for x in range(0,password_count):
#         password = ""
#         for x in range(0,password_len):
#             password_char = random.choice(chars)
#             password = password + password_char
#         print("here is your password",password)

# #password-GENRATOR end