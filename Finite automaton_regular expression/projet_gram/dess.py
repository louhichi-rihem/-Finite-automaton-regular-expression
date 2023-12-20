
from textwrap import fill
from tkinter import *
from turtle import bgcolor, color, width

def save_mot():
    mot_automate= mot.get()
    print(mot_automate)

    test=True 
    for g in mot_automate :
        if not (g in ["a","b","(",")","*","+"," "]):
            test=False
            break 
        if test:
            file=open('mot.txt','w')
        
        
            file.write(mot_automate)
            
        
        file.close()
        return "mot: ",mot_automate
    else :
        rmq=Label(text="error")
        rmq.place(x=100,y=300)
        canvas.pack() 

app = Tk()
app.geometry("1000x500")





def get_x_and_y(event):
    global lasx, lasy 
    lasx, lasy = event.x, event.y


def draw_smth(event):
    global lasx, lasy
    canvas.create_line((lasx, lasy, event.x, event.y ),fill="red",width=5)
    lasx,lasy= event.x,event.y


canvas = Canvas(app,bg='white')
canvas.create_text(500,10,text="dessiner votre automate",fill='black',font=50)
canvas.pack(anchor='n',fill='both',expand=1)

canvas.bind("<Button-1>", get_x_and_y)
canvas.bind("<B1-Motion>", draw_smth)


m=Label(text="donner le mot:")
m.place(x=460,y=380)
canvas.pack()

mot=StringVar()
mot_entry=Entry(textvariable=mot ,width="100")
mot_entry.place(x=170,y=400)

button = Button(app,text = 'envoyer',width="30",command=save_mot,bg="grey")
button.place(x=400,y=440)

app.mainloop()