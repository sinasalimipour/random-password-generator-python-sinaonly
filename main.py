
from tkinter import *
import tkinter
import random

root = Tk()
root.title("password generator")



#welcometext
welcometext = Label(root, text="welcome to the password generator").grid(row=0, column=0)
#welcometext end





#text box and Button 1

lengthtext = Label(root, text="how many password do you need:").grid(row=1, column=0)
userinput_for_how_many = Entry(root,borderwidth=5,)
userinput_for_how_many.grid()
def button_how_many():
    user_password_how_many = Label(root, text="your want " + userinput_for_how_many.get() + " different password").grid()

Button_for_how_password_many= Button(root,text="submit",command=button_how_many).grid()

#text box and Button 1 end






#text box and Button 2

lengthtext = Label(root, text="what length would you like to your password be:").grid()
userinput_for_length = Entry(root,borderwidth=5,)
userinput_for_length.grid()

def button_add():
    user_password_length = Label(root, text="your password length is: " + userinput_for_length.get() + " character long").grid()

Button_for_password_length= Button(root,text="submit",command=button_add).grid()

#text box and Button 2 end


chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+}{"
while 1:
    password_len = userinput_for_length.get()
    password_count = userinput_for_how_many.get()


for x in range(0, password_count):
    password = ""
    for x in range(0, password_len):
        password_char = random.choice(chars)
        password = password + password_char




#text box and Button 3


def button_find():
    user_password = Label(root, text="your password is: " + password).grid()

Button_for_password_length= Button(root,text="find me a random password",command=button_find).grid()

#text box and Button 3 end








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








#.v1 GUI


# e = Entry(root,borderwidth=5,).grid(row=5, column=0,columnspan=10)
#
#
# def button_add():
#         first_number = e.get()
#         global f_num
#
# def myClick():
#     number1 = Label(root,text=f_num+e.get()).grid()
#     txtforpassword = Label(root, text="here your password with length of:"+ e.get()).grid()
#
#
# welcometext = Label(root, text="welcome to the password generator").grid(row=0, column=0)
# lengthtext = Label(root, text="what length would you like to your password be:").grid(row=1, column=0)
# Buttonforpassword = Button(root, text="find me a random password",command=myClick,fg="blue",bg="black").grid()