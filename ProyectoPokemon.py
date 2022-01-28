"""
Proyecto Final
Instrucciones aqui:
https://classroom.google.com/c/NDE1MTM0NDc4ODk0/a/NDU3Mzg4NzQyMDI0/details
"""
from cProfile import label
from cgitb import text
from ctypes import resize
from email.mime import image
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
#from turtle import bgcolor, color, title
#from webbrowser import get
from PIL import Image, ImageTk
import os
import csv
from numpy import dtype
import pandas as pd

##########
#paso1: Al inicio del juego se mostrará una ventana preguntando si se desea iniciar sesión o si desea registrar un usuario nuevo.
##########

principal = Tk()
principal.geometry('520x540')

canvas1 = Canvas( principal, width=400, height=400)
canvas1.pack(fill = "both", expand= True)

#Imagenes y fondos de ventana
bg = PhotoImage(master = canvas1, file = "Imagenes\BGPrincipal.png") 
im = Image.open("Imagenes\TituloJuego.png")
ph = ImageTk.PhotoImage(im)
imgmenu= Image.open('C:\\Users\\chris\\Documents\\IALabSchool\\Imagenes\\menu.png')
tk_imgmenu = ImageTk.PhotoImage(imgmenu)
imgpokedex= Image.open('C:\\Users\\chris\\Documents\\IALabSchool\\Imagenes\\pokedex.png')
tk_imgpokedex = ImageTk.PhotoImage(imgpokedex)

aquanderimg = Image.open('C:\\Users\\chris\\Documents\\IALabSchool\\Imagenes\\aquarder.png')
tk_aquanderimg = ImageTk.PhotoImage(aquanderimg)
aquanderdet = Image.open('C:\\Users\\chris\\Documents\\IALabSchool\\Imagenes\\detaquarder.png')
tk_aquanderdet = ImageTk.PhotoImage(aquanderdet)

electderimg = Image.open('C:\\Users\\chris\\Documents\\IALabSchool\\Imagenes\\electder.png')
tk_electderimg = ImageTk.PhotoImage(electderimg)
electerdet = Image.open('C:\\Users\\chris\\Documents\\IALabSchool\\Imagenes\\detelecter.png')
tk_electerdet = ImageTk.PhotoImage(electerdet)

firesorimg = Image.open('C:\\Users\\chris\\Documents\\IALabSchool\\Imagenes\\firesor.png')
tk_firesorimg = ImageTk.PhotoImage(firesorimg)
firesordet = Image.open('C:\\Users\\chris\\Documents\\IALabSchool\\Imagenes\\detfiresor.png')
tk_firesordet = ImageTk.PhotoImage(firesordet)

mouseimg = Image.open('C:\\Users\\chris\\Documents\\IALabSchool\\Imagenes\\mousebug.png')
tk_mouseimg = ImageTk.PhotoImage(mouseimg)
mousedet = Image.open('C:\\Users\\chris\\Documents\\IALabSchool\\Imagenes\\detmousebug.png')
tk_mousedet = ImageTk.PhotoImage(mousedet)

splantimg = Image.open('C:\\Users\\chris\\Documents\\IALabSchool\\Imagenes\\splant.png')
tk_splantimg = ImageTk.PhotoImage(splantimg)
splantdet = Image.open('C:\\Users\\chris\\Documents\\IALabSchool\\Imagenes\\detsplant.png')
tk_splantdet = ImageTk.PhotoImage(splantdet)

rockdogimg = Image.open('C:\\Users\\chris\\Documents\\IALabSchool\\Imagenes\\rockdog.png')
tk_rockdogimg = ImageTk.PhotoImage(rockdogimg)
rockdogdet = Image.open('C:\\Users\\chris\\Documents\\IALabSchool\\Imagenes\\detrockdog.png')
tk_rockdogdet = ImageTk.PhotoImage(rockdogdet)



canvas1.create_image( 0, 0, image = bg, anchor = "nw")

titulo = Label(canvas1, image= ph, width=500)
titulo.place(x=10, y=50)
titulo.image=ph

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
        usuario = e1.get()
        contra =e2.get()
        
        bd = os.listdir('C:\\Users\\chris\\Documents\\IALabSchool')
        print(bd)
        print(usuario)
        print("contra:"+contra)
        for fichero in bd:
            print(fichero)
            if fichero.startswith(usuario) and fichero.endswith(".csv"):
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
            usuario = e1.get()
            passw = e2.get()
            passw1 = e3.get()
            if(passw == passw1):
            #generar csv con distinto nombre para cada usuario
                header=['Name','Password']
                datos=[usuario,passw]
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
        
    btnHistoria= Button(menu, text="Modo Historia",height= 5, width=26, font=("times",10,"bold"), bg= "#F7C031", fg="black")#, command= Historia)
    btnHistoria.place(x=100, y= 200)

    btnsalir= Button(menu, text="Menu Principal",height= 5, width=26, font=("times",10,"bold"), bg= "#F7C031", fg="black", command= Regresar)
    btnsalir.place(x=100, y= 400)

def Entrenar():
    train = Toplevel()#Nueva Ventana Independiente
    menu.withdraw()#Esconde la Ventana Anterior
    train.geometry('1300x950')
    train.config(bg='#F7DE79')
    train.title("Elige a tu pokemon")
    train.resizable(False, False)

    l1 = Label(train, text="Elige a tu pokemon!",width=25,font=("times",20,"bold"),bg='#F0F9F0',fg='black')
    l1.place(x=350,y=20)

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
        
        #tabla['columns']= ('Habilidad', 'Ataque Normal','Ataque con Ventaja','Ataque sin ventaja','Ataque con potenciador normal','Ataque con potenciador con ventaja','Ataque con potenciador sin ventaja')
        # tabla.column("#0", width=80)
        # tabla.column("col1",anchor=CENTER, width=80)
        # tabla.column("col2",anchor=CENTER, width=120)
        # tabla.column("col3",anchor=CENTER, width=120)
        # tabla.column("col4",anchor=CENTER, width=200)
        # tabla.column("col5",anchor=CENTER, width=200)
        # tabla.column("col6",anchor=CENTER, width=200)
        # tabla.heading("#0",text="Habilidad", anchor=LEFT, )
        # tabla.heading("col1",text="Ataque Normal",anchor=CENTER)
        # tabla.heading("col2",text="Ataque con Ventaja",anchor=CENTER)
        # tabla.heading("col3",text="Ataque sin Ventaja",anchor=CENTER)
        # tabla.heading("col4",text="Ataque con potenciador normal",anchor=CENTER)
        # tabla.heading("col5",text="Ataque con potenciador con ventaja",anchor=CENTER)
        # tabla.heading("col6",text="Ataque con potenciador sin ventaja",anchor=CENTER)
        # tabla.insert("",END, text="Aqua-jet", values=("3 puntos","5 puntos","2 puntos","5 puntos","7 puntos","4 puntos"))
        # tabla.insert("",END, text="Cola Férrea", values=("2 puntos","","","","",""))
        # tabla.insert("",END, text="Cabezazo", values=("2 puntos","","","","",""))
        # tabla.insert("",END, text="Lluvia", values=("Potenciador de ataques que puede utilizar una vez cada TRES turnos y dura DOS turnos"))
        # tabla.place(x=10,y=230)
        # tabla1.column("#0", width=80)
        # tabla1.column("col1",anchor=CENTER, width=80)
        # tabla1.heading("#0",text="Habilidad Especial", anchor=CENTER, )
        # tabla1.heading("col1",text="Efecto",anchor=CENTER)
        # tabla1.insert("",END, text="Lluvia", values=("Potenciador de Campo, Se puede utilizar una vez cada TRES turnos y dura DOS turnos"))
        # tabla1.place(x=10,y=300)

    #IMAGENES 200X200
    aquanderlab= Label(train, text="Aquander",width=25,font=("times",12),bg='#F0F9F0',fg='black')
    aquanderlab.place(x=50,y=80)
    pokeaquander= Button(train, image=tk_aquanderimg, width=300, height=300)#command= aquander
    pokeaquander.place(x=20, y=120)
    det1= Button(train, text="Detalles", height=2, width=16, command= detaquander)
    det1.place(x=110, y= 440)

    labelectder= Label(train, text="Electder",width=25,font=("times",12),bg='#F0F9F0',fg='black')
    labelectder.place(x=400,y=80)
    pokeelectder= Button(train, image=tk_electderimg, width=300, height=300)#command= aquander
    pokeelectder.place(x=340, y=120)
    det2= Button(train, text="Detalles", width=16, height=2, command=detelecter) 
    det2.place(x=400, y= 440)

    labfiresor= Label(train, text="Firesor",width=25,font=("times",12),bg='#F0F9F0',fg='black')
    labfiresor.place(x=710,y=80)
    pokefiresor= Button(train, image=tk_firesorimg, width=300, height=300)#command= aquander
    pokefiresor.place(x=660, y=120)
    detfiresor= Button(train, text="Detalles", width=16, height=2, command= detfiresor)
    detfiresor.place(x=710, y= 440)

    labmouse= Label(train, text="Mousebug",width=25,font=("times",12),bg='#F0F9F0',fg='black')
    labmouse.place(x=1050,y=80)
    pokemouse= Button(train, image=tk_mouseimg, width=300, height=300)#command= aquander
    pokemouse.place(x=980, y=120)
    detmouse= Button(train, text="Detalles", width=16, height=2, command=detmousebug)
    detmouse.place(x=1050, y= 440)

    labsplant= Label(train, text="Splant",width=25,font=("times",12),bg='#F0F9F0',fg='black')
    labsplant.place(x=50,y=520)
    pokesplant= Button(train, image=tk_splantimg, width=300, height=300)#command= aquander
    pokesplant.place(x=20, y=550)
    detsplant= Button(train, text="Detalles", width=16, height=2, command=detsplant)
    detsplant.place(x=110, y= 870)  

    labrockdog= Label(train, text="Rockdog",width=25,font=("times",12),bg='#F0F9F0',fg='black')
    labrockdog.place(x=1050,y=520)
    pokerockdog= Button(train, image=tk_rockdogimg, width=300, height=300)#command= aquander
    pokerockdog.place(x=980, y=550)
    detrockdog= Button(train, text="Detalles", width=16, height=2, command=detrockdog)
    detrockdog.place(x=1050, y= 870)  

    btnTrain= Button(train, text="Iniciar combate",height= 5, width=26, font=("times",15,"bold"), bg= "#1DD81E", fg="black")
    btnTrain.place(x=500, y= 600)

    btnsalir= Button(train, text="Menu Aventura",height= 3, width=16, font=("times",10,"bold"), bg= "#F7C031", fg="black", command= RegresaMenu)
    btnsalir.place(x=500, y= 800)




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