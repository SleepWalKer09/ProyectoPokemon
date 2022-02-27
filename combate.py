from tkinter import messagebox
from config import selection_pokemon, user_name, ronda, pokemones, count_cpu_turno, count_jugador_turno, potenciador_jugador, potenciador_cpu, count_potenciador_cpu, count_potenciador_jugador, selected_potenciador_cpu, selected_potenciador_jugador, ataque_cpu, ataque_jugador, status
import random
import os
import copy


def cpu_selection()->int:
    num = random.randint(0, 5)
    return num


class Entrenador:
    def __init__(self, indice:int, name='cpu'):
        self.entrenador = name
        self.indice = indice
        self.poke = selection_pokemon[indice]
        self.vida=25

def hacer_daño(jugador:Entrenador, cpu:Entrenador, daño:int):
    global status
    r = ronda
    if r:
        vida = jugador.vida - daño
        jugador.vida = vida
        print("*******")
        print(f'El jugador recibió {daño} de daño')
        print("*******")
        print(f'Vida {jugador.entrenador} => {vida}')
        print("*******")
        if jugador.vida < 1:
            status = True
            messagebox.showinfo(message=f'{jugador.entrenador} Perdiste la batalla',title='Derrota')
            
    else:
        vida = cpu.vida - daño
        cpu.vida = vida
        print("-------")
        print(f'El CPU recibió {daño} de daño') 
        print("-------")
        print(f'Vida {cpu.entrenador} => {vida}')
        print("-------")
        if cpu.vida < 1:
            status = True
            messagebox.showinfo(message=f'{jugador.entrenador} Has ganado',title='Victoria')
            

class Duelo:
    def __init__(self, jugador:Entrenador):
        self.jugador = jugador
        self.cpuindice = cpu_selection()
        self.cpu = Entrenador(indice=self.cpuindice)

    def flip_coin(self,):
        coin = random.randint(0, 1)
        if coin == 0:
            messagebox.showinfo(message=f'{self.jugador.entrenador} es tu turno',title='Elección de turno')
            print("+++++++")
            print('Comienza jugador')
            print("+++++++")
            ronda = False
            print(f'la ronda da {ronda}')
            return ronda
        else:
            messagebox.showinfo(message=f'Turno del {self.cpu.entrenador}',title='Elección de turno')
            print("xxxxxxx")
            print('Comienza CPU')
            print("xxxxxxx")
            ronda = True
            print(f'la ronda da {ronda}')
            return ronda

    def change_turn(self):
        global ronda
        if ronda:
            ronda = False
        else:
            ronda = True

    def ai_selection(self, pokemon):
        index_atack = random.randint(0,3)
        pokeindice = list()
        for ataque in pokemones[pokemon]:
            pokeindice.append(ataque)
        
        return pokeindice[index_atack]

    def seleccion_ataque(self, ataque_):
        turno = Turno()
        turno.entregar_turno()
        print(turno.count_potenciador, turno.count_turno, turno.potenciador)
        if turno.ronda:
            personaje = 'CPU'
            elpoke = self.cpu.indice
            contricante = self.jugador.indice
        else:
            personaje = user_name
            elpoke = self.jugador.indice
            contricante = self.cpu.indice

        pokepoke = selection_pokemon[elpoke]
        pokepoke_contrincanet = selection_pokemon[contricante]
        print(f'{personaje} eligiste {ataque_}')
        ataques = pokemones[pokepoke]
        arbol_ataque = list()
        nturno = turno.count_turno + 1
        turno.count_turno = nturno

        for i, ataque in enumerate(ataques):
            arbol_ataque.append(ataque)
        # Ataque Elemental
        if ataque_ == arbol_ataque[0]:
            # Desventajas
            if contricante in pokemones[pokepoke]['Desventajas']:
                if turno.count_potenciador < 2 and turno.potenciador == True:
                    hacer_daño(self.jugador,self.cpu,daño=4)
                    self.change_turn()
                    
                else:
                    turno.potenciador = False
                    turno.count_turno = 0
                    hacer_daño(self.jugador,self.cpu,daño=2)
                    self.change_turn()
                    
            # Ventajas
            elif contricante in pokemones[pokepoke]['Ventajas']:
                if turno.potenciador:
                    if turno.count_potenciador < 2:
                        hacer_daño(self.jugador,self.cpu,daño=7)
                        self.change_turn()
                        
                    else:
                        turno.potenciador = False
                        turno.count_turno = 0
                        hacer_daño(self.jugador,self.cpu,daño=5)
                        self.change_turn()
                        
                else:
                    hacer_daño(self.jugador,self.cpu,daño=5)
                    self.change_turn()
            # Normal
            else:
                if turno.potenciador:
                    if turno.count_potenciador < 2:
                        turno.count_turno = 0
                        hacer_daño(self.jugador,self.cpu,daño=5)
                        self.change_turn()
                        
                    else:
                        turno.potenciador = False
                        turno.count_turno = 0
                        hacer_daño(self.jugador,self.cpu,daño=3)
                        self.change_turn()
                        
                else:
                    hacer_daño(self.jugador,self.cpu,daño=3)
                    self.change_turn()
        # Ataque especial
        elif ataque_ == arbol_ataque[3]:
                if turno.count_potenciador > 1 and turno.count_turno > 2:
                    turno.potenciador = True
                    turno.count_turno = 0
                    print('Habilidad usada')
                    self.change_turn()
                    return True
                else:
                    turno.potenciador = False
                    print('No es posible usar esta habilidad')
                    self.change_turn()
                    return None
        # Resto de ataques
        else:
            thepoke = selection_pokemon[elpoke]
            if thepoke == 'Electer':
                hacer_daño(self.jugador,self.cpu,daño=3)
                self.change_turn()
                
            else:
                hacer_daño(self.jugador,self.cpu,daño=2)
                self.change_turn()
                      


class Turno:

    def __init__(self):
        self.ronda = ronda
        self.count_turno = 0
        self.count_potenciador = 0
        self.potenciador = None
    
    def entregar_turno(self):
        global potenciador_cpu
        global potenciador_jugador
        global count_cpu_turno
        global count_jugador_turno
        global count_potenciador_jugador
        global count_potenciador_cpu
        if self.ronda == True:
            cct =  count_cpu_turno + 1
            count_cpu_turno = cct
            self.count_turno = count_cpu_turno
            cpc =  count_potenciador_cpu + 1
            count_potenciador_cpu = cpc
            self.count_potenciador = count_potenciador_cpu
            potenciador_cpu = self.potenciador
            self.potenciador = copy.copy(potenciador_cpu)
            return self
        else:
            cjt = count_jugador_turno + 1
            count_jugador_turno = cjt
            self.count_turno = count_jugador_turno
            cpj = count_potenciador_jugador + 1
            count_potenciador_jugador = cpj
            self.count_potenciador =cpj
            potenciador_jugador = self.potenciador
            self.potenciador = copy.copy(potenciador_jugador)
            return self

if __name__ == '__main__':
    name = user_name
    chris = Entrenador(indice=2, name=name)
    batalla = Duelo(chris)
    poke_cpu = batalla.cpu.poke
    print("///////")
    print("Eleccion de pokemon aleatorio CPU")
    print(f'CPU eligio a {poke_cpu}')
    print("///////")
    print(f'Turno-{ronda}')
    el_turno = batalla.flip_coin()
    print(f'Turno-{ronda}')
    print("Tu pokemon es Electer")
    while status == False:
        if ronda:
            cpu_ataque = batalla.ai_selection(poke_cpu)
            batalla.seleccion_ataque(cpu_ataque)
        else:
            print("///////")

            print("Elige tu ataque (Arañazo, Trueno, Campo Magnetico)")
            mipokeataque = input('Da la orden > ')
            batalla.seleccion_ataque(mipokeataque)


###
#Ataques para poner en consola
###
# Arañazo
# Trueno
# Campo magnético