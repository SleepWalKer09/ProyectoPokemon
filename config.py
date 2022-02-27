# variables = {
#     Personaje:0,
#     Nombre:str,
#     Nombre2:str,
#     contra:0,
#     juego:0,
#     t:0,
#     tipo1:str,
#     tipo2:str,
#     pot_1:0,
#     pot_2:0,
#     contador_pot1:0,
#     contador_pot2:0,
#     Vidajugador:25,
#     cpu:int,
#     Vidacpu:int,
# }

user_name ='Chris'
ronda = False
potenciador_jugador = [True]
potenciador_cpu = [True]
count_potenciador_jugador = 0
count_potenciador_cpu = 0
selected_potenciador_cpu = 0
selected_potenciador_jugador = 0
ataque_cpu = ''
ataque_jugador = ''
user_selection:int
cpu_selection:int
count_cpu_turno = 3
count_jugador_turno = 3
status = False

selection_pokemon = {0:'Aquarder',1:'Firesor',2:'Electer',3:'Mousebug',4:'Splant',5:'Rockdog'}

pokemones = {
    'Aquarder':{
        'Aqua-jet':True,
        'Cola férrea':2,
        'Cabezazo':2,
        'Lluvia':True,
        'Ventajas':[1,5],
        'Desventajas':[2,4],
    },
    'Firesor':{
        'Llamarada':True,
        'Embestida':2,
        'Mordisco':2,
        'Día soleado':True,
        'Ventajas':[3,4],
        'Desventajas':[0,5],
    },
    'Electer':{
        'Trueno':True,
        'Arañazo':3,
        'Mordisco':3,
        'Campo magnético':True,
        'Ventajas':[0,3],
        'Desventajas':[4,5],
    },
    'Mousebug':{
        'Picotazo':True,
        'Embestida':2,
        'Cabezazo':2,
        'Esporas':True,
        'Ventajas':[4,5],
        'Desventajas':[1,2],
    },
    'Splant':{
        'Hoja navaja':True,
        'Mordisco':2,
        'Cabezazo':2,
        'Rayo solar':True,
        'Ventajas':[0,2,5],
        'Desventajas':[1,3],
    },
    'Rockdog':{
        'Roca afilado':True,
        'Velocidad':2,
        'Cola ferrea':2,
        'Campo rocoso':True,
        'Ventajas':[1,2],
        'Desventajas':[0,4],
    },
}