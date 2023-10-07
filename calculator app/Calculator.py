from tkinter import Tk, Label, Button, Entry, PhotoImage

plus_button = False
sub_button = False
mul_button = False
div_button = False
equals_button = False
calc_state = True
num1 = 0
index = 0


def num_one():
    global index, equals_button
    if equals_button:
        choice.delete(0,'end')
        equals_button = False
    choice.insert(index,'1')
    index += 1


def num_two():
    global index, equals_button
    if equals_button:
        choice.delete(0,'end')
        equals_button = False
    choice.insert(index,'2')
    index += 1


def num_three():
    global index, equals_button
    if equals_button:
        choice.delete(0,'end')
        equals_button = False
    choice.insert(index,'3')
    index += 1


def num_four():
    global index, equals_button
    if equals_button:
        choice.delete(0,'end')
        equals_button = False
    choice.insert(index,'4')
    index += 1


def num_five():
    global index, equals_button
    if equals_button:
        choice.delete(0,'end')
        equals_button = False
    choice.insert(index,'5')
    index += 1


def num_six():
    global index, equals_button
    if equals_button:
        choice.delete(0,'end')
        equals_button = False
    choice.insert(index,'6')
    index += 1


def num_seven():
    global index, equals_button
    if equals_button:
        choice.delete(0,'end')
        equals_button = False
    choice.insert(index,'7')
    index += 1


def num_eight():
    global index, equals_button
    if equals_button:
        choice.delete(0,'end')
        equals_button = False
    choice.insert(index,'8')
    index += 1


def num_nine():
    global index, equals_button
    if equals_button:
        choice.delete(0,'end')
        equals_button = False
    choice.insert(index,'9')
    index += 1


def num_zero():
    global index, equals_button
    if equals_button:
        choice.delete(0,'end')
        equals_button = False
    choice.insert(index,'0')
    index += 1


def add():
    global plus_button, num1
    plus_button = True
    if choice.get() != '':
        if choice.get() == '-':
            choice.delete(0,'end')
            choice.insert(0,'Syntax Error')
            disable_func()
        else:
            num1 = float(choice.get())
            choice.delete(0,'end')


def subtract():
    global sub_button, num1, index
    if choice.get() == '':
        choice.insert(index,'-')
        index += 1
    else:
        if choice.get() == '-':
            choice.delete(0,'end')
            choice.insert(0,'Syntax Error')
            disable_func()
        else:
            sub_button = True
            num1 = float(choice.get())
            choice.delete(0,'end')


def multiplication():
    global mul_button, num1
    mul_button = True
    if choice.get() != '':
        if choice.get() == '-':
            choice.delete(0,'end')
            choice.insert(0,'Syntax Error')
            disable_func()
        else:
            num1 = float(choice.get())
            choice.delete(0,'end')


def division():
    global div_button, num1
    div_button = True
    if choice.get() != '':
        if choice.get() == '-':
            choice.delete(0,'end')
            choice.insert(0,'Syntax Error')
            disable_func()
        else:
            num1 = float(choice.get())
            choice.delete(0,'end')


def result():
    global plus_button, sub_button, mul_button, div_button, equals_button
    equals_button = True
    if choice.get() != '':
        if choice.get() == '-':
            choice.delete(0,'end')
            choice.insert(0,'Syntax Error')
            disable_func()
        else:
            num2 = float(choice.get())
            choice.delete(0,'end')

            if plus_button:
                summation = str(round(num1 + num2))
                choice.insert(0,summation)
                plus_button = False

            elif sub_button:
                difference = str(round(num1 - num2))
                choice.insert(0,difference)
                sub_button = False

            elif mul_button:
                mult = str(round(num1 * num2))
                choice.insert(0,mult)
                mul_button = False

            elif div_button:
                try:
                    if num1 % num2 == 0:
                        div = str(round(num1 / num2))
                    else:
                        div = str(num1 / num2)

                    choice.insert(0,div)
                    div_button = False

                except ZeroDivisionError:
                    choice.insert(0,'Zero Division Error')
                    disable_func()

            else:
                choice.insert(0,str(num2))


def clr():
    global calc_state
    choice.delete(0,'end')
    if not calc_state:
        plus_btn.config(state='normal')
        minus_btn.config(state='normal')
        multiply_btn.config(state='normal')
        divide_btn.config(state='normal')
        equals_btn.config(state='normal')
        one_btn.config(state='normal')
        two_btn.config(state='normal')
        three_btn.config(state='normal')
        four_btn.config(state='normal')
        five_btn.config(state='normal')
        six_btn.config(state='normal')
        seven_btn.config(state='normal')
        eight_btn.config(state='normal')
        nine_btn.config(state='normal')
        zero_btn.config(state='normal')
        calc_state = True


def disable_func():
    global calc_state
    calc_state = False
    plus_btn.config(state='disabled')
    minus_btn.config(state='disabled')
    multiply_btn.config(state='disabled')
    divide_btn.config(state='disabled')
    equals_btn.config(state='disabled')
    one_btn.config(state='disabled')
    two_btn.config(state='disabled')
    three_btn.config(state='disabled')
    four_btn.config(state='disabled')
    five_btn.config(state='disabled')
    six_btn.config(state='disabled')
    seven_btn.config(state='disabled')
    eight_btn.config(state='disabled')
    nine_btn.config(state='disabled')
    zero_btn.config(state='disabled')


win = Tk()
win.geometry('295x350+520+140')
win.title('Calculator')
icon = PhotoImage(file='calculator icon.png')
win.iconphoto(False,icon)
win.resizable(False,False)
win.config(bg='white')

plus = PhotoImage(file='plus sign.png')
minus = PhotoImage(file='minus sign.png')
multiply = PhotoImage(file='multiply sign.png')
divide = PhotoImage(file='divide sign.png')
equals_to = PhotoImage(file='equals to sign.png')
one = PhotoImage(file='one.png')
two = PhotoImage(file='two.png')
three = PhotoImage(file='three.png')
four = PhotoImage(file='four.png')
five = PhotoImage(file='five.png')
six = PhotoImage(file='six.png')
seven = PhotoImage(file='seven.png')
eight = PhotoImage(file='eight.png')
nine = PhotoImage(file='nine.png')
zero = PhotoImage(file='zero.png')
clear = PhotoImage(file='clr.png')

casio_label = Label(win,text='CASIO',font=('Helvetica',18,'bold'),fg='black',bg='white')
casio_label.place(x=105,y=7)

choice = Entry(win,font=('Helvetica',20,'bold'),bg='#d1d1d1',width=17)
choice.place(x=18,y=40)

plus_btn = Button(win,image=plus,bd=4,relief='raised',bg='#eb008b',command=add)
plus_btn.place(x=215,y=210)

minus_btn = Button(win,image=minus,bd=4,relief='raised',bg='#76b73f',command=subtract)
minus_btn.place(x=215,y=270)

multiply_btn = Button(win,image=multiply,bd=4,relief='raised',bg='#76298f',command=multiplication)
multiply_btn.place(x=215,y=150)

divide_btn = Button(win,image=divide,bd=4,relief='raised',bg='#fbad19',command=division)
divide_btn.place(x=215,y=90)

equals_btn = Button(win,image=equals_to,bd=4,relief='raised',bg='#483f9a',command=result)
equals_btn.place(x=150,y=270)

one_btn = Button(win,image=one,bd=4,relief='raised',bg='#00aeed',command=num_one)
one_btn.place(x=20,y=210)

two_btn = Button(win,image=two,bd=4,relief='raised',bg='#f25a29',command=num_two)
two_btn.place(x=85,y=210)

three_btn = Button(win,image=three,bd=4,relief='raised',bg='#eb008b',command=num_three)
three_btn.place(x=150,y=210)

four_btn = Button(win,image=four,bd=4,relief='raised',bg='#77b840',command=num_four)
four_btn.place(x=20,y=150)

five_btn = Button(win,image=five,bd=4,relief='raised',bg='#76298f',command=num_five)
five_btn.place(x=85,y=150)

six_btn = Button(win,image=six,bd=4,relief='raised',bg='#fbad19',command=num_six)
six_btn.place(x=150,y=150)

seven_btn = Button(win,image=seven,bd=4,relief='raised',bg='#483f9a',command=num_seven)
seven_btn.place(x=20,y=90)

eight_btn = Button(win,image=eight,bd=4,relief='raised',bg='#00b6a9',command=num_eight)
eight_btn.place(x=85,y=90)

nine_btn = Button(win,image=nine,bd=4,relief='raised',bg='#eb1c24',command=num_nine)
nine_btn.place(x=150,y=90)

zero_btn = Button(win,image=zero,bd=4,relief='raised',bg='#00aeed',command=num_zero)
zero_btn.place(x=85,y=270)

clear_btn = Button(win,image=clear,bd=4,relief='raised',bg='#f88a3f',command=clr)
clear_btn.place(x=20,y=270)

win.mainloop()








