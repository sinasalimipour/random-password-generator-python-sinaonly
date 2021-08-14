
from tkinter import *
import tkinter
import random

root = Tk()

myLabel = Label(root, text="hello world").grid(row=0, column=0)
myLabel1 = Label(root, text="what length would you like to your password be:").grid(row=1, column=0)



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