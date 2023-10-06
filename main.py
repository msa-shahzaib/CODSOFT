from tkinter import Tk, Label, Button, Entry, PhotoImage, Frame, Listbox, Menubutton, Menu, Scrollbar

index = 0


def add_item():
    global index
    if entry.get() != '':
        item = entry.get()
        entry.delete(0,'end')
        listbox.insert(index,item)
        index += 1


def delete_item():
    if not len(listbox.curselection()) == 0:
        ind = listbox.curselection()
        if len(ind) == 1:
            listbox.delete(ind[0])

        elif len(ind) == 2:
            listbox.delete(ind[0])
            listbox.delete(ind[1] - 1)

        elif len(ind) == 3:
            listbox.delete(ind[0])
            listbox.delete(ind[1] - 1)
            listbox.delete(ind[2] - 2)

        else:
            listbox.delete(ind[0])
            listbox.delete(ind[1] - 1)
            listbox.delete(ind[2] - 2)
            listbox.delete(ind[3] - 3)


def saveMenu():
    def saveFile():
        if filename_entry.get() == '':
            emp_lab.config(text='filename required')
        else:
            tasks = listbox.get(0, 'end')
            file = str(filename_entry.get()) + '.txt'

            with open(file,'w') as f:
                for task in range(len(tasks)):
                    f.write(tasks[task] + ',')
            win2.destroy()

    win2 = Tk()
    win2.geometry('300x100+525+220')
    win2.title('save list')
    win2.config(bg='#0e0d26')
    win2.resizable(False,False)

    filename_entry = Entry(win2,font=('Arial',18,'bold'),width=16)
    filename_entry.place(x=15,y=21)

    save_btn = Button(win2,text='Save',font=('Arial',10,'bold'),bd=5,relief='raised',fg='black',bg='#d17e19',
                      activebackground='#d17e19',command=saveFile)
    save_btn.place(x=235,y=20)

    emp_lab = Label(win2,text='',font=('Arial',10),fg='red',bg='#0e0d26')
    emp_lab.place(x=80,y=60)

    win2.mainloop()


def openMenu():
    def openFile():
        listbox.delete(0,'end')
        file = str(openFileEntry.get()) + '.txt'
        try:
            with open(file) as f:
                for task in f.readlines():
                    toDoList = task.split(',')
                    toDoList.pop(-1)
                    for i in range(len(toDoList)):
                        listbox.insert(i,toDoList[i])
            win3.destroy()

        except FileNotFoundError:
            emp_lab.config(text=f'{file} does not exist')
            openFileEntry.delete(0,'end')

    win3 = Tk()
    win3.geometry('300x100+525+220')
    win3.title('Open saved files')
    win3.config(bg='#0e0d26')
    win3.resizable(False,False)

    openFileEntry = Entry(win3,font=('Arial',18,'bold'),width=16)
    openFileEntry.place(x=15,y=21)

    open_btn = Button(win3,text='Open',font=('Arial',10,'bold'),bd=5,relief='raised',fg='black',bg='#d17e19',
                      activebackground='#d17e19',command=openFile)
    open_btn.place(x=235,y=20)

    emp_lab = Label(win3,text='',font=('Arial',10),fg='red',bg='#0e0d26')
    emp_lab.place(x=60,y=60)

    win3.mainloop()


def clr():
    listbox.delete(0,'end')


win = Tk()
win.geometry('350x450+500+130')
win.title('To-Do-List')
win.config(bg='#0e0d26')
win.resizable(False,False)
icon = PhotoImage(file='list icon.png')
win.iconphoto(False,icon)

empty_label = Label(win,text='',font=('Arial',35),bg='#d17e19',width=50)
empty_label.place(x=0,y=0)

head_label = Label(win,text='All Tasks',font=('Georgia',20,'bold'),fg='#050300',bg='#d17e19')
head_label.place(x=110,y=15)

menu_img = PhotoImage(file='menu button.png')
menubutton = Menubutton(win,image=menu_img,bg='#d17e19',relief='flat')
menubutton.place(x=20,y=22)
menubutton.menu = Menu(menubutton,tearoff=0)
menubutton['menu'] = menubutton.menu
menubutton.menu.add_checkbutton(label='Save',indicatoron=False,command=saveMenu)
menubutton.menu.add_checkbutton(label='Open',indicatoron=False,command=openMenu)

del_img = PhotoImage(file='delete-button modified.png')
delete_btn = Button(win,image=del_img,bd=5,bg='#fa3232',activebackground='#fa3232',relief='raised',command=delete_item)
delete_btn.place(x=210,y=385)

clear_btn = Button(win,text='clear list',font=('Arial',10,'bold'),fg='black',bg='#d17e19',activeforeground='black',
                   activebackground='#d17e19',bd=5,relief='raised',command=clr)
clear_btn.place(x=90,y=395)

frame = Frame(win,bg='grey')
frame.pack(side='bottom',padx=10,pady=80)

scroll = Scrollbar(frame,orient='vertical',width=30)
scroll.pack(side='right',fill='y')

listbox = Listbox(frame,font=('Arial',20,'bold'),width=20,height=7,fg='#0e0d26',bg='#c9c9c9',yscrollcommand=scroll.set,
                  selectbackground='#0e0d26',selectmode='multiple')
listbox.pack(side='bottom')
scroll.config(command=listbox.yview)

entry = Entry(win,font=('Arial',20,'bold'),width=19)
entry.place(x=10,y=91)

add_img = PhotoImage(file='add button modified.png')
add_btn = Button(win,image=add_img,bd=3,bg='#001789',activebackground='#001789',relief='raised',command=add_item)
add_btn.place(x=300,y=90)

win.mainloop()
