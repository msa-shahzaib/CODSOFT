from tkinter import Tk, Label, Button, Entry, Radiobutton, IntVar, messagebox, PhotoImage
import random

msg = ''
name = ''
count = 0
won = 0
lose = 0
score = 0
games = 3
player = 'rock'


def high_score():
    main_win.destroy()
    hs_win = Tk()
    hs_win.geometry("620x450+370+110")
    hs_win.title("Top High Scores")
    hs_win.configure(bg="#0a0324")
    icon_image = PhotoImage(file='gameboy icon.png')
    hs_win.iconphoto(False,icon_image)
    hs_win.resizable(False,False)

    all_scores = []
    with open('high scores.txt') as f:
        for i in f.readlines():
            high_scores = i.strip('\n').split(':')
            all_scores.append(high_scores)

    sorted_list = sorted(all_scores,key=lambda s: int(s[-1]),reverse=True)
    mis_var = 3 - len(sorted_list)
    (name1, games1, won1, lose1, tie1, score1, name2, games2, won2, lose2, tie2, score2, name3, games3, won3, lose3,
     tie3, score3) = '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''

    if mis_var == 1:
        (name1, games1, won1, lose1, tie1, score1, name2, games2, won2, lose2, tie2, score2) = (
            sorted_list[0][0], sorted_list[0][1], sorted_list[0][2], sorted_list[0][3], sorted_list[0][4],
            sorted_list[0][5], sorted_list[1][0], sorted_list[1][1], sorted_list[1][2], sorted_list[1][3],
            sorted_list[1][4], sorted_list[1][5])

    elif mis_var == 2:
        name1, games1, won1, lose1, tie1, score1 = (sorted_list[0][0], sorted_list[0][1], sorted_list[0][2],
                                                    sorted_list[0][3], sorted_list[0][4],sorted_list[0][5])

    elif mis_var == 0 or mis_var < 0:
        (name1, games1, won1, lose1, tie1, score1, name2, games2, won2, lose2, tie2, score2, name3, games3, won3, lose3,
         tie3, score3) = (sorted_list[0][0], sorted_list[0][1], sorted_list[0][2], sorted_list[0][3], sorted_list[0][4],
                          sorted_list[0][5], sorted_list[1][0], sorted_list[1][1], sorted_list[1][2], sorted_list[1][3],
                          sorted_list[1][4], sorted_list[1][5], sorted_list[2][0], sorted_list[2][1], sorted_list[2][2],
                          sorted_list[2][3], sorted_list[2][4], sorted_list[2][5])

    mis1 = (10 - len(name1)) * 4
    mis2 = (10 - len(name2)) * 4
    mis3 = (10 - len(name3)) * 4
    scr1 = (3 - len(score1)) * 5
    scr2 = (3 - len(score2)) * 5
    scr3 = (3 - len(score3)) * 5

    header = Label(hs_win,text='HIGH SCORERS',font=("Helvetica",22,'bold'),fg="#9a48ab",bg="#0a0324")
    header.place(x=190,y=30)

    name_heading = Label(hs_win,text='Player',font=("Helvetica",18,'bold'),fg="#33c7d5",bg="#0a0324")
    name_heading.place(x=25,y=100)

    game_heading = Label(hs_win,text='Games',font=("Helvetica",18,'bold'),fg="#33c7d5",bg="#0a0324")
    game_heading.place(x=150,y=100)

    win_heading = Label(hs_win,text='Wins',font=("Helvetica",18,'bold'),fg="#33c7d5",bg="#0a0324")
    win_heading.place(x=260,y=100)

    lose_heading = Label(hs_win,text='Loses',font=("Helvetica",18,'bold'),fg="#33c7d5",bg="#0a0324")
    lose_heading.place(x=350,y=100)

    tie_heading = Label(hs_win,text='Ties',font=("Helvetica",18,'bold'),fg="#33c7d5",bg="#0a0324")
    tie_heading.place(x=445,y=100)

    score_heading = Label(hs_win,text='Score',font=("Helvetica",18,'bold'),fg="#33c7d5",bg="#0a0324")
    score_heading.place(x=525,y=100)

    name_label = Label(hs_win,text=name1.capitalize(),font=("Helvetica",16,'bold'),fg="#fcfcfc",bg="#0a0324")
    name_label.place(x=10 + mis1,y=160)

    games_played_lab = Label(hs_win,text=games1,font=("Helvetica",16,'bold'),fg="#fcfcfc",bg="#0a0324")
    games_played_lab.place(x=185,y=160)

    won_lab = Label(hs_win,text=won1,font=("Helvetica",16,'bold'),fg="#fcfcfc",bg="#0a0324")
    won_lab.place(x=285,y=160)

    lose_lab = Label(hs_win,text=lose1,font=("Helvetica",16,'bold'),fg="#fcfcfc",bg="#0a0324")
    lose_lab.place(x=380,y=160)

    tie_lab = Label(hs_win,text=tie1,font=("Helvetica",16,'bold'),fg="#fcfcfc",bg="#0a0324")
    tie_lab.place(x=465,y=160)

    score_lab = Label(hs_win,text=score1,font=("Helvetica",16,'bold'),fg="#fcfcfc",bg="#0a0324")
    score_lab.place(x=540 + scr1,y=160)

    name_label2 = Label(hs_win,text=name2.capitalize(),font=("Helvetica",16,'bold'),fg="#fcfcfc",bg="#0a0324")
    name_label2.place(x=10 + mis2,y=200)

    games_played_lab2 = Label(hs_win,text=games2,font=("Helvetica",16,'bold'),fg="#fcfcfc",bg="#0a0324")
    games_played_lab2.place(x=185,y=200)

    won_lab2 = Label(hs_win,text=won2,font=("Helvetica",16,'bold'),fg="#fcfcfc",bg="#0a0324")
    won_lab2.place(x=285,y=200)

    lose_lab2 = Label(hs_win,text=lose2,font=("Helvetica",16,'bold'),fg="#fcfcfc",bg="#0a0324")
    lose_lab2.place(x=380,y=200)

    tie_lab2 = Label(hs_win,text=tie2,font=("Helvetica",16,'bold'),fg="#fcfcfc",bg="#0a0324")
    tie_lab2.place(x=465,y=200)

    score_lab2 = Label(hs_win,text=score2,font=("Helvetica",16,'bold'),fg="#fcfcfc",bg="#0a0324")
    score_lab2.place(x=540 + scr2,y=200)

    name_label3 = Label(hs_win,text=name3.capitalize(),font=("Helvetica",16,'bold'),fg="#fcfcfc",bg="#0a0324")
    name_label3.place(x=10 + mis3,y=240)

    games_played_lab3 = Label(hs_win,text=games3,font=("Helvetica",16,'bold'),fg="#fcfcfc",bg="#0a0324")
    games_played_lab3.place(x=185,y=240)

    won_lab3 = Label(hs_win,text=won3,font=("Helvetica",16,'bold'),fg="#fcfcfc",bg="#0a0324")
    won_lab3.place(x=285,y=240)

    lose_lab3 = Label(hs_win,text=lose3,font=("Helvetica",16,'bold'),fg="#fcfcfc",bg="#0a0324")
    lose_lab3.place(x=380,y=240)

    tie_lab3 = Label(hs_win,text=tie3,font=("Helvetica",16,'bold'),fg="#fcfcfc",bg="#0a0324")
    tie_lab3.place(x=465,y=240)

    score_lab3 = Label(hs_win,text=score3,font=("Helvetica",16,'bold'),fg="#fcfcfc",bg="#0a0324")
    score_lab3.place(x=540 + scr3,y=240)

    main_menu_btn = Button(hs_win,text="Back",font=("Helvetica",14,"bold"),fg="#fcfcfc",bg="#9a48ab",relief="raised",
                           activebackground='#9a48ab',activeforeground='#fcfcfc',bd=10,command=hs_win.destroy)
    main_menu_btn.pack(side='bottom',pady=60)

    hs_win.mainloop()


def play_game():
    def select_games():
        global games
        if x.get() == 2:
            games = 7
        elif x.get() == 1:
            games = 5
        else:
            games = 3

    def submit():
        def player_choice():
            global player
            if y.get() == 2:
                player = 'scissors'
            elif y.get() == 1:
                player = 'paper'
            else:
                player = 'rock'

        def compute():
            def next_game():
                player_lab.destroy()
                player_choice_lab.destroy()
                comp_lab.destroy()
                comp_choice_lab.destroy()
                games_played.destroy()
                next_button.destroy()
                msg_lab.destroy()
                rock_rb.config(state='normal')
                paper_rb.config(state='normal')
                scissor_rb.config(state='normal')
                submit_btn.config(text='shoot',bd=8,relief='raised',bg='#9a48ab',state='normal')

            def results():
                global score, games, count, won, lose
                score = round(((won * 100) / (lose + 1)) + (games - won - lose) * 10)

                play_win.destroy()
                final_win = Tk()
                final_win.geometry("600x450+380+100")
                final_win.configure(bg="#0a0324")
                final_win.title("Game Review")
                icon_pic = PhotoImage(file='gameboy icon.png')
                final_win.iconphoto(False,icon_pic)
                final_win.resizable(False,False)

                ply_name = Label(final_win,text=f"\n< Player : {name.capitalize()} >",font=("Helvetica",20,'bold'),
                                 fg="#fcfcfc",bg="#0a0324")
                ply_name.pack(pady=5)

                if games == 3:
                    games_lab = Label(final_win,text='Best Of Three Game',font=("Helvetica",20,'bold'),fg="#fcfcfc",
                                      bg="#0a0324")
                    games_lab.pack(pady=5)

                elif games == 5:
                    games_lab = Label(final_win,text='Best Of Five Game',font=("Helvetica",20,'bold'),fg="#fcfcfc",
                                      bg="#0a0324")
                    games_lab.pack(pady=5)

                else:
                    games_lab = Label(final_win,text='Best Of Seven Game',font=("Helvetica",20,'bold'),fg="#fcfcfc",
                                      bg="#0a0324")
                    games_lab.pack(pady=5)

                wins = Label(final_win,text=f"Number of wins : {won}",font=("Helvetica",18,'bold'),fg="#fcfcfc",
                             bg="#0a0324")
                wins.pack(pady=5)

                loses = Label(final_win,text=f"Number of loses : {lose}",font=("Helvetica",18,'bold'),fg="#fcfcfc",
                              bg="#0a0324")
                loses.pack(pady=5)

                ties = Label(final_win,text=f"Number of ties : {games-won-lose}",font=("Helvetica",18,'bold'),
                             fg="#fcfcfc",bg="#0a0324")
                ties.pack(pady=5)

                score_lab = Label(final_win,text=f"Your score is: {score}",font=("Helvetica",22,'bold'),fg="#fcfcfc",
                                  bg="#0a0324")
                score_lab.pack(pady=20)

                main_menu = Button(final_win,text="main menu",font=("Helvetica",12,'bold'),bg="#9a48ab",fg="#fcfcfc",
                                   activeforeground='#fcfcfc',activebackground='#9a48ab',bd=8,relief="raised",
                                   command=final_win.destroy)
                main_menu.pack()

                final_win.mainloop()

                with open("high scores.txt","a") as f:
                    ties = games - won - lose
                    f.write(name + ":" + str(games) + ':' + str(won) + ':' + str(lose) + ':' + str(ties) + ":" +
                            str(score) + "\n")
                games, count, won, lose = 3, 0, 0, 0

            global msg, games, count, won, lose
            submit_btn.config(text='',bg='#0a0324',state='disabled',relief='flat',bd=0)
            rock_rb.config(state='disabled')
            paper_rb.config(state='disabled')
            scissor_rb.config(state='disabled')
            Set = ["paper", "scissors", "rock"]
            computer = random.choice(Set)

            if computer == player:
                msg = "Its a tie"
                count += 1

            else:
                if computer == "rock" and player == "paper":
                    msg = "Congratulations! You Won"
                    won += 1
                    count += 1

                elif computer == "scissors" and player == "paper":
                    msg = "You lost! Better luck next time"
                    lose += 1
                    count += 1

                elif computer == "rock" and player == "scissors":
                    msg = "You lost! Better luck next time"
                    lose += 1
                    count += 1

                elif computer == "paper" and player == "scissors":
                    msg = "Congratulations! You Won"
                    won += 1
                    count += 1

                elif computer == "paper" and player == "rock":
                    msg = "You lost! Better luck next time"
                    lose += 1
                    count += 1

                elif computer == "scissors" and player == "rock":
                    msg = "Congratulations! You Won"
                    won += 1
                    count += 1

            player_lab = Label(play_win,text='your choice :',font=("Helvetica",17,'bold'),fg="#fcfcfc",bg="#0a0324")
            player_lab.place(x=170,y=200)

            comp_lab = Label(play_win,text='comp choice :',font=("Helvetica",17,'bold'),fg="#fcfcfc",bg="#0a0324")
            comp_lab.place(x=170,y=230)

            player_choice_lab = Label(play_win,text=player,font=("Helvetica",17,'bold'),fg="#33c7d5",bg="#0a0324")
            player_choice_lab.place(x=330,y=200)

            comp_choice_lab = Label(play_win,text=computer,font=("Helvetica",17,'bold'),fg="#33c7d5",bg="#0a0324")
            comp_choice_lab.place(x=340,y=230)

            msg_lab = Label(play_win,text='| ' + msg + ' |',font=("Helvetica",20,"bold"),fg="#fcfcfc",bg="#0a0324")
            msg_lab.pack(side='bottom',pady=120)

            games_played = Label(play_win,text="Games Played : " + str(count) + " / " + str(games),
                                 font=("Helvetica",16,'bold'),fg="#fcfcfc",bg="#0a0324")
            games_played.place(x=195,y=340)

            if count < games:
                next_button = Button(play_win,text="Next Round",font=("Helvetica",12,'bold'),bg="#9a48ab",fg="#fcfcfc"
                                     ,activeforeground='#fcfcfc',activebackground='#9a48ab',bd=8,relief="raised",
                                     command=next_game)
                next_button.place(x=245,y=380)

            elif count == games:
                result_button = Button(play_win,text="View Results",font=("Helvetica",12,'bold'),bg="#9a48ab",
                                       fg="#fcfcfc",activeforeground='#fcfcfc',activebackground='#9a48ab',bd=8,
                                       relief="raised",command=results)
                result_button.place(x=240,y=380)

        global name
        name = name_entry.get()

        if name == '':
            messagebox.showerror('Entry error','name is required to proceed')

        else:
            player_name = name_entry.get().capitalize()
            id_win.destroy()

            play_win = Tk()
            play_win.geometry("600x450+380+100")
            play_win.title("Rock Paper Scissors Game")
            play_win.configure(bg='#0a0324')
            icon_image = PhotoImage(file='gameboy icon.png')
            play_win.iconphoto(False,icon_image)
            play_win.resizable(False,False)

            name_display_lab = Label(play_win,text="Hey there " + player_name,font=("Helvetica",20,"bold"),fg="#fcfcfc"
                                     ,bg="#0a0324")
            name_display_lab.pack(pady=10)

            pc_lab = Label(play_win,text="Select Rock Paper or Scissors",font=("Helvetica",15,'bold'),fg="#fcfcfc",
                           bg="#0a0324")
            pc_lab.place(x=150,y=60)

            rock_img = PhotoImage(file='rock sign.png')
            paper_img = PhotoImage(file='paper icon.png')
            scissor_img = PhotoImage(file='scissor icon.png')

            y = IntVar()
            rock_rb = Radiobutton(play_win,image=rock_img,bg='#26006e',activebackground='#26006e',variable=y,value=0,
                                  indicatoron=False,bd=6,relief='raised',selectcolor='#26006e',command=player_choice)
            rock_rb.place(x=170,y=100)

            paper_rb = Radiobutton(play_win,image=paper_img,bg='#26006e',activebackground='#26006e',variable=y,value=1,
                                   indicatoron=False,bd=6,relief='raised',selectcolor='#26006e',command=player_choice)
            paper_rb.place(x=260,y=100)

            scissor_rb = Radiobutton(play_win,image=scissor_img,bg='#26006e',activebackground='#26006e',variable=y,
                                     value=2,indicatoron=False,bd=6,relief='raised',selectcolor='#26006e',
                                     command=player_choice)
            scissor_rb.place(x=350,y=100)

            submit_btn = Button(play_win,text="shoot",font=("Helvetica",14,'bold'),bg="#9a48ab",fg="#fcfcfc",bd=8,
                                relief="raised",activeforeground='#fcfcfc',activebackground='#9a48ab',command=compute)
            submit_btn.place(x=260,y=230)

            play_win.mainloop()

    global name_entry
    main_win.destroy()
    id_win = Tk()
    id_win.geometry("600x450+380+100")
    id_win.title("ID Configuration")
    id_win.configure(bg='#0a0324')
    icon_img = PhotoImage(file='gameboy icon.png')
    id_win.iconphoto(False,icon_img)
    id_win.resizable(False,False)

    def text_limit(P):
        return len(P) <= 10

    name_lab = Label(id_win,text="\nEnter Your Name",font=("Helvetica",20,'bold'),fg="#fcfcfc",bg="#0a0324")
    name_lab.pack()

    name_register = id_win.register(text_limit)
    name_entry = Entry(id_win,font=("Helvetica",18,'bold'),fg="black",bg="#a4aba6",width=28,validate='key',
                       validatecommand=(name_register,'%P'))
    name_entry.pack(pady=10)

    game_lab = Label(id_win,text="\nSet number of games",font=("Helvetica",20,'bold'),fg="#fcfcfc",bg="#0a0324")
    game_lab.pack(pady=5)

    options = ['Best of Three','Best Of Five','Best Of Seven']
    x = IntVar()
    for i in range(len(options)):
        radiobutton = Radiobutton(id_win,text=options[i],font=("Helvetica",12,'bold'),bg="#33c7d5",fg="#080808",
                                  width=20,activeforeground='#080808',activebackground='#33c7d5',relief='raised',bd=6,
                                  indicatoron=False,variable=x,value=i,selectcolor='#33c7d5',command=select_games)
        radiobutton.pack(pady=5)

    submit_button = Button(id_win,text="submit",font=("Helvetica",14,'bold'),bd=8,relief="raised",bg="#9a48ab",
                           fg="#fcfcfc",activebackground='#9a48ab',activeforeground='#fcfcfc',width=8,command=submit)
    submit_button.pack(side='bottom',pady=20)

    id_win.mainloop()


while True:
    main_win = Tk()
    main_win.geometry("600x450+380+100")
    main_win.configure(bg="#0a0324")
    main_win.title("Rock Paper Scissors Game")
    icon = PhotoImage(file='gameboy icon.png')
    main_win.iconphoto(False,icon)
    main_win.resizable(False,False)

    header_img = PhotoImage(file='main interface pic.PNG')
    welcome = Label(main_win,image=header_img,bg="#0a0324")
    welcome.pack()

    Label(main_win,text='',bg="#0a0324",font=("Helvetica",12)).pack()

    pl_game = Button(main_win,text="Play Game",font=("Helvetica",20,'bold'),bg="#9a48ab",fg="#fcfcfc",bd=8,
                     relief="raised",activebackground='#9a48ab',activeforeground='#fcfcfc',command=play_game,width=10)
    pl_game.pack(pady=5)

    High_score = Button(main_win,text="High Scores",font=("Helvetica",20,'bold'),bg="#9a48ab",fg="#fcfcfc",
                        relief="raised",activebackground='#9a48ab',activeforeground='#fcfcfc',bd=8,width=10,
                        command=high_score)
    High_score.pack(pady=5)

    Quit = Button(main_win,text="Quit Game",font=("Helvetica",20,'bold'),bg="#9a48ab",fg="#fcfcfc",bd=8,relief="raised"
                  ,activebackground='#9a48ab',activeforeground='#fcfcfc',command=quit,width=10)
    Quit.pack(pady=5)

    main_win.mainloop()

