from generador import CampoBatalla
from jugador import Jugador

print('\nBienvenido a Buscaminas Artillado!!')

campoBatalla = None
jugador = None

def crearCampoBatalla():
    opcionInvalida = True
    tamanoCuadricula = int(input('\nQue tamaño va a tener la cuadricula del juego?: '))
    campoBatalla = CampoBatalla(tamanoCuadricula, 1)

    autoRellenarMinas = int(input('\nQuieres una cantidad de minas aleatoria?\n1. Si\n2. No\nEscribe aqui: '))
    
    while opcionInvalida:
        if autoRellenarMinas == 1:
            campoBatalla.establecerMinasAleatorias(1)
            campoBatalla.plantarMinas()
            return campoBatalla
        elif autoRellenarMinas == 2:
            campoBatalla.establecerMinasManualmente()
            campoBatalla.plantarMinas()
            return campoBatalla
        else:
            print('La opcion no existe, vuelva a intentarlo')

def crearJugador():
    nombre = input('Escribe tu apellido: ')
    print('Jugador creado!')
    return Jugador(nombre, 1, 1, 0)

def comenzarJuego(jugador):
    jugar = True
    campoBatalla = crearCampoBatalla()
    jugador.reiniciarEstadisticas()

    oportunidades = int(input('Cuantas oportunidades quieres tener?: '))
    jugador.establecerOportunidades(oportunidades)

    while jugar:
        if jugador.obtenerPuntaje() == campoBatalla.obtenerCantidadMinas():
            print(f'Felicidades soldado {jugador.obtenerNombre()}! Destruiste todas las minas\nSeras ascendido a Cabo!!\n')
            mostrarMenu(jugador)
            break

        if jugador.obtenerOportunidades() > 1:
            print(f'\nTurno #{jugador.obtenerTurno()}\nOportunidades restantes: {jugador.obtenerOportunidades()}\n -> ¡Dispara!')    
        elif jugador.obtenerOportunidades() == 1:
            print(f'\nTurno #{jugador.obtenerTurno()}\nOportunidades restantes: {jugador.obtenerOportunidades()}\n -> ¡Es tu ultima oportunidad, no puedes fallar!')
        else:
            print(f'Perdiste el juego {jugador.obtenerNombre()}!! Seras retirado del servicio activo GRANUJA >:(')
            mostrarMenu(jugador)
            break

        coordenadaX = int(input('Ingresa la coordenada en X: '))
        coordenadaY = int(input('Ingresa la coordenada en Y: '))
        jugador.disparar(campoBatalla, coordenadaX, coordenadaY)

def mostrarMenu(jugador):
    opcionInvalida = True
    accion = 0
    
    while opcionInvalida:
        if jugador != None:
            mensaje = f'\nQue opcion vas a escoger {jugador.obtenerNombre()}?:\n1. Jugar \n2. Crear jugador\n3. Estadisticas partida anterior \n4. Creditos \n5. Salir\nEscribe aqui: '
        else:
            mensaje = '\nEscoge lo que quieres hacer:\n1. Jugar \n2. Crear jugador\n3. Estadisticas partida anterior \n4. Creditos \n5. Salir\nEscribe aqui: '
        
        accion = int(input(mensaje))

        if accion == 1:
            if jugador != None:
                comenzarJuego(jugador)
            else:
                jugador = crearJugador()
                comenzarJuego(jugador)
        elif accion == 2:
            if jugador != None:
                print('\nYa existe un jugador')
            else:
                jugador = crearJugador()
        elif accion == 3:
            if jugador != None:
                print(f'\nEstadisticas partida:\nTurno alcanzado: {jugador.obtenerTurno() - 1}\nPuntaje alcanzado: {jugador.obtenerPuntaje()}\n\nRegistro de tus disparos:')
                jugador.obtenerRegistros()
            else:
                print('Aun no existen estadisticas, vuelve despues de jugar una partida ;)\n')
            
        elif accion == 4:
            print('\nBuscaminas Artillado\nCreador: Felipe Casañas - ADSO 07\nCasanas Software - 2025\n')
        elif accion == 5:
            exit(0)
        else:
            opcionInvalida = True
            print('La opcion no existe\n')


mostrarMenu(jugador)