from tkinter import Tk, PhotoImage, Label, Radiobutton, Spinbox, Button, IntVar, Checkbutton, BooleanVar, messagebox
import string, random

numbers = string.digits
uppercase_alphabets = string.ascii_uppercase
lowercase_alphabets = string.ascii_lowercase
symbols = string.punctuation
strength_value = ''
password = ''
uppercase = False


def strength():
    global strength_value
    if var.get() == 1:
        strength_value = 'moderate'
    elif var.get() == 2:
        strength_value = 'high'
    elif var.get() == 0:
        strength_value = 'low'


def password_generate():
    global password
    length = int(spinbox.get())
    if uppercase:
        if strength_value == 'moderate':
            x = uppercase_alphabets + lowercase_alphabets + numbers
            password = ''.join(random.sample(x,length))

        elif strength_value == 'high':
            x = uppercase_alphabets + lowercase_alphabets + numbers + symbols
            password = ''.join(random.sample(x,length))

        else:
            alphabets = uppercase_alphabets + lowercase_alphabets
            password = ''.join(random.sample(alphabets,length))

    else:
        if strength_value == 'moderate':
            x = lowercase_alphabets + numbers
            password = ''.join(random.sample(x, length))

        elif strength_value == 'high':
            x = lowercase_alphabets + numbers + symbols
            password = ''.join(random.sample(x, length))

        else:
            alphabets = lowercase_alphabets
            password = ''.join(random.sample(alphabets, length))

    output_lab.config(text=password,background='black',highlightbackground='blue')
    x_axis = len(password) * 6 + 330
    save.place(x=x_axis,y=128)


def save_password():
    with open('password.txt','a') as f:
        f.write(password + '\n')
    messagebox.showinfo('password protected','Password saved successfully\nCheck password.txt')


def include_upper():
    global uppercase
    if boolVar.get():
        uppercase = True
    else:
        uppercase = False


win = Tk()
win.geometry('600x420+370+150')
win.title('Password Generator')
icon = PhotoImage(file='icon photo.png')
win.iconphoto(False,icon)
win.config(bg='#0a132d')
win.resizable(False,False)

header_img = PhotoImage(file='password generator header.png')
header = Label(win,image=header_img,bg='#0a132d')
header.place(x=0,y=0)

pass_strength = Label(win,text='Strength of password',font=('Comic Sans',12,'bold'),fg='white',bg='#0a132d')
pass_strength.place(x=60,y=190)

var = IntVar()
radioButton1 = Radiobutton(win,text='low',font=('Comic Sans',12),fg='#ffce08',bg='#0a132d',activebackground='#0a132d',
                           activeforeground='#ffce08',variable=var,value=0,command=strength,selectcolor='black')
radioButton1.place(x=305,y=190)

radioButton2 = Radiobutton(win,text='moderate',font=('Comic Sans',12),fg='#ffce08',bg='#0a132d',command=strength,value=1
                           ,activebackground='#0a132d',activeforeground='#ffce08',variable=var,selectcolor='black')
radioButton2.place(x=360,y=190)

radioButton3 = Radiobutton(win,text='high',font=('Comic Sans',12),fg='#ffce08',bg='#0a132d',activebackground='#0a132d',
                           activeforeground='#ffce08',variable=var,value=2,command=strength,selectcolor='black')
radioButton3.place(x=460,y=190)
radioButton1.select()

pass_length = Label(win,text='Length of password   (8 - 24)', font=('Comic Sans',12,'bold'),fg='white',bg='#0a132d')
pass_length.place(x=60,y=230)

spinbox = Spinbox(win,from_=8,to=24,font=('Comic Sans',12,'bold'),fg='black',width=4,wrap=True)
spinbox.place(x=385,y=231)

include_lab = Label(win,text='Include uppercase letters',font=('Comic Sans',12,'bold'),fg='white',bg='#0a132d')
include_lab.place(x=60,y=270)

boolVar = BooleanVar()
on_img = PhotoImage(file='on checkbutton.png')
off_img = PhotoImage(file='off checkbutton.png')
checkbutton = Checkbutton(win,bg='white',activebackground='white',image=off_img,variable=boolVar,selectcolor='white',
                          onvalue=True,offvalue=False,selectimage=on_img,command=include_upper,indicatoron=False)
checkbutton.place(x=397,y=270)

generate = Button(win,text='Generate',font=('Comic Sans',12,'bold'),fg='black',bg='#ffce08',activeforeground='black',
                  activebackground='#ffce08',bd=8,relief='raised',command=password_generate)
generate.place(x=255,y=330)

output_lab = Label(win,text=password,font=('Comic Sans',16,'bold'),fg='#ffce08',bg='#0a132d',padx=10,pady=5)
output_lab.pack(side='top',pady=125)

save = Button(win,text='save',font=('Comic Sans',10,'bold'),fg='black',bg='#ffce08',activeforeground='black',
              activebackground='#ffce08',bd=6,relief='raised',command=save_password)

win.mainloop()


