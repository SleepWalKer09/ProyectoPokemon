import time
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import os
import random
import pandas as pd


a= "C:\\Users\\chris\\Documents\\IALabSchool\\Imagenes\\"
Personaje = 0
Nombre=""
Nombre2="Mousebug"
juego=4
t=0
tipo1=""
tipo2="Escarabajo"
pot_1=0
pot_2=0
contador_pot1=0
contador_pot2=0
Vidajugador = 25
Vidacpu = 25

#Ventana del combate
hist5 = Tk()
hist5.geometry("900x560")
hist5.title("Pelea Entrenamiento")
hist5.resizable(False,False)

gymimg = Image.open(a+'gimnasio.png')
tk_gym = ImageTk.PhotoImage(gymimg)

#Imagenes para la batalla
aquanderimg = Image.open(a+'aquarder.png')
tk_aquander = ImageTk.PhotoImage(aquanderimg)
electderimg = Image.open(a+'electder.png')
tk_electder = ImageTk.PhotoImage(electderimg)
firesorimg = Image.open(a+'firesor.png')
tk_firesor = ImageTk.PhotoImage(firesorimg)
mouseimg = Image.open(a+'mousebug.png')
tk_mouse = ImageTk.PhotoImage(mouseimg)
splantimg = Image.open(a+'splant.png')
tk_splant= ImageTk.PhotoImage(splantimg)
rockdogimg = Image.open(a+'rockdog.png')
tk_rockdog = ImageTk.PhotoImage(rockdogimg)

canvashist5 = Canvas(hist5, width=1000, height=500)
canvashist5.create_image( 0, 0, image = tk_gym, anchor = "nw")
canvashist5.pack(fill = "both", expand= True) 

#ventana de combate contra aquarder, primer pokemon en la lista
#el cpu debe ser igual al entrenamiento, solo se debe programar la parte del jugador

#funcion con valores de la ventana de seleccion del modo historia
def batalla1(Personaje,nombre,t1):
    global player
    global cpu
    global tipo1
    global tipo2
    global Nombre
    global Nombre2
    Nombre = nombre
    tipo1=t1
    player=Personaje
    nombrejugador.config(text=Nombre)
    print("************************")
    print("Datos batalla")
    print("personaje: "+str(player))
    print("nombre "+nombre)
    print("TipoPlayer "+t1)

    if(player==1):
        Pokemonjugador.config(image=tk_aquander)
        Atq1.config(text="Aqua-jet")
        Atq2.config(text="Cola Ferrea")
        Atq3.config(text="Cabezazo")
        Atq4.config(text="Lluvia")

    elif(player==2):
        Pokemonjugador.config(image=tk_electder)
        Atq1.config(text="Trueno")
        Atq2.config(text="Arañazo")
        Atq3.config(text="Mordisco")
        Atq4.config(text="C. Magnetico")
    
    elif(player==3):
        Pokemonjugador.config(image=tk_firesor)
        Atq1.config(text="Llamarada")
        Atq2.config(text="Embestida")
        Atq3.config(text="Mordisco")
        Atq4.config(text="Dia Soleado")
    
    elif(player==4):
        Pokemonjugador.config(image=tk_mouse)
        Atq1.config(text="Picotazo")
        Atq2.config(text="Embestida")
        Atq3.config(text="Cabezazo")
        Atq4.config(text="Esporas")

    elif(player==5):
        Pokemonjugador.config(image=tk_splant)
        Atq1.config(text="Hola Navaja")
        Atq2.config(text="Mordisco")
        Atq3.config(text="Cabezazo")
        Atq4.config(text="Rayo Solar")

    elif(player==6):
        Pokemonjugador.config(image=tk_rockdog)
        Atq1.config(text="Roca Afilada")
        Atq2.config(text="Velocidad")
        Atq3.config(text="Cola Ferrea")
        Atq4.config(text="Campo Rocoso")
    
    global nivel
    nivel=5
    LogBatalla.config(text="La batalla esta por iniciar", anchor="center")
    hist5.update()
    time.sleep(2)
    LogBatalla.config(text="", anchor="center")


    global t
    t=random.randint(1,2)
    if(t==1):
        LogBatalla.config("¡Tu atacas primero! \n Preparate", anchor="center")
        
    else:
        LogBatalla.config("¡Tu rival ataca primero! \n Buena suerte", anchor="center")
        oponente(Nombre2,tipo1)
    time.sleep(5)



#Funcion con las acciones que podra tomar el oponente
def oponente(nombre2,t1):
    global Vidajugador
    global Vidacpu
    global pot_2
    global contador_pot2
    Atq1.config(state=DISABLED)
    Atq2.config(state=DISABLED)
    Atq3.config(state=DISABLED)
    Atq4.config(state=DISABLED)

#NIVEL 5: CPU PELEA CON SPLANT
#no esta activo el potenciador
    if(pot_2==0) and ((contador_pot2 >4) or (contador_pot2==0)):
        CPUatq=random.randint(1,4)#ataques aleatorios
    else:#si esta activo el potenciador
        CPUatq=random.randint(1,3)
    #si utiliza el ataque especial
    if(CPUatq==4):
        pot_2= 1
        contador_pot2= 1
        LogBatalla.config(text=str(nombre2)+''' a utilizado Rayo Solar\n
        Sus ataques se intensifican por 2 turnos''', anchor="Center")
        time.sleep(2)
    #ataque 1 mousebug
    elif(CPUatq==1):
        if(t1=="Agua" or t1=="Roca" or t1=="Electrico"):
           LogBatalla.config(text= str(Nombre2)+''' a utilizado Hoja Navaja\n
           ¡Es super efectivo!''', anchor="center")
        if(pot_2==0):
            LogBatalla.config(text='''Recibiste 5 HP de daño!!''', anchor="center")
            Vidajugador = Vidajugador-5
            time.sleep(2)
        elif(pot_2==1):
            LogBatalla.config(text='''Recibiste 7 HP de daño!!''', anchor="center")
            Vidajugador= Vidajugador-7
            time.sleep(2)
        if(t1=="Fuego" or t1=="Escarabajo"):
            LogBatalla.config(text=str(Nombre2)+''' a utilizado Hoja Navaja\n
            ¡No es muy efectivo!''', anchor="center")
            if(pot_2==0):
                LogBatalla.config(text='''Recibiste 2 HP de daño!!''', anchor="center")
                Vidajugador = Vidajugador-2
                time.sleep(2)
            elif(pot_2==1):
                LogBatalla.config(text='''Recibiste 4 HP de daño!!''', anchor="center")
                Vidajugador= Vidajugador-4
                time.sleep(2)
        if(t1=="Planta"):
            LogBatalla.config(text=str(Nombre2)+''' a utilizado Hoja Navaja\n
            ¡Daño normal!''', anchor="center")
            if(pot_2==0):
                LogBatalla.config(text='''Recibiste 3 HP de daño!!''', anchor="center")
                Vidajugador = Vidajugador-3
                time.sleep(2)
            elif(pot_2==1):
                LogBatalla.config(text='''Recibiste 5 HP de daño!!''', anchor="center")
                Vidajugador= Vidajugador-5
                time.sleep(2)
        hist5.update()
        time.sleep(2)
    
        #Ataques splant
    elif(CPUatq==2):
        LogBatalla.config(text=str(Nombre2)+''' a utilizado Mordisco''', anchor="center")
        time.sleep(2)
        Vidajugador = Vidajugador-2
        LogBatalla.config(text='''Recibiste 2 HP de daño!!''', anchor="center")
        hist5.update()

    elif(CPUatq==3):
        LogBatalla.config(text=str(Nombre2)+''' a utilizado Cabezazo''', anchor="center")
        time.sleep(2)
        Vidajugador = Vidajugador-2
        LogBatalla.config(text='''Recibiste 2 HP de daño!!''', anchor="center")
        hist5.update()

    if(contador_pot2 != 0):
        contador_pot2 = contador_pot2 + 1
        
    #contador de turnos para el ataque especial
    if(contador_pot2 == 4):
        pot_2 = 0
        LogBatalla.conf(text=''' Ha terminado el efecto Rayo Solar \n
        Los ataques de '''+ str(Nombre2) +'''vuelven a la normalidad''', anchor="center")
    elif(contador_pot2 > 4):
        contador_pot2= 0
    else:
        LogBatalla.config(text=str(Nombre2)+ ''' a utilizado Rayo Solar\n
        Quedan '''+str(4-contador_pot2)+" Movimientos ",anchor="center")
        VidaJ.config(text=str(Vidajugador)+" HP")
        hist5.update()
        time.sleep(2)
            
    Atq1.config(state=NORMAL)
    Atq2.config(state=NORMAL)
    Atq3.config(state=NORMAL)
    Atq4.config(state=NORMAL)

def PrimerAtaque(pot_1):
    #global pot_1
    global contador_pot1
    global Nombre
    global player
    global Vidacpu
    global t2

    
    if(player==1):
        #ataque 1 aquarder
        if(t2=="Roca" or t2=="Fuego"):
            LogBatalla.config(text= str(Nombre)+''' a utilizado Aqua-Jet\n
            ¡Es super efectivo!''', anchor="center")
            if(pot_1==0):
                LogBatalla.config(text='''Recibiste 5 HP de daño!!''', anchor="center")
                Vidacpu = Vidacpu-5
                time.sleep(2)
            elif(pot_1==1):
                LogBatalla.config(text='''Recibiste 7 HP de daño!!''', anchor="center")
                Vidacpu= Vidacpu-7
                time.sleep(2)
        if(t2=="Electrico" or t2=="Planta"):
            LogBatalla.config(text=str(Nombre)+''' a utilizado Aqua-Jet\n
            ¡No es muy efectivo!''', anchor="center")
            if(pot_1==0):
                LogBatalla.config(text='''Recibiste 2 HP de daño!!''', anchor="center")
                Vidacpu = Vidacpu-2
                time.sleep(2)
            elif(pot_1==1):
                LogBatalla.config(text='''Recibiste 4 HP de daño!!''', anchor="center")
                Vidacpu= Vidacpu-4
                time.sleep(2)
        if(t2=="Agua" or t2=="Escarabajo"):
            LogBatalla.config(text=str(Nombre)+''' a utilizado Aqua-Jet\n
            ¡Daño normal!''', anchor="center")
            if(pot_1==0):
                LogBatalla.config(text='''Recibiste 3 HP de daño!!''', anchor="center")
                Vidacpu = Vidacpu-3
                time.sleep(2)
            elif(pot_1==1):
                LogBatalla.config(text='''Recibiste 5 HP de daño!!''', anchor="center")
                Vidacpu= Vidacpu-5
                time.sleep(2)
        hist5.update()
        time.sleep(2)
        #calculos del potenciador
        if(contador_pot1 !=0):
            contador_pot1=contador_pot1+1
        
        #parte de deshabilitar boton
        if(contador_pot1==4):
            pot_1=0
            LogBatalla.config(text= '''Termino efecto de lluvia,\n tus ataques vuelven a la normalidad''', anchor="center")
            time.sleep(2)
        elif(contador_pot1 >4):
            contador_pot1=0
        else:
            LogBatalla.config(text=str(Nombre)+ ''' a utilizado lluvia \n
            Quedan '''+str(4-contador_pot1)+" Movimientos ",anchor="center")
            VidaC.config(text=str(Vidacpu)+" HP")
            hist5.update()
            time.sleep(2)

    elif(player==2):
        if(t2=="Agua" or t2=="Escarabajo"):
            LogBatalla.config(text= str(Nombre)+''' a utilizado Trueno\n
            ¡Es super efectivo!''', anchor="center")
            if(pot_1==0):
                LogBatalla.config(text='''Recibiste 5 HP de daño!!''', anchor="center")
                Vidacpu = Vidacpu-5
                time.sleep(2)
            elif(pot_1==1):
                LogBatalla.config(text='''Recibiste 7 HP de daño!!''', anchor="center")
                Vidacpu= Vidacpu-7
                time.sleep(2)
        if(t2=="Roca" or t2=="Planta"):
            LogBatalla.config(text=str(Nombre)+''' a utilizado Trueno\n
            ¡No es muy efectivo!''', anchor="center")
            if(pot_1==0):
                LogBatalla.config(text='''Recibiste 2 HP de daño!!''', anchor="center")
                Vidacpu = Vidacpu-2
                time.sleep(2)
            elif(pot_1==1):
                LogBatalla.config(text='''Recibiste 4 HP de daño!!''', anchor="center")
                Vidacpu= Vidacpu-4
                time.sleep(2)
        if(t2=="Electrico" or t2=="Fuego"):
            LogBatalla.config(text=str(Nombre)+''' a utilizado Trueno\n
            ¡Daño normal!''', anchor="center")
            if(pot_1==0):
                LogBatalla.config(text='''Recibiste 3 HP de daño!!''', anchor="center")
                Vidacpu = Vidacpu-3
                time.sleep(2)
            elif(pot_1==1):
                LogBatalla.config(text='''Recibiste 5 HP de daño!!''', anchor="center")
                Vidacpu= Vidacpu-5
        hist5.update()
        time.sleep(2)

        #calculos del potenciador
        if(contador_pot1 !=0):
            contador_pot1=contador_pot1+1
        
        #parte de deshabilitar boton
        if(contador_pot1==4):
            pot_1=0
            LogBatalla.config(text= '''Termino efecto de Campo Magnetico,\n tus ataques vuelven a la normalidad''', anchor="center")
            time.sleep(2)
        elif(contador_pot1 >4):
            contador_pot1=0
        else:
            LogBatalla.config(text=str(Nombre)+ ''' a utilizado Campo Magnetico \n
            Quedan '''+str(4-contador_pot1)+" Movimientos ",anchor="center")
            VidaC.config(text=str(Vidacpu)+" HP")
            hist5.update()
            time.sleep(2)

    elif(player==3):
        #ataque 1 firesor
        if(t2=="Planta" or t2=="Escarabajo"):
            LogBatalla.config(text= str(Nombre)+''' a utilizado Llamarada\n
            ¡Es super efectivo!''', anchor="center")
            if(pot_1==0):
                LogBatalla.config(text='''Recibiste 5 HP de daño!!''', anchor="center")
                Vidacpu = Vidacpu-5
                time.sleep(2)
            elif(pot_1==1):
                LogBatalla.config(text='''Recibiste 7 HP de daño!!''', anchor="center")
                Vidacpu= Vidacpu-7
                time.sleep(2)
        if(t2=="Roca" or t2=="Agua"):
            LogBatalla.config(text=str(Nombre)+''' a utilizado Llamarada\n
            ¡No es muy efectivo!''', anchor="center")
            if(pot_1==0):
                LogBatalla.config(text='''Recibiste 2 HP de daño!!''', anchor="center")
                Vidacpu = Vidacpu-2
                time.sleep(2)
            elif(pot_1==1):
                LogBatalla.config(text='''Recibiste 4 HP de daño!!''', anchor="center")
                Vidacpu= Vidacpu-4
                time.sleep(2)
        if(t2=="Electrico" or t2=="Fuego"):
            LogBatalla.config(text=str(Nombre)+''' a utilizado Llamarada\n
            ¡Daño normal!''', anchor="center")
            if(pot_1==0):
                LogBatalla.config(text='''Recibiste 3 HP de daño!!''', anchor="center")
                Vidacpu = Vidacpu-3
                time.sleep(2)
            elif(pot_1==1):
                LogBatalla.config(text='''Recibiste 5 HP de daño!!''', anchor="center")
                Vidacpu= Vidacpu-5
                time.sleep(2)
            hist5.update()
            time.sleep(2)

        #calculos del potenciador
        if(contador_pot1 !=0):
            contador_pot1=contador_pot1+1
        
        #parte de deshabilitar boton
        if(contador_pot1==4):
            pot_1=0
            LogBatalla.config(text= '''Termino efecto de Dia Soleado,\n tus ataques vuelven a la normalidad''', anchor="center")
            time.sleep(2)
        elif(contador_pot1 >4):
            contador_pot1=0
        else:
            LogBatalla.config(text=str(Nombre)+ ''' a utilizado Dia Soleado \n
            Quedan '''+str(4-contador_pot1)+" Movimientos ",anchor="center")
            Vidacpu.config(text=str(Vidacpu)+" HP")
            hist5.update()
            time.sleep(2)

    elif(player==4):
        #ataque 1 mousebug
        if(t2=="Planta" or t2=="Roca"):
            LogBatalla.config(text= str(Nombre)+''' a utilizado Picotazo\n
            ¡Es super efectivo!''', anchor="center")
            if(pot_1==0):
                LogBatalla.config(text='''Recibiste 5 HP de daño!!''', anchor="center")
                Vidacpu = Vidacpu-5
                time.sleep(2)
            elif(pot_1==1):
                LogBatalla.config(text='''Recibiste 7 HP de daño!!''', anchor="center")
                Vidacpu= Vidacpu-7
                time.sleep(2)
        if(t2=="Fuego" or t2=="Electrico"):
            LogBatalla.config(text=str(Nombre)+''' a utilizado Picotazo\n
            ¡No es muy efectivo!''', anchor="center")
            if(pot_1==0):
                LogBatalla.config(text='''Recibiste 2 HP de daño!!''', anchor="center")
                Vidacpu = Vidacpu-2
                time.sleep(2)
            elif(pot_1==1):
                LogBatalla.config(text='''Recibiste 4 HP de daño!!''', anchor="center")
                Vidacpu= Vidacpu-4
                time.sleep(2)
        if(t2=="Escarabajo" or t2=="Agua"):
            LogBatalla.config(text=str(Nombre)+''' a utilizado Picotazo\n
            ¡Daño normal!''', anchor="center")
            if(pot_1==0):
                LogBatalla.config(text='''Recibiste 3 HP de daño!!''', anchor="center")
                Vidacpu = Vidacpu-3
                time.sleep(2)
            elif(pot_1==1):
                LogBatalla.config(text='''Recibiste 5 HP de daño!!''', anchor="center")
                Vidacpu= Vidacpu-5
                time.sleep(2)
        hist5.update()
        time.sleep(2)
        
        #calculos del potenciador
        if(contador_pot1 !=0):
            contador_pot1=contador_pot1+1
        
        #contador de turnos para el ataque especial
        if(contador_pot1 == 4):
            pot_1 = 0
            LogBatalla.conf(text=''' Ha terminado el efecto Esporas \n
            Los ataques de '''+ str(Nombre) +'''vuelven a la normalidad''', anchor="center")
        elif(contador_pot1 > 4):
            contador_pot1= 0
        else:
            LogBatalla.config(text=str(Nombre)+ ''' a utilizado Esporas\n
            Quedan '''+str(4-contador_pot1)+" Movimientos ",anchor="center")
            VidaC.config(text=str(Vidacpu)+" HP")
        hist5.update()
        time.sleep(2)
    
    elif(player==5):
        #ataque 1 splant
        if(t2=="Agua" or t2=="Roca" or t2=="Electrico"):
            LogBatalla.config(text= str(Nombre)+''' a utilizado Hoja Navaja\n
            ¡Es super efectivo!''', anchor="center")
            if(pot_1==0):
                LogBatalla.config(text='''Recibiste 5 HP de daño!!''', anchor="center")
                Vidacpu = Vidacpu-5
                time.sleep(2)
            elif(pot_1==1):
                LogBatalla.config(text='''Recibiste 7 HP de daño!!''', anchor="center")
                Vidacpu= Vidacpu-7
                time.sleep(2)
        if(t2=="Fuego" or t2=="Escarabajo"):
            LogBatalla.config(text=str(Nombre)+''' a utilizado Hoja Navaja\n
            ¡No es muy efectivo!''', anchor="center")
            if(pot_1==0):
                LogBatalla.config(text='''Recibiste 2 HP de daño!!''', anchor="center")
                Vidacpu = Vidacpu-2
                time.sleep(2)
            elif(pot_1==1):
                LogBatalla.config(text='''Recibiste 4 HP de daño!!''', anchor="center")
                Vidacpu= Vidacpu-4
                time.sleep(2)
        if(t2=="Planta"):
            LogBatalla.config(text=str(Nombre)+''' a utilizado Hoja Navaja\n
            ¡Daño normal!''', anchor="center")
            if(pot_1==0):
                LogBatalla.config(text='''Recibiste 3 HP de daño!!''', anchor="center")
                Vidacpu = Vidacpu-3
                time.sleep(2)
            elif(pot_1==1):
                LogBatalla.config(text='''Recibiste 5 HP de daño!!''', anchor="center")
                Vidacpu= Vidacpu-5
                time.sleep(2)
            hist5.update()
            time.sleep(2)
        #calculos del potenciador
        if(contador_pot1 !=0):
            contador_pot1=contador_pot1+1
        
        #contador de turnos para el ataque especial
        if(contador_pot1 == 4):
            pot_1 = 0
            LogBatalla.conf(text=''' Ha terminado el efecto Rayo Solar \n
            Los ataques de '''+ str(Nombre) +'''vuelven a la normalidad''', anchor="center")
        elif(contador_pot1 > 4):
            contador_pot1= 0
        else:
            LogBatalla.config(text=str(Nombre)+ ''' a utilizado Rayo Solar \n
            Quedan '''+str(4-contador_pot1)+" Movimientos ",anchor="center")
            VidaC.config(text=str(Vidacpu)+" HP")
        hist5.update()
        time.sleep(2)
    
    elif(player==6):
        #ataque 1 rockdog
        if(t2=="Fuego" or t2=="Electrico"):
            LogBatalla.config(text= str(Nombre)+''' a utilizado Roca Afilada\n
            ¡Es super efectivo!''', anchor="center")
            if(pot_1==0):
                LogBatalla.config(text='''Recibiste 5 HP de daño!!''', anchor="center")
                Vidacpu = Vidacpu-5
                time.sleep(2)
            elif(pot_1==1):
                LogBatalla.config(text='''Recibiste 7 HP de daño!!''', anchor="center")
                Vidacpu= Vidacpu-7
                time.sleep(2)
        if(t2=="Agua" or t2=="Planta"):
            LogBatalla.config(text=str(Nombre)+''' a utilizado Roca Afilada\n
            ¡No es muy efectivo!''', anchor="center")
            if(pot_1==0):
                LogBatalla.config(text='''Recibiste 2 HP de daño!!''', anchor="center")
                Vidacpu = Vidacpu-2
                time.sleep(2)
            elif(pot_2==1):
                LogBatalla.config(text='''Recibiste 4 HP de daño!!''', anchor="center")
                Vidacpu= Vidacpu-4
                time.sleep(2)
        if(t2=="Roca" or t2=="Escarabajo"):
            LogBatalla.config(text=str(Nombre)+''' a utilizado Roca Afilada\n
            ¡Daño normal!''', anchor="center")
            if(pot_1==0):
                LogBatalla.config(text='''Recibiste 3 HP de daño!!''', anchor="center")
                Vidacpu = Vidacpu-3
                time.sleep(2)
            elif(pot_1==1):
                LogBatalla.config(text='''Recibiste 5 HP de daño!!''', anchor="center")
                Vidacpu= Vidacpu-5
                time.sleep(2)
        hist5.update()
        time.sleep(2)
        #calculos del potenciador
        if(contador_pot1 !=0):
            contador_pot1=contador_pot1+1
        
        #contador de turnos para el ataque especial
        if(contador_pot1 == 4):
            pot_1 = 0
            LogBatalla.conf(text=''' Ha terminado el efecto Campo Rocoso \n
            Los ataques de '''+ str(Nombre) +'''vuelven a la normalidad''', anchor="center")
        elif(contador_pot1 > 4):
            contador_pot1= 0
        else:
            LogBatalla.config(text=str(Nombre)+ ''' a utilizado Campo Rocoso \n
            Quedan '''+str(4-contador_pot1)+" Movimientos ",anchor="center")
            VidaC.config(text=str(Vidacpu)+" HP")
        hist5.update()
        time.sleep(2)

    

def SegundoAtaque():
    global pot_1
    global contador_pot1
    global Nombre
    global player
    global Vidacpu

    if(player==1):
        LogBatalla.config(text=str(Nombre)+''' a utilizado Cola Ferrea''', anchor="center")
        time.sleep(2)
        Vidacpu = Vidacpu-2
        LogBatalla.config(text='''Tu rival ha recibido 2 HP de daño!!''', anchor="center")
        hist5.update()
    elif(player==2):
        LogBatalla.config(text=str(Nombre)+''' a utilizado Arañazo''', anchor="center")
        time.sleep(2)
        Vidacpu = Vidacpu-3
        LogBatalla.config(text='''Tu rival ha recibido 3 HP de daño!!''', anchor="center")
        hist5.update()
    elif(player==3):
        LogBatalla.config(text=str(Nombre)+''' a utilizado Embestida''', anchor="center")
        time.sleep(2)
        Vidacpu = Vidacpu-2
        LogBatalla.config(text='''Tu rival ha recibido 2 HP de daño!!''', anchor="center")
        hist5.update()
    elif(player==4):
        LogBatalla.config(text=str(Nombre)+''' a utilizado Embestida''', anchor="center")
        time.sleep(2)
        Vidacpu = Vidacpu-2
        LogBatalla.config(text='''Tu rival ha recibido 2 HP de daño!!''', anchor="center")
        hist5.update()
    elif(player==5):
        LogBatalla.config(text=str(Nombre)+''' a utilizado Mordisco''', anchor="center")
        time.sleep(2)
        Vidacpu = Vidacpu-2
        LogBatalla.config(text='''Tu rival ha recibido 2 HP de daño!!''', anchor="center")
        hist5.update()
    elif(player==6):
        LogBatalla.config(text=str(Nombre)+''' a utilizado Velocidad''', anchor="center")
        time.sleep(2)
        Vidacpu = Vidacpu-2
        LogBatalla.config(text='''Tu rival ha recibido 2 HP de daño!!''', anchor="center")
        hist5.update()


def TercerAtaque():
    global pot_1
    global contador_pot1
    global Nombre
    global player
    global Vidacpu
    if (player==1):
        LogBatalla.config(text=str(Nombre)+''' a utilizado Cabezazo''', anchor="center")
        time.sleep(2)
        Vidacpu = Vidacpu-2
        LogBatalla.config(text='''Recibiste 2 HP de daño!!''', anchor="center")
        hist5.update()
    elif(player==2):
        LogBatalla.config(text=str(Nombre)+''' a utilizado Mordisco''', anchor="center")
        time.sleep(2)
        Vidacpu = Vidacpu-3
        LogBatalla.config(text='''Recibiste 3 HP de daño!!''', anchor="center")
        hist5.update()
    elif(player==3):
        LogBatalla.config(text=str(Nombre)+''' a utilizado Embestida''', anchor="center")
        time.sleep(2)
        Vidacpu = Vidacpu-2
        LogBatalla.config(text='''Recibiste 2 HP de daño!!''', anchor="center")
        hist5.update()
    elif(player==4):
        LogBatalla.config(text=str(Nombre2)+''' a utilizado Cabezazo''', anchor="center")
        time.sleep(2)
        Vidacpu = Vidacpu-2
        LogBatalla.config(text='''Recibiste 2 HP de daño!!''', anchor="center")
        hist5.update()
    elif(player==5):
        LogBatalla.config(text=str(Nombre2)+''' a utilizado Cabezazo''', anchor="center")
        time.sleep(2)
        Vidacpu = Vidacpu-2
        LogBatalla.config(text='''Recibiste 2 HP de daño!!''', anchor="center")
        hist5.update()
    elif(player==6):
        LogBatalla.config(text=str(Nombre2)+''' a utilizado Cola Ferrea''', anchor="center")
        time.sleep(2)
        Vidacpu = Vidacpu-2
        LogBatalla.config(text='''Recibiste 2 HP de daño!!''', anchor="center")
        hist5.update()

    
def CuartoAtaque():#especial
    global Nombre
    global pot_1
    global contador_pot1
    #se inicializan las varables en 1 para demostrar que esta activo el potenciador
    if(player==1):
        pot_1= 1
        contador_pot1= 1
        LogBatalla.config(text=str(Nombre)+''' a utilizado Lluvia\n
        Sus ataques se intensifican por 2 turnos''', anchor="Center")
        time.sleep(2)
    elif(player==2):
        pot_1= 1
        contador_pot1= 1
        LogBatalla.config(text=str(Nombre)+''' a utilizado Campo Magnetico\n
        Sus ataques se intensifican por 2 turnos''', anchor="Center")
        time.sleep(2)
    elif(player==3):
        pot_1= 1
        contador_pot1= 1
        LogBatalla.config(text=str(Nombre)+''' a utilizado Dia soleado\n
        Sus ataques se intensifican por 2 turnos''', anchor="Center")
        time.sleep(2)
    elif(player==4):
        pot_1= 1
        contador_pot1= 1
        LogBatalla.config(text=str(Nombre)+''' a utilizado Esporas\n
        Sus ataques se intensifican por 2 turnos''', anchor="Center")
        time.sleep(2)
    elif(player==5):
        pot_1= 1
        contador_pot1= 1
        LogBatalla.config(text=str(Nombre)+''' a utilizado Rayo Solar\n
        Sus ataques se intensifican por 2 turnos''', anchor="Center")
        time.sleep(2)
    elif(player==6):
        pot_1= 1
        contador_pot1= 1
        LogBatalla.config(text=str(Nombre)+''' a utilizado Campo Rocoso\n
        Sus ataques se intensifican por 2 turnos''', anchor="Center")
        time.sleep(2)



Pokemonjugador= Label()
Pokemonjugador.place(x=180,y=80)
nombrejugador = Label(text=Nombre)
nombrejugador.place(x=220,y=30)
CpuImagen= Label(image=tk_aquander)
CpuImagen.place(x=500,y=80)
nombrerival = Label(text="Aquarder")
nombrerival.place(x=580,y=30)
VidaJ = Label(text=str(Vidajugador) + " HP")
VidaJ.place(x=220, y=300)
VidaC = Label(text= str(Vidacpu) + " HP")
VidaC.place(x=580,y=300)
LogBatalla = Label(text="")
LogBatalla.place(x=200, y=350)

Atq1= Button(hist5, command= PrimerAtaque)
Atq1.place(x=50, y= 100)
Atq2= Button(hist5, command= SegundoAtaque)
Atq2.place(x=50, y= 150)
Atq3= Button(hist5, command= TercerAtaque)
Atq3.place(x=50, y= 200)
Atq4= Button(hist5, command= CuartoAtaque)
Atq4.place(x=50, y= 250)

hist5.mainloop()