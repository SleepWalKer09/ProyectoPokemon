"""
Proyecto Final
Instrucciones aqui:
https://classroom.google.com/c/NDE1MTM0NDc4ODk0/a/NDU3Mzg4NzQyMDI0/details
"""
from logging import _Level
from random import random
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
from PIL import Image, ImageTk
import csv
from numpy import dtype
import pandas as pd
from os import getcwd
import os

aquander = 1
electer = 2
firesor = 3
mousebug = 4
splant = 5
rockdog = 6
vida = 25

principal = Tk()
principal.geometry('520x540')

canvas1 = Canvas( principal, width=400, height=400)
canvas1.pack(fill = "both", expand= True)
a= getcwd()
#Imagenes, fondos de ventana, valores combate
bg = PhotoImage(master = canvas1, file = "Imagenes\BGPrincipal.png") 
im = Image.open("Imagenes\TituloJuego.png")
ph = ImageTk.PhotoImage(im)
imgmenu= Image.open(a+'\\Imagenes\\menu.png')
tk_imgmenu = ImageTk.PhotoImage(imgmenu)
imgpokedex= Image.open(a+'\\Imagenes\\pokedex.png')
tk_imgpokedex = ImageTk.PhotoImage(imgpokedex)
# imggym = Image.open(a+'\\Imagenes\\gym.png')
# tk_imggym = ImageTk.PhotoImage(imggym)

aquanderimg = Image.open(a+'\\Imagenes\\aquarder.png')
tk_aquanderimg = ImageTk.PhotoImage(aquanderimg)
aquanderdet = Image.open(a+'\\Imagenes\\detaquarder.png')
tk_aquanderdet = ImageTk.PhotoImage(aquanderdet)

electderimg = Image.open(a+'\\Imagenes\\electder.png')
tk_electderimg = ImageTk.PhotoImage(electderimg)
electerdet = Image.open(a+'\\Imagenes\\detelecter.png')
tk_electerdet = ImageTk.PhotoImage(electerdet)

firesorimg = Image.open(a+'\\Imagenes\\firesor.png')
tk_firesorimg = ImageTk.PhotoImage(firesorimg)
firesordet = Image.open(a+'\\Imagenes\\detfiresor.png')
tk_firesordet = ImageTk.PhotoImage(firesordet)

mouseimg = Image.open(a+'\\Imagenes\\mousebug.png')
tk_mouseimg = ImageTk.PhotoImage(mouseimg)
mousedet = Image.open(a+'\\Imagenes\\detmousebug.png')
tk_mousedet = ImageTk.PhotoImage(mousedet)

splantimg = Image.open(a+'\\Imagenes\\splant.png')
tk_splantimg = ImageTk.PhotoImage(splantimg)
splantdet = Image.open(a+'\\Imagenes\\detsplant.png')
tk_splantdet = ImageTk.PhotoImage(splantdet)

rockdogimg = Image.open(a+'\\Imagenes\\rockdog.png')
tk_rockdogimg = ImageTk.PhotoImage(rockdogimg)
rockdogdet = Image.open(a+'\\Imagenes\\detrockdog.png')
tk_rockdogdet = ImageTk.PhotoImage(rockdogdet)


canvas1.create_image( 0, 0, image = bg, anchor = "nw")

titulo = Label(canvas1, image= ph, width=500)
titulo.place(x=10, y=50)


principal.title("Menu Principal")
principal.resizable(False, False)


#Si se desea iniciar sesión se buscara un archivo csv con el nombre del usuario indicado, y dentro del archivo se validara una contraseña.
def IniciarSesion():
    global InicioSesion
    InicioSesion = Toplevel()#Nueva Ventana Independiente
    principal.withdraw()#Esconde la Ventana Anterior
    InicioSesion.geometry('520x540')

    InicioSesion.title("Inicio Sesion")
    InicioSesion.resizable(False, False)

    canvas2 = Canvas(InicioSesion, width=400, height=400)
    canvas2.pack(fill = "both", expand= True)
    canvas2.create_image( 0, 0, image = bg, anchor = "nw")

    titulosesion = Label(canvas2, image= ph, width=500)
    titulosesion.place(x=10, y=10)
    titulosesion.image=ph

    l1 = Label(InicioSesion, text="Inicia Sesión",width=25,font=("times",20,"bold"),bg='#F0F9F0',fg='black')
    l1.place(x=70,y=100)
    
    labeluser= Label(InicioSesion, text="Usuario",font=("times",15,"bold"))
    labeluser.place( x= 70, y=150)
    e1 = Entry(InicioSesion,width=30,bd=2)
    e1.place(x=70,y=170)
    
    labelpass= Label(InicioSesion, text="Contraseña", font=("times",15,"bold"))
    labelpass.place( x= 70, y=250)
    e2 = Entry(InicioSesion,width=30,bd=2)
    e2.place(x=70,y=270)

    def Ingresar():
        global usuario
        global Level
        usuario = e1.get()
        contra =e2.get()
        
        bd = os.listdir('C:\\Users\\chris\\Documents\\IALabSchool')
        print(bd)
        print("user: "+ usuario)
        print("contra: "+ contra)
        for fichero in bd:
            print(fichero)
            if fichero.startswith(usuario):# and fichero.endswith(".csv"):
                # archivo = open("Users\\"+usuario+".csv","r")
                # with archivo:
                    # lector = csv.reader(archivo, delimiter=",", quotechar=",", quoting=csv.QUOTE_MINIMAL)
                    # lector["Password" == contra]
                    # usuarios.append(fichero)
                    # print(bd)
                    # print(usuarios)
                    # menu.deiconify()
                    df = pd.read_csv(fichero, sep=',')
                    df = pd.DataFrame(df, columns=['Name', 'Password'])
                    passcsv = str(df.iloc[0]['Password']) #esto permite imprimir una fila concreta o un valor de esa fila
                    print("contra_"+passcsv)
                    print("tipo csv")
                    print(type(passcsv))
                    print("tipo textfield")
                    print(type(contra))

                    if(contra == passcsv):
                        #ventana personalizada
                        mensaje = Toplevel()
                        mensaje.geometry('400x250')
                        mensaje.resizable(False, False)

                        l1 = Label(mensaje, text="Buena suerte entrenador!",width=25,font=("times",15,"bold"),bg='#F0F9F0',fg='black')
                        l1.place(x=70,y=100)

                        btning= Button(mensaje,text="Quiero atrapar a todos!",height= 5, width=26, font=("times",10,"bold"), bg= "#F7C031", fg="black", command= TipoAventura)
                        btning.place(x=125, y= 125)
                        
                            
                    else:
                        messagebox.showerror("Datos incorrectos", "Error: Usuario o contraseña incorrectos")
                        InicioSesion.update()

            else:
                InicioSesion.update()
                


    btnIngresar= Button(InicioSesion, text="Iniciar",height= 5, width=26, font=("times",10,"bold"), bg= "#1DD81E", fg="black", command=Ingresar)
    btnIngresar.place(x=300, y= 400)
    btnRegresar= Button(InicioSesion, text="Regresar a Menu Principal",height= 5, width=26, font=("times",10,"bold"), bg= "#F7C031", fg="black", command= Regresar)
    btnRegresar.place(x=30, y= 400)

#En caso de que no se encuentre el usuario, se va habilitara una ventana emergente preguntando si se desea agregar un nuevo usuario, en caso de ser así, la ventana principal
#cambiara a la del registro de nuevo usuario, si se selecciona cancelar, los campos se van a limpiar para volver a introducir datos.

def RegistrarUsuario():
    aviso = messagebox.askyesno(message= "¿Desea registrar un nuevo usuario?", title="Nuevo Usuario")
    if aviso == True:
        global RegistroUsuario
        RegistroUsuario = Toplevel()
        principal.withdraw()#Esconde la Ventana Anterior
        RegistroUsuario.geometry('520x540')

        RegistroUsuario.title("Registro de nuevo usuario")
        RegistroUsuario.resizable(False, False)
        

        canvas3 = Canvas(RegistroUsuario, width=400, height=400)
        canvas3.pack(fill = "both", expand= True)
        canvas3.create_image( 0, 0, image = bg, anchor = "nw")

        tituloregistro = Label(canvas3, image= ph, width=500)
        tituloregistro.place(x=10, y=10)
        tituloregistro.image=ph

        l1 = Label(RegistroUsuario, text="Inicia Sesión",width=25,font=("times",20,"bold"),bg='#F0F9F0',fg='black')
        l1.place(x=70,y=100)

        labeluser= Label(RegistroUsuario, text="Usuario")
        labeluser.place( x= 70, y=150)
        e1 = Entry(RegistroUsuario,width=30,bd=2)
        e1.place(x=70,y=170)   

        labelpass= Label(RegistroUsuario, text="Contraseña")
        labelpass.place( x= 100, y=250)
        e2 = Entry(RegistroUsuario,width=30,bd=2)
        e2.place(x=70,y=270)
       
        labelpass1= Label(RegistroUsuario, text="Confirmar Contraseña")
        labelpass1.place( x= 70, y=350)
        e3 = Entry(RegistroUsuario,width=30,bd=2)
        e3.place(x=70,y=370)
        
        def registro():
            global usuario
            global passw
            global level
            usuario = e1.get()
            passw = e2.get()
            passw1 = e3.get()
            level = 1
            if(passw == passw1):
            #generar csv con distinto nombre para cada usuario
                header=['Name','Password','Level']
                datos=[usuario,passw,level]
                archivo = open("BDUsuarios\\"+usuario+".csv","w",newline="")
                with archivo:
                    escritor=csv.writer(archivo)
                    escritor.writerow(header)
                    escritor.writerow(datos)
                    messagebox.showinfo("Registro Exitoso","Se ha registrado con Exito")

            else:
                messagebox.showwarning("Verifica la contraseña", "La contraseña no coincide")  


        btnRegistrar= Button(RegistroUsuario, text="Registrar",height= 5, width=26, font=("times",10,"bold"), bg= "#1DD81E", fg="black",command=registro)
        btnRegistrar.place(x=300, y= 400)
        

        #agregar que si el usuario ya existe, no dejar que se registre
        
        btnRegresar= Button(RegistroUsuario, text="Regresar a Menu Principal",height= 5, width=26, font=("times",10,"bold"), bg= "#F7C031", fg="black", command= Regresar)
        btnRegresar.place(x=30, y= 400)

############
#PARTE 2 Una vez que se registre como nuevo usuario o que se inicie sesión, se mostrara una ventana con dos opciones de juego
#Modo Historia o Entrenamiento
############   
def TipoAventura():
    global menu
    #InicioSesion.withdraw()
    menu = Toplevel()
    menu.title("Modo de juego")
    menu.geometry('420x540')
    menu.resizable(False, False)
    #bgmenu = PhotoImage(master = canvas4, file = "Imagenes\Menu.png") 
    canvas4 = Canvas(menu, width=420, height=540)
    canvas4.create_image( 0, 0, image = tk_imgmenu, anchor = "nw")
    canvas4.pack(fill = "both", expand= True)   

    l2 = Label(menu, text="Selecciona tu modo de juego",width=25,font=("times",20,"bold"),bg='#F0F9F0',fg='black')
    l2.place(x=20,y=30)

    btnTrain= Button(menu, text="Modo Entrenamiento",height= 5, width=26, font=("times",10,"bold"), bg= "#1DD81E", fg="black",command=Entrenar)
    btnTrain.place(x=100, y= 100)

    #agregar que si el usuario ya existe, no dejar que se registre
        
    btnHistoria= Button(menu, text="Modo Historia",height= 5, width=26, font=("times",10,"bold"), bg= "#F7C031", fg="black", command= Historia)
    btnHistoria.place(x=100, y= 200)

    btnsalir= Button(menu, text="Menu Principal",height= 5, width=26, font=("times",10,"bold"), bg= "#F7C031", fg="black", command= Regresar)
    btnsalir.place(x=100, y= 400)

def Entrenar():
    import Seleccion
    menu.withdraw()#Esconde la Ventana Anterior

def Historia(bd,usuario,level):
    datos=bd
    user = usuario
    nivel = level
    import SeleccionHistoria

    menu.withdraw()


def Regresar():
    # IniciarSesion(InicioSesion.withdraw())
    # RegistrarUsuario(RegistroUsuario.withdraw())
    principal.deiconify()

def RegresaMenu():
    # IniciarSesion(InicioSesion.withdraw())
    # RegistrarUsuario(RegistroUsuario.withdraw())
    menu.deiconify()
   

btnInicio= Button(principal, text="Iniciar Sesion",height= 5, width=15, font=("times",10,"bold"), bg= "#C9F951", fg="black", command= IniciarSesion)
btnRegistro= Button(principal, text="Registrar Usuario",height= 5, width=15, font=("times",10,"bold"),  bg= "#F2F71C", fg="black", command= RegistrarUsuario)

button1_canvas = canvas1.create_window( 225, 210,  
                                       anchor = "nw", 
                                       window = btnInicio)

button1_canvas = canvas1.create_window( 225, 410,  
                                       anchor = "nw", 
                                       window = btnRegistro)




principal.mainloop()