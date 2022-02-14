from cgitb import text
from sre_parse import State
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import os

Personaje=0
nombre=""
nombre2=""
rival=0
t1=""
t2=""
train = Tk()
train.geometry('1300x950')
train.config(bg='#F7DE79')
train.title("Elige a tu pokemon")
train.resizable(False, False)
a= "C:\\Users\\chris\\Documents\\IALabSchool\\Imagenes\\"
#imagenes de pokemon
aquanderimg = Image.open(a+'aquarder.png')
tk_aquanderimg = ImageTk.PhotoImage(aquanderimg)
aquanderdet = Image.open(a+'detaquarder.png')
tk_aquanderdet = ImageTk.PhotoImage(aquanderdet)

electderimg = Image.open(a+'electder.png')
tk_electderimg = ImageTk.PhotoImage(electderimg)
electerdet = Image.open(a+'detelecter.png')
tk_electerdet = ImageTk.PhotoImage(electerdet)

firesorimg = Image.open(a+'firesor.png')
tk_firesorimg = ImageTk.PhotoImage(firesorimg)
firesordet = Image.open(a+'detfiresor.png')
tk_firesordet = ImageTk.PhotoImage(firesordet)

mouseimg = Image.open(a+'mousebug.png')
tk_mouseimg = ImageTk.PhotoImage(mouseimg)
mousedet = Image.open(a+'detmousebug.png')
tk_mousedet = ImageTk.PhotoImage(mousedet)

splantimg = Image.open(a+'splant.png')
tk_splantimg = ImageTk.PhotoImage(splantimg)
splantdet = Image.open(a+'detsplant.png')
tk_splantdet = ImageTk.PhotoImage(splantdet)

rockdogimg = Image.open(a+'rockdog.png')
tk_rockdogimg = ImageTk.PhotoImage(rockdogimg)
rockdogdet = Image.open(a+'detrockdog.png')
tk_rockdogdet = ImageTk.PhotoImage(rockdogdet)

imgpokedex= Image.open(a+'pokedex.png')
tk_imgpokedex = ImageTk.PhotoImage(imgpokedex)


#botones de detalles de pokemones 
def detaquander():
    detalleaquander = Toplevel()
    detalleaquander.geometry('1000x480')
    detalleaquander.resizable(False, False)
    canvas5 = Canvas(detalleaquander, width=1000, height=500)
    canvas5.create_image( 0, 0, image = tk_imgpokedex, anchor = "nw")
    canvas5.pack(fill = "both", expand= True)   
    detalleaquander.title('Detalles Aquander')
        # tabla = Treeview(detalleaquander, columns=("col1","col2","col3","col4","col5","col6"))
        # tabla1 = Treeview(detalleaquander, columns=("col1","col2"))

    pokedeximg= Label(detalleaquander, image=tk_aquanderimg, width=200, height=200)
    pokedeximg.place(x=620, y=10)
    labelname = Label(detalleaquander, text= "Aquander: Tipo Agua",font=("times",20,"bold"))
    labelname.place(x=250, y=30)
    labelname1 = Label(detalleaquander, text= "Ventaja con: Roca, Fuego",font=("times",15,"bold"))
    labelname1.place(x=20, y=120)
    labelname2 = Label(detalleaquander, text= "Desventaja con: Electrico, Planta",font=("times",15,"bold"))
    labelname2.place(x=20, y=150)
    labelname3 = Label(detalleaquander, text= "Normal con: Agua, Escarabajo",font=("times",15,"bold"))
    labelname3.place(x=20, y=180)

    habimg= Label(detalleaquander, image=tk_aquanderdet, width=983, height=206)
    habimg.place(x=10,y=230)

def detelecter():
    detalleelecter = Toplevel()
    detalleelecter.geometry('1000x480')
    detalleelecter.resizable(False, False)
    canvas5 = Canvas(detalleelecter, width=1000, height=500)
    canvas5.create_image( 0, 0, image = tk_imgpokedex, anchor = "nw")
    canvas5.pack(fill = "both", expand= True)   

    detalleelecter.title('Detalles Aquander')

    pokedeximg= Label(detalleelecter, image=tk_electderimg, width=200, height=200)
    pokedeximg.place(x=620, y=10)
    labelname = Label(detalleelecter, text= "Electer: Tipo Eléctrico",font=("times",20,"bold"))
    labelname.place(x=250, y=30)
    labelname1 = Label(detalleelecter, text= "Ventaja con: Agua, Escarabajo",font=("times",15,"bold"))
    labelname1.place(x=20, y=120)
    labelname2 = Label(detalleelecter, text= "Desventaja con: Roca, Planta",font=("times",15,"bold"))
    labelname2.place(x=20, y=150)
    labelname3 = Label(detalleelecter, text= "Normal con: Electrico, Fuego",font=("times",15,"bold"))
    labelname3.place(x=20, y=180)

    habimg= Label(detalleelecter, image=tk_electerdet, width=983, height=206)
    habimg.place(x=10,y=230)
    
def detfiresor():
    detallefiresor = Toplevel()
    detallefiresor.geometry('1000x480')
    detallefiresor.resizable(False, False)
    canvas5 = Canvas(detallefiresor, width=1000, height=500)
    canvas5.create_image( 0, 0, image = tk_imgpokedex, anchor = "nw")
    canvas5.pack(fill = "both", expand= True)   

    detallefiresor.title('Detalles Firesor')

    pokedeximg= Label(detallefiresor, image=tk_firesorimg, width=200, height=200)
    pokedeximg.place(x=620, y=10)
    labelname = Label(detallefiresor, text= "Firesor: Tipo Fuego",font=("times",20,"bold"))
    labelname.place(x=250, y=30)
    labelname1 = Label(detallefiresor, text= "Ventaja con: Planta, Escarabajo",font=("times",15,"bold"))
    labelname1.place(x=20, y=120)
    labelname2 = Label(detallefiresor, text= "Desventaja con: Agua, Roca",font=("times",15,"bold"))
    labelname2.place(x=20, y=150)
    labelname3 = Label(detallefiresor, text= "Normal con: Electrico, Fuego",font=("times",15,"bold"))
    labelname3.place(x=20, y=180)

    habimg= Label(detallefiresor, image=tk_firesordet, width=983, height=206)
    habimg.place(x=10,y=230)

def detmousebug():
    detallemouse = Toplevel()
    detallemouse.geometry('1000x480')
    detallemouse.resizable(False, False)
    canvas5 = Canvas(detallemouse, width=1000, height=500)
    canvas5.create_image( 0, 0, image = tk_imgpokedex, anchor = "nw")
    canvas5.pack(fill = "both", expand= True)   

    detallemouse.title('Detalles Mousebug')

    pokedeximg= Label(detallemouse, image=tk_mouseimg, width=200, height=200)
    pokedeximg.place(x=620, y=10)
    labelname = Label(detallemouse, text= "Mousebug: Tipo Escarabajo",font=("times",20,"bold"))
    labelname.place(x=250, y=30)
    labelname1 = Label(detallemouse, text= "Ventaja con: Planta, Roca",font=("times",15,"bold"))
    labelname1.place(x=20, y=120)
    labelname2 = Label(detallemouse, text= "Desventaja con: Fuego, Electrico",font=("times",15,"bold"))
    labelname2.place(x=20, y=150)
    labelname3 = Label(detallemouse, text= "Normal con: Escarabajo, Agua",font=("times",15,"bold"))
    labelname3.place(x=20, y=180)

    habimg= Label(detallemouse, image=tk_mousedet, width=983, height=206)
    habimg.place(x=10,y=230)

def detsplant():
    detallesplant= Toplevel()
    detallesplant.geometry('1000x480')
    detallesplant.resizable(False, False)
    canvas5 = Canvas(detallesplant, width=1000, height=500)
    canvas5.create_image( 0, 0, image = tk_imgpokedex, anchor = "nw")
    canvas5.pack(fill = "both", expand= True)   

    detallesplant.title('Detalles Splant')

    pokedeximg= Label(detallesplant, image=tk_splantimg, width=200, height=200)
    pokedeximg.place(x=620, y=10)
    labelname = Label(detallesplant, text= "Splant: Tipo Planta",font=("times",20,"bold"))
    labelname.place(x=250, y=30)
    labelname1 = Label(detallesplant, text= "Ventaja con: Agua, Roca, Eléctrico",font=("times",15,"bold"))
    labelname1.place(x=20, y=120)
    labelname2 = Label(detallesplant, text= "Desventaja con: Fuego, Escarabajo",font=("times",15,"bold"))
    labelname2.place(x=20, y=150)
    labelname3 = Label(detallesplant, text= "Normal con: Planta",font=("times",15,"bold"))
    labelname3.place(x=20, y=180)

    habimg= Label(detallesplant, image=tk_splantdet, width=983, height=206)
    habimg.place(x=10,y=230)

def detrockdog():
    detallerockdog= Toplevel()
    detallerockdog.geometry('1000x480')
    detallerockdog.resizable(False, False)
    canvas5 = Canvas(detallerockdog, width=1000, height=500)
    canvas5.create_image( 0, 0, image = tk_imgpokedex, anchor = "nw")
    canvas5.pack(fill = "both", expand= True)   

    detallerockdog.title('Detalles Rockdog')

    pokedeximg= Label(detallerockdog, image=tk_splantimg, width=200, height=200)
    pokedeximg.place(x=620, y=10)
    labelname = Label(detallerockdog, text= "Rockdog: Tipo Roca",font=("times",20,"bold"))
    labelname.place(x=250, y=30)
    labelname1 = Label(detallerockdog, text= "Ventaja con: Fuego, Eléctrico",font=("times",15,"bold"))
    labelname1.place(x=20, y=120)
    labelname2 = Label(detallerockdog, text= "Desventaja con: Agua, Planta",font=("times",15,"bold"))
    labelname2.place(x=20, y=150)
    labelname3 = Label(detallerockdog, text= "Normal con: Escarabajo, Roca",font=("times",15,"bold"))
    labelname3.place(x=20, y=180)

    habimg= Label(detallerockdog, image=tk_splantdet, width=983, height=206)
    habimg.place(x=10,y=230)

#seleccion de personaje
def a1():
    global nombre
    global nombre2
    global bandera
    global Personaje
    global rival
    global t1
    global t2
    if (bandera ==0):
        nombre = "Aquarder"
        t1= "Agua"
        bandera=1
        Personaje=1
        pokeaquander.config(bg="red")
        messagebox.showinfo(message="Selecciona tu contricante", title="Contricante")
    else:
        if (Personaje==1):
            pokeaquander.config(bg="pink")
        else:
            pokeaquander.config(bg="blue")
        nombre2="Aquarder"
        t2="Agua"
        bandera=2
        rival=1
        btnTrain.config(state=NORMAL)
        pokeaquander.config(state=DISABLED)
        pokeelectder.config(state=DISABLED)
        pokefiresor.config(state=DISABLED)
        pokemouse.config(state=DISABLED)
        pokesplant.config(state=DISABLED)
        pokerockdog.config(state=DISABLED)
        print("personaje: "+str(Personaje))
        print("nombre "+nombre)
        print("TipoPlayer "+t1)
        print("rival "+str(rival))
        print("nombre2 "+nombre2)
        print("TipoRival "+t2)

def a2():
    global nombre
    global nombre2
    global bandera
    global Personaje
    global rival
    global t1
    global t2
    if (bandera ==0):
        nombre = "Electder"
        t1= "Electrico"
        bandera=1
        Personaje=2
        pokeelectder.config(bg="red")
        messagebox.showinfo(message="Selecciona tu contricante", title="Contricante")
    else:
        if (Personaje==2):
            pokeelectder.config(bg="pink")
        else:
            pokeelectder.config(bg="blue")
        nombre2="Electder"
        t2="Electrico"
        bandera=2
        rival=2
        btnTrain.config(state=NORMAL)
        pokeaquander.config(state=DISABLED)
        pokeelectder.config(state=DISABLED)
        pokefiresor.config(state=DISABLED)
        pokemouse.config(state=DISABLED)
        pokesplant.config(state=DISABLED)
        pokerockdog.config(state=DISABLED)
        print("personaje: "+str(Personaje))
        print("nombre "+nombre)
        print("TipoPlayer "+t1)
        print("rival "+str(rival))
        print("nombre2 "+nombre2)
        print("TipoRival "+t2)

def a3():
    global nombre
    global nombre2
    global bandera
    global Personaje
    global rival
    global t1
    global t2
    if (bandera ==0):
        nombre = "Firesor"
        t1= "Fuego"
        bandera=1
        Personaje=3
        pokefiresor.config(bg="red")
        messagebox.showinfo(message="Selecciona tu contricante", title="Contricante")
    else:
        if (Personaje==3):
            pokefiresor.config(bg="pink")
        else:
            pokefiresor.config(bg="blue")
        nombre2="Electder"
        t2="Electrico"
        bandera=2
        rival=3
        btnTrain.config(state=NORMAL)
        pokeaquander.config(state=DISABLED)
        pokeelectder.config(state=DISABLED)
        pokefiresor.config(state=DISABLED)
        pokemouse.config(state=DISABLED)
        pokesplant.config(state=DISABLED)
        pokerockdog.config(state=DISABLED)
        print("personaje: "+str(Personaje))
        print("nombre "+nombre)
        print("TipoPlayer "+t1)
        print("rival "+str(rival))
        print("nombre2 "+nombre2)
        print("TipoRival "+t2)

def a4():
    global nombre
    global nombre2
    global bandera
    global Personaje
    global rival
    global t1
    global t2
    if (bandera ==0):
        nombre = "MouseBug"
        t1= "Escarabajo"
        bandera=1
        Personaje=4
        pokemouse.config(bg="red")
        messagebox.showinfo(message="Selecciona tu contricante", title="Contricante")
    else:
        if (Personaje==4):
            pokemouse.config(bg="pink")
        else:
            pokemouse.config(bg="blue")
        nombre2="MouseBug"
        t2="Escarabajo"
        bandera=2
        rival=4
        btnTrain.config(state=NORMAL)
        pokeaquander.config(state=DISABLED)
        pokeelectder.config(state=DISABLED)
        pokefiresor.config(state=DISABLED)
        pokemouse.config(state=DISABLED)
        pokesplant.config(state=DISABLED)
        pokerockdog.config(state=DISABLED)
        print("personaje: "+str(Personaje))
        print("nombre "+nombre)
        print("TipoPlayer "+t1)
        print("rival "+str(rival))
        print("nombre2 "+nombre2)
        print("TipoRival "+t2)
def a5():
    global nombre
    global nombre2
    global bandera
    global Personaje
    global rival
    global t1
    global t2
    if (bandera ==0):
        nombre = "Splant"
        t1= "Planta"
        bandera=1
        Personaje=5
        pokesplant.config(bg="red")
        messagebox.showinfo(message="Selecciona tu contricante", title="Contricante")
    else:
        if (Personaje==5):
            pokesplant.config(bg="pink")
        else:
            pokesplant.config(bg="blue")
        nombre2="Splant"
        t2="Planta"
        bandera=2
        rival=5
        btnTrain.config(state=NORMAL)
        pokeaquander.config(state=DISABLED)
        pokeelectder.config(state=DISABLED)
        pokefiresor.config(state=DISABLED)
        pokemouse.config(state=DISABLED)
        pokesplant.config(state=DISABLED)
        pokerockdog.config(state=DISABLED)
        print("personaje: "+str(Personaje))
        print("nombre "+nombre)
        print("TipoPlayer "+t1)
        print("rival "+str(rival))
        print("nombre2 "+nombre2)
        print("TipoRival "+t2)

def a6():
    global nombre
    global nombre2
    global bandera
    global Personaje
    global rival
    global t1
    global t2
    if (bandera ==0):
        nombre = "Rockdog"
        t1= "Roca"
        bandera=1
        Personaje=6
        pokerockdog.config(bg="red")
        messagebox.showinfo(message="Selecciona tu contricante", title="Contricante")
    else:
        if (Personaje==6):
            pokerockdog.config(bg="pink")
        else:
            pokerockdog.config(bg="blue")
        nombre2="Rockdog"
        t2="Roca"
        bandera=2
        rival=3
        btnTrain.config(state=NORMAL)
        pokeaquander.config(state=DISABLED)
        pokeelectder.config(state=DISABLED)
        pokefiresor.config(state=DISABLED)
        pokemouse.config(state=DISABLED)
        pokesplant.config(state=DISABLED)
        pokerockdog.config(state=DISABLED)
        print("************************")
        print("Datos seleccion")
        print("personaje: "+str(Personaje))
        print("nombre "+nombre)
        print("TipoPlayer "+t1)
        print("rival "+str(rival))
        print("nombre2 "+nombre2)
        print("TipoRival "+t2)



def iniciar():
    global nombre
    global nombre2
    global bandera
    global Personaje
    global rival
    global t1
    global t2
    res=messagebox.askyesno(message="¿Listo?",title="Elige a tu pokemon")
    if(res == True):
        if(Personaje!=0) or (rival!=0):
            print("Ok")
            train.destroy()
            import CombateEntrenamiento
            CombateEntrenamiento.batalla(Personaje,rival,nombre,nombre2,t1,t2)
        else:
            messagebox.showerror(message="Selecciona ambos personajes", title="Error")
    else:
        messagebox.showinfo(message="Selecciona tu personaje", title="Personaje")
        bandera = 0
        Personaje = 0
        rival = 0
        btnTrain.config(state=DISABLED)
        pokeaquander.config(state=DISABLED, bg="gray")
        pokeelectder.config(state=DISABLED, bg="gray")
        pokefiresor.config(state=DISABLED, bg="gray")
        pokemouse.config(state=DISABLED, bg="gray")
        pokesplant.config(state=DISABLED, bg="gray")
        pokerockdog.config(state=DISABLED, bg="gray")



#primer ventana emergente
messagebox.showinfo(message="Selecciona tu personaje",title="Personaje")
bandera= 0
l1 = Label(train, text="Elige a tu pokemon!",width=25,font=("times",20,"bold italic"),bg='#F0F9F0',fg='black')
l1.place(x=350,y=20)

aquanderlab= Label(train, text="Aquander",width=25,font=("times",12),bg='#F0F9F0',fg='black')
aquanderlab.place(x=50,y=80)
pokeaquander= Button(train, image=tk_aquanderimg, width=300, height=300, command= a1)
pokeaquander.place(x=20, y=120)
det1= Button(train, text="Detalles", height=2, width=16, command= detaquander)
det1.place(x=110, y= 440)

labelectder= Label(train, text="Electder",width=25,font=("times",12),bg='#F0F9F0',fg='black')
labelectder.place(x=400,y=80)
pokeelectder= Button(train, image=tk_electderimg, width=300, height=300,command= a2)
pokeelectder.place(x=340, y=120)
det2= Button(train, text="Detalles", width=16, height=2, command=detelecter) 
det2.place(x=400, y= 440)

labfiresor= Label(train, text="Firesor",width=25,font=("times",12),bg='#F0F9F0',fg='black')
labfiresor.place(x=710,y=80)
pokefiresor= Button(train, image=tk_firesorimg, width=300, height=300, command= a3)
pokefiresor.place(x=660, y=120)
defiresor = Button(train, text="Detalles", width=16, height=2, command= detfiresor)
defiresor.place(x=710, y= 440)

labmouse= Label(train, text="Mousebug",width=25,font=("times",12),bg='#F0F9F0',fg='black')
labmouse.place(x=1050,y=80)
pokemouse= Button(train, image=tk_mouseimg, width=300, height=300, command= a4)
pokemouse.place(x=980, y=120)
detmouse= Button(train, text="Detalles", width=16, height=2, command=detmousebug)
detmouse.place(x=1050, y= 440)

labsplant= Label(train, text="Splant",width=25,font=("times",12),bg='#F0F9F0',fg='black')
labsplant.place(x=50,y=520)
pokesplant= Button(train, image=tk_splantimg, width=300, height=300, command= a5)
pokesplant.place(x=20, y=550)
desplant= Button(train, text="Detalles", width=16, height=2, command=detsplant)
desplant.place(x=110, y= 870)  

labrockdog= Label(train, text="Rockdog",width=25,font=("times",12),bg='#F0F9F0',fg='black')
labrockdog.place(x=1050,y=520)
pokerockdog= Button(train, image=tk_rockdogimg, width=300, height=300, command= a6)
pokerockdog.place(x=980, y=550)
derockdog= Button(train, text="Detalles", width=16, height=2, command=detrockdog)
derockdog.place(x=1050, y= 870)  

pokeaquander.config(state=NORMAL, bg="gray")
pokeelectder.config(state=NORMAL, bg="gray")
pokefiresor.config(state=NORMAL, bg="gray")
pokemouse.config(state=NORMAL, bg="gray")
pokesplant.config(state=NORMAL, bg="gray")
pokerockdog.config(state=NORMAL, bg="gray")

btnTrain= Button(train, text="Iniciar combate",height= 5, width=26, font=("times",15,"bold"), bg= "#1DD81E", fg="black",state=DISABLED, command= iniciar)
btnTrain.place(x=500, y= 600)

train.mainloop()