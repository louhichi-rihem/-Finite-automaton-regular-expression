from textwrap import fill
from tkinter import *
from tkinter import font
from turtle import bgcolor, color
#import aut

def save_grammaire():
    grammaire_info=grammaire.get()
    etat_info=etat_finaeux.get()
    print(grammaire_info)
    print(etat_info)

    test_1=True
    test_2=True
    for g in grammaire_info :
        if not ("A"<=g<="Z" or g in ["a","b","-",">"," "]):
            test_1=False
            break

    for g in etat_info:
        if not ("A"<=g<="Z" or g==" "):
            test_2=False
            break
    if test_1 and test_2:
        file=open('grammaire.txt','w')
        L=grammaire_info.split(" ")
        for i in range(len(L)):
            file.write(L[i])
            file.write("\n")
        file.write(etat_info)
        #print("grammaire: ",grammaire_info," et les etats fineaux: ",etat_info," est dans le file ")
        file.close()
        print("grammaire: ",grammaire_info," et les etats fineaux: ",etat_info," est dans le file ")
        #return "grammaire: ",grammaire_info," et les etats fineaux: ",etat_info," est dans le file "
    else :
        rmq=Label(text="error")
        rmq.place(x=50,y=300)
        heading.pack()

def gram():
    
 import aut


screen= Tk()
screen.geometry("1000x500")
screen.title("automate")
heading=Label(text="automate",bg="grey",fg="black",width="500",height="3")
heading.pack()




gram=Label(text="la grammaire est:",font="20")
gram.place(x=450,y=100)
heading.pack()

etat=Label(text="les etats finale sont :",font="20")
etat.place(x=440,y=170)
heading.pack()


rmq=Label(text="NB : Utliliser a et b comme vocabulaire, les états sont dans [A..Z] ",fg="red")
rmq.place(x=10,y=350)
heading.pack()



grammaire=StringVar()
etat_finaeux=StringVar()


grammaire_entry=Entry(textvariable=grammaire ,width="100")
grammaire_entry.place(x=220,y=130)
etat_finaeux_entry=Entry(textvariable=etat_finaeux,width="60")
etat_finaeux_entry.place(x=340,y=200)




button = Button(screen,text = 'envoyer',width="30",command=save_grammaire,bg="grey",font="50")
button.place(x=350,y=250)


button = Button(screen,text = 'next',width="30",command=gram,bg="grey")
button.place(x=50,y=300)

heading.mainloop()
