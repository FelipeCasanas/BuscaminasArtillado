from generador import CampoBatalla
from jugador import Jugador

print('\nBienvenido a Buscaminas!!')

campoBatalla = None
jugador = None

def crearCampoBatalla():
    opcionInvalida = True
    tamanoCuadricula = int(input('\nQue tamaño va a tener la cuadricula del juego?: '))
    campoBatalla = CampoBatalla(tamanoCuadricula, 0)

    autoRellenarMinas = int(input('\nQuieres una cantidad de minas aleatoria?\n1. Si\n2. No\nEscribe aqui: '))
    
    while opcionInvalida:
        if autoRellenarMinas == 1:
            campoBatalla.establecerCantidadMinasAleatoria(1)
            campoBatalla.plantarMinas()
            return campoBatalla
        elif autoRellenarMinas == 2:
            campoBatalla.establecerCantidadMinas()
            campoBatalla.plantarMinas()
            return campoBatalla
        else:
            print('La opcion no existe, vuelva a intentarlo')

def crearJugador():
    nombre = input('Escribe tu nombre: ')
    print('Jugador creado!')
    return Jugador(nombre, 1, 1, 0)

def comenzarJuego(jugador):
    jugar = True
    campoBatalla = crearCampoBatalla()

    oportunidades = int(input('Cuantos intentos quieres tener?: '))
    jugador.establecerOportunidades(oportunidades)

    while jugar:
        if jugador.obtenerOportunidades() > 1:
            print(f'\nTurno #{jugador.obtenerTurno()}\nOportunidades restantes: {jugador.obtenerOportunidades()}\n -> ¡Dispara!')    
        elif jugador.obtenerOportunidades() == 1:
            print(f'\nTurno #{jugador.obtenerTurno()}\nOportunidades restantes: {jugador.obtenerOportunidades()}\n -> ¡Es tu ultima oportunidad, no puedes fallar!')
        else:
            print(f'Perdiste el juego {jugador.obtenerNombre()}!! Seras retirado del servicio activo GRANUJA >:(')
            jugador.reiniciarEstadisticas()
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
            mensaje = f'\nQue opcion vas a escoger {jugador.obtenerNombre()}?:\n1. Jugar \n2. Crear jugador \n3. Creditos \n4. Salir\nEscribe aqui: '
        else:
            mensaje = '\nEscoge lo que quieres hacer:\n1. Jugar \n2. Crear jugador \n3. Creditos \n4. Salir\nEscribe aqui: '
        
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
            print('\nBuscaminas Artillado\nCreador: Felipe Casañas - ADSO 07\nCasanas Software - 2025\n')
        elif accion == 4:
            exit(0)
        else:
            opcionInvalida = True
            print('La opcion no existe\n')


mostrarMenu(jugador)