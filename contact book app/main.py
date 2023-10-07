from tkinter import Tk, PhotoImage, Button, Frame, Listbox, Scrollbar, Label, Entry, messagebox

index = 0
fName = ''
lName = ''
PhoneNo = ''
Email = ''
Address = ''
x = ''
contactSelected = False
mint = '#a2e3cc'
blue = '#001f40'


class ContactBook:
    contactList = []

    def addContact(self):
        def saveContact():
            if first_name_ent.get() == '':
                lab1.config(text='*first name is required')

            elif last_name_ent.get() == '':
                lab1.config(text='*last name is required')

            elif phone_no_ent.get() == '':
                lab1.config(text='*phone no. is required')

            elif email_ent.get() == '':
                lab1.config(text='*email field is required')

            elif address_ent.get() == '':
                lab1.config(text='*address is required')

            else:
                if not (phone_no_ent.get().isdigit()) or len(phone_no_ent.get()) != 11:
                    lab1.config(text='*Invalid phone number!')

                elif '@' not in email_ent.get() or '.com' not in email_ent.get():
                    lab1.config(text='*Invalid email address!')

                else:
                    global index, fName, lName, PhoneNo, Email, Address
                    lab1.destroy()
                    fName, lName, phoneNo, Email, Address = (first_name_ent.get().title(), last_name_ent.get().title(), phone_no_ent.get(), email_ent.get(), address_ent.get())
                    fullName = fName + ' ' + lName
                    if fullName in listbox.get(0,'end'):
                        messagebox.showwarning('contact exists',f'{fullName} is already in list!')
                    else:
                        messagebox.showinfo('contact info', 'Contact Saved Successfully!')
                        listbox.insert(index,fullName)
                        index += 1

                        first_name = fName.split()
                        last_name = lName.split()
                        with open('contacts.txt','a') as f:
                            if len(first_name) == 1 and len(last_name) == 1:
                                string = first_name[0] + ',' + last_name[0] + ',' + phoneNo + ',' + Email + ',' + Address + '\n'
                            elif len(first_name) == 2 and len(last_name) == 1:
                                string = first_name[0] + ',' + first_name[1] + ',' + last_name[0] + ',' + phoneNo + ',' + Email + ',' + Address + '\n'
                            elif len(first_name) == 1 and len(last_name) == 2:
                                string = first_name[0] + ',' + last_name[0] + ',' + last_name[1] + ',' + phoneNo+ ',' + Email + ',' + Address + '\n'
                            else:
                                string = first_name[0] + ',' + first_name[1] + ',' + last_name[0] + ',' + last_name[1] + ',' + phoneNo + ',' + Email + ',' + phoneNo + '\n'
                            f.write(string)
                    add_win.destroy()

        add_win = Tk()
        add_win.geometry('450x400+450+100')
        add_win.title('Contact Book')
        add_win.config(bg='white')
        add_win.resizable(False,False)

        con_details = Label(add_win,text='CONTACT DETAILS',font=('Baskerville',20,'bold'),bg='white',fg=blue)
        con_details.pack(pady=10)

        frame = Frame(add_win,width=420,height=250)
        frame.pack()

        f_name_lab = Label(frame,text='Enter first name:', font=('Baskerville',12),fg='black')
        f_name_lab.place(x=10,y=10)

        first_name_ent = Entry(frame,font=('Baskerville', 12),bg='white',fg='black', width=22)
        first_name_ent.place(x=170,y=10)

        l_name_lab = Label(frame,text='Enter last name:', font=('Baskerville', 12),fg='black')
        l_name_lab.place(x=10,y=60)

        last_name_ent = Entry(frame,font=('Baskerville',12), bg='white', fg='black', width=22)
        last_name_ent.place(x=170,y=60)

        phone_lab = Label(frame,text='Enter phone no.:',font=('Baskerville', 12),fg='black')
        phone_lab.place(x=10,y=110)

        phone_no_ent = Entry(frame,font=('Baskerville', 12), bg='white', fg='black', width=22)
        phone_no_ent.place(x=170,y=110)

        email_lab = Label(frame,text='Enter email:', font=('Baskerville', 12),fg='black')
        email_lab.place(x=10,y=160)

        email_ent = Entry(frame,font=('Baskerville', 12), bg='white', fg='black', width=22)
        email_ent.place(x=170,y=160)

        address_lab = Label(frame,text='Enter address:', font=('Baskerville', 12),fg='black')
        address_lab.place(x=10,y=210)

        address_ent = Entry(frame,font=('Baskerville', 12), bg='white', fg='black',width=22)
        address_ent.place(x=170,y=210)

        save_btn = Button(add_win,text='save',font=('Baskerville',11),bg='#fa3434',activebackground='#fa3434',fg='black',
                           activeforeground='black',bd=6,relief='raised',command=saveContact)
        save_btn.pack(side='bottom',pady=15)

        lab1 = Label(add_win,text='', font=('Baskerville', 12), bg='white', fg='red')
        lab1.pack(side='bottom')

        add_win.mainloop()

    def updateContact(self):
        def newDetails():
            if fn_entry.get() == '':
                lab2.config(text='*first name is required')

            elif ln_entry.get() == '':
                lab2.config(text='*last name is required')

            elif pn_entry.get() == '':
                lab2.config(text='*phone no. is required')

            elif em_entry.get() == '':
                lab2.config(text='*email field is required')

            elif a_entry.get() == '':
                lab2.config(text='*address is required')

            else:
                if not(pn_entry.get().isdigit()) or len(pn_entry.get()) != 11:
                    lab2.config(text='*Invalid phone number!')

                elif '@' not in em_entry.get() or '.com' not in em_entry.get():
                    lab2.config(text='*Invalid email address!')

                else:
                    f_name, l_name, Phone_no, email, address = fn_entry.get().title(), ln_entry.get().title(), pn_entry.get(), em_entry.get(), a_entry.get().strip()
                    fullName = f_name + ' ' + l_name
                    f_name, l_name = f_name.split(), l_name.split()
                    fn, ln = firstname.split(), lastname.split()

                    updatedContacts = []
                    with open('contacts.txt') as f:
                        for i in f.readlines():
                            contacts = i.strip().split(',')
                            if len(fn) == 1 and len(ln) == 1:
                                if fn[0] in contacts and ln[0] in contacts:
                                    contacts.clear()
                                    for i in range(len(f_name)):
                                        contacts.append(f_name[i])
                                    for i in range(len(l_name)):
                                        contacts.append(l_name[i])
                                    contacts.append(Phone_no)
                                    contacts.append(email)
                                    contacts.append(address)

                            elif len(fn) == 2 and len(ln) == 1:
                                if fn[0] in contacts and fn[1] in contacts and ln[0] in contacts:
                                    contacts.clear()
                                    for i in range(len(f_name)):
                                        contacts.append(f_name[i])
                                    for i in range(len(l_name)):
                                        contacts.append(l_name[i])
                                    contacts.append(Phone_no)
                                    contacts.append(email)
                                    contacts.append(address)

                            elif len(fn) == 1 and len(ln) == 2:
                                if fn[0] in contacts and ln[0] in contacts and ln[1] in contacts:
                                    contacts.clear()
                                    for i in range(len(f_name)):
                                        contacts.append(f_name[i])
                                    for i in range(len(l_name)):
                                        contacts.append(l_name[i])
                                    contacts.append(Phone_no)
                                    contacts.append(email)
                                    contacts.append(address)

                            else:
                                if fn[0] in contacts and fn[1] in contacts and ln[0] in contacts and ln[1] in contacts:
                                    contacts.clear()
                                    for i in range(len(f_name)):
                                        contacts.append(f_name[i])
                                    for i in range(len(l_name)):
                                        contacts.append(l_name[i])
                                    contacts.append(Phone_no)
                                    contacts.append(email)
                                    contacts.append(address)
                            updatedContacts.append(contacts)

                    with open('contacts.txt','w') as f:
                        for i in updatedContacts:
                            f.write(','.join(i) + '\n')

                    listbox.delete(listbox.curselection())
                    listbox.insert(0,fullName)
                    update_win.destroy()

        if contactSelected:
            firstname, lastname, phone, email, address = (fname_entry.get(), lname_entry.get(), phone_no_entry.get(),
                                                          email_entry.get(), address_entry.get())

            update_win = Tk()
            update_win.geometry('450x400+450+100')
            update_win.title('Edit Contact')
            update_win.config(bg='white')
            update_win.resizable(False, False)

            con_details = Label(update_win, text='Update Contact', font=('Baskerville', 20, 'bold'), bg='white',
                                fg=blue)
            con_details.pack(pady=10)

            frame = Frame(update_win, width=420, height=250)
            frame.pack()

            f_name_lab = Label(frame, text='Enter first name:', font=('Baskerville', 12),fg='black')
            f_name_lab.place(x=10, y=10)

            fn_entry = Entry(frame, font=('Baskerville', 12), bg='white', fg='black', width=22)
            fn_entry.place(x=170, y=10)
            fn_entry.insert(0,firstname)

            l_name_lab = Label(frame, text='Enter last name:', font=('Baskerville', 12),fg='black')
            l_name_lab.place(x=10, y=60)

            ln_entry = Entry(frame, font=('Baskerville', 12), bg='white', fg='black', width=22)
            ln_entry.place(x=170, y=60)
            ln_entry.insert(0,lastname)

            phone_lab = Label(frame, text='Enter phone no.:', font=('Baskerville', 12),fg='black')
            phone_lab.place(x=10, y=110)

            pn_entry = Entry(frame, font=('Baskerville', 12), bg='white', fg='black', width=22)
            pn_entry.place(x=170, y=110)
            pn_entry.insert(0,phone)

            email_lab = Label(frame, text='Enter email:', font=('Baskerville', 12),fg='black')
            email_lab.place(x=10, y=160)

            em_entry = Entry(frame, font=('Baskerville', 12), bg='white', fg='black', width=22)
            em_entry.place(x=170, y=160)
            em_entry.insert(0,email)

            address_lab = Label(frame, text='Enter address:', font=('Baskerville', 12),fg='black')
            address_lab.place(x=10, y=210)

            a_entry = Entry(frame, font=('Baskerville', 12), bg='white', fg='black', width=22)
            a_entry.place(x=170, y=210)
            a_entry.insert(0,address)

            saveButton = Button(update_win, text='save', font=('Baskerville', 11), bg='#fa3434', activebackground='#fa3434',
                              fg='black',activeforeground='black',bd=6, relief='raised',command=newDetails)
            saveButton.pack(side='bottom',pady=15)

            lab2 = Label(update_win,text='',font=('Baskerville',12),bg='white',fg='red')
            lab2.pack(side='bottom')

            update_win.mainloop()

    def viewContactList(self):
        global index, contactSelected
        if len(listbox.get(0, 'end')) > 0:
            listbox.delete(0, 'end')
        with open('contacts.txt') as f:
            for i in f.readlines():
                contactList = i.split(',')
                if contactList[2].isdigit():
                    listbox.insert(index, contactList[0] + ' ' + contactList[1])
                elif contactList[3].isdigit():
                    listbox.insert(index, contactList[0] + ' ' + contactList[1] + ' ' + contactList[2])
                else:
                    listbox.insert(index, contactList[0] + ' ' + contactList[1] + ' ' + contactList[2] + ' ' +
                                   contactList[3])
                index += 1
        contactSelected = False

    def searchContact(self):
        def searchContact():
            contact = search_entry.get().title()
            if contact == '':
                lab.config(text='*Type in to search a contact!')
            else:
                lab.config(text='')
                content = listbox.get(0, 'end')
                if contact in content:
                    listbox.selection_clear(0,'end')
                    contactIndex = content.index(contact)
                    listbox.delete(contactIndex)
                    listbox.insert(0,contact)
                    listbox.selection_set(0)
                    listbox.yview_moveto(0.0)
                    fname_entry.delete(0, 'end')
                    lname_entry.delete(0, 'end')
                    phone_no_entry.delete(0, 'end')
                    email_entry.delete(0, 'end')
                    address_entry.delete(0, 'end')
                    search_win.destroy()
                else:
                    lab.config(text=f'{contact} was not found!')
                    search_entry.delete(0,'end')

        search_win = Tk()
        search_win.geometry('420x80+460+270')
        search_win.title('Contact Book')
        search_win.config(bg='white')
        search_win.resizable(False, False)

        search_entry = Entry(search_win,font=('Baskerville',15),bg='white',fg='black',width=25)
        search_entry.place(x=27,y=20)

        search_button = Button(search_win,text='find',font=('Baskerville',10),bg='#fa3434',activebackground='#fa3434',fg='black',
                               activeforeground='black',bd=6,relief='raised',command=searchContact)
        search_button.place(x=340,y=16)

        lab = Label(search_win,text='', font=('Baskerville', 10),bg='white',fg='red')
        lab.pack(side='bottom',pady=5)

        search_win.mainloop()

    def removeContact(self):
        global contactSelected
        if contactSelected:
            contact = listbox.get(listbox.curselection())
            choice = messagebox.askquestion('delete contact',f'Are you sure you want to remove {contact}')
            if choice == 'yes':
                ind = listbox.curselection()
                listbox.delete(ind[0])

                L = []
                with open('contacts.txt') as f:
                    for i in f.readlines():
                        contacts = i.strip().split(',')
                        if len(x) == 2:
                            if x[0] in contacts and x[1] in contacts:
                                continue
                        elif len(x) == 3:
                            if x[0] in contacts and x[1] in contacts and x[2] in contacts:
                                continue
                        else:
                            if x[0] in contacts and x[1] in contacts and x[2] in contacts and x[3] in contacts:
                                continue
                        L.append(contacts)

                with open('contacts.txt', 'w') as f:
                    for contact in L:
                        f.write(','.join(contact) + '\n')

                fname_entry.delete(0, 'end')
                lname_entry.delete(0, 'end')
                phone_no_entry.delete(0, 'end')
                email_entry.delete(0, 'end')
                address_entry.delete(0, 'end')
            contactSelected = False


c = ContactBook()
##########################################################################################################################


def clearList():
    if len(listbox.get(0,'end')) > 0:
        confirm = messagebox.askquestion('clear contact list','Are you sure you want to clear all contacts?')
        if confirm == 'yes':
            listbox.delete(0,'end')
            fname_entry.delete(0,'end')
            lname_entry.delete(0,'end')
            phone_no_entry.delete(0,'end')
            email_entry.delete(0,'end')
            address_entry.delete(0,'end')
            with open('contacts.txt','w') as f:
                f.write('')
    else:
        messagebox.showerror('empty contact list','Contacts are already cleared!')


def selected(event):
    global contactSelected, x
    if len(listbox.get(0,'end')) > 0:
        contactSelected = True
        x = listbox.get(listbox.curselection()).split()
        with open('contacts.txt') as f:
            for i in f.readlines():
                contactList = i.split(',')
                if len(x) == 2:
                    if x[0] in contactList and x[1] in contactList:
                        cont = contactList
                elif len(x) == 3:
                    if x[0] in contactList and x[1] in contactList and x[2] in contactList:
                        cont = contactList
                else:
                    if x[0] in contactList and x[1] in contactList and x[2] in contactList and x[3] in contactList:
                        cont = contactList

            if len(cont) == 5:
                fName, lName, PhoneNo, Email, Address = cont[0], cont[1], cont[2], cont[3], cont[4]
            elif len(cont) == 6:
                fName, lName, PhoneNo, Email, Address = cont[0] + ' ' + cont[1], cont[2], cont[3], cont[4], cont[5]
            else:
                fName, lName, PhoneNo, Email, Address = cont[0] + ' ' + cont[1], cont[2] + ' ' + cont[3], cont[4], cont[5], cont[6]

            fname_entry.delete(0,'end')
            lname_entry.delete(0,'end')
            phone_no_entry.delete(0,'end')
            email_entry.delete(0,'end')
            address_entry.delete(0,'end')
            fname_entry.insert(0,fName)
            lname_entry.insert(0,lName)
            phone_no_entry.insert(0,PhoneNo)
            email_entry.insert(0,Email)
            address_entry.insert(0,Address)


while True:
    win = Tk()
    win.geometry('800x500+270+70')
    win.title('Contact Book')
    win.config(bg='white')
    icon = PhotoImage(file='contact-image.png')
    win.iconphoto(False,icon)
    win.resizable(False,False)

    Label(win,font=('Baskerville',36),bg=blue,width=200).place(x=0,y=0)

    exit_img = PhotoImage(file='exit icon.png')
    exit_btn = Button(win,image=exit_img,bg=blue,activebackground=blue,bd=5,relief='raised',command=quit)
    exit_btn.place(x=30,y=10)

    top_label = Label(win,text='CONTACT BOOK',font=('Baskerville',20,'bold'),fg=mint,bg=blue)
    top_label.place(x=270,y=15)

    contact_header = Label(win,text='Contact List',font=('Baskerville',12,'bold'),fg=blue,bg='white')
    contact_header.place(x=545,y=70)

    listbox_frame = Frame(win,width=29,height=10,bg='white')
    listbox_frame.pack(side='right',anchor='n',pady=90)

    scroller = Scrollbar(listbox_frame,orient='vertical',width=20)
    scroller.pack(side='right',fill='y')

    listbox = Listbox(listbox_frame,font=('Baskerville',15),width=29,height=10,bg=blue,fg=mint,
                      selectbackground=mint,yscrollcommand=scroller.set)
    listbox.pack()
    scroller.config(command=listbox.yview)
    listbox.bind('<ButtonRelease-1>',selected)

    detail_frame = Frame(win,width=400,height=380,bg=blue)
    detail_frame.place(x=10,y=90)

    f_name_lab = Label(detail_frame,text='First Name :',font=('Baskerville',15,'bold'),fg='white',bg=blue)
    f_name_lab.place(x=15,y=10)

    l_name_lab = Label(detail_frame,text='Last Name :',font=('Baskerville',15,'bold'),bg=blue,fg='white')
    l_name_lab.place(x=15,y=80)

    phone_lab = Label(detail_frame,text='Phone Number :',font=('Baskerville',15,'bold'),bg=blue,fg='white')
    phone_lab.place(x=15,y=150)

    email_lab = Label(detail_frame,text='Email :',font=('Baskerville',15,'bold'),bg=blue,fg='white')
    email_lab.place(x=15,y=220)

    address_lab = Label(detail_frame,text='Address :',font=('Baskerville',15,'bold'),bg=blue,fg='white')
    address_lab.place(x=15,y=290)

    fname_entry = Entry(detail_frame,font=('Baskerville',15,'bold'),fg=mint,bg=blue,width=28)
    fname_entry.place(x=15,y=40)

    lname_entry = Entry(detail_frame,font=('Baskerville',15,'bold'),fg=mint,bg=blue,width=28)
    lname_entry.place(x=15,y=110)

    phone_no_entry = Entry(detail_frame,font=('Baskerville',15,'bold'),fg=mint,bg=blue,width=28)
    phone_no_entry.place(x=15,y=180)

    email_entry = Entry(detail_frame,font=('Baskerville',15,'bold'),fg=mint,bg=blue,width=28)
    email_entry.place(x=15,y=250)

    address_entry = Entry(detail_frame,font=('Baskerville',15,'bold'),fg=mint,bg=blue,width=28)
    address_entry.place(x=15,y=320)

    add_btn = Button(win,text='Add',font=('Baskerville',10),bg='white',activebackground='white',fg='black',
                     activeforeground='black',bd=6,relief='raised',width=8,command=c.addContact)
    add_btn.place(x=460,y=390)

    remove_btn = Button(win,text='Remove',font=('Baskerville',10),bg='white',activebackground='white',fg='black',
                        activeforeground='black',bd=6,relief='raised',width=8,command=c.removeContact)
    remove_btn.place(x=560,y=390)

    search_btn = Button(win,text='Search',font=('Baskerville',10),bg='white',activebackground='white',fg='black',
                        activeforeground='black',bd=6,relief='raised',width=8,command=c.searchContact)
    search_btn.place(x=460,y=430)

    update_btn = Button(win,text='Update',font=('Baskerville',10),bg='white',activebackground='white',fg='black',
                        activeforeground='black',bd=6,relief='raised',width=8,command=c.updateContact)
    update_btn.place(x=660,y=390)

    load_btn = Button(win,text='load',font=('Baskerville',10),bg='white',width=8,activebackground='white',fg='black',
                      activeforeground='black',bd=6,relief='raised',command=c.viewContactList)
    load_btn.place(x=560,y=430)

    clear_btn = Button(win,text='clear',font=('Baskerville',10),bg='#fa3434',width=8,activebackground='#fa3434',fg='black',
                       activeforeground='black',bd=6,relief='raised',command=clearList)
    clear_btn.place(x=660,y=430)

    win.mainloop()




