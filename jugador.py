from generador import CampoBatalla

class Jugador():

    def __init__(self, nombre, oportunidades, turno, puntaje):
        self.nombre = nombre
        self.oportunidades = oportunidades
        self.turno = turno
        self.puntaje = puntaje
        self.historialX = []
        self.historialY = []
        self.minasEncontradas = []

    def cambiarNombre(self, nombre):
        self.nombre = nombre
        
    def obtenerNombre(self):
        return self.nombre

    def establecerOportunidades(self, oportunidades):
        self.oportunidades = oportunidades

    def obtenerOportunidades(self):
        return self.oportunidades
    
    def decrementarOportunidad(self):
        self.oportunidades -= 1

    def obtenerTurno(self):
        return self.turno
    
    def establecerTurno(self, nuevoTurno):
        self.turno = nuevoTurno
    
    def incrementarTurno(self):
        self.turno += 1

    def establecerPuntaje(self, nuevoPuntaje):
        self.puntaje = nuevoPuntaje
    
    def incrementarPuntaje(self):
        self.puntaje += 1

    def obtenerPuntaje(self):
        return self.puntaje
    
    def agregarRegistro(self, coordenadaX, coordenadaY):
        self.historialX.append(coordenadaX)
        self.historialY.append(coordenadaY)

    def eliminarRegistros(self):
        self.historialX.clear
        self.historialY.clear

    def mostrarRegistros(self):
        i = 0

        while i < self.cantidadIntentos:
            print(f'Se disparo a las coordenadas {self.historialX[i]}, {self.historialY[i]} en el turno #{i}\n')
            i += 1

    def disparar(self, campoBatalla, coordenadaX, coordenadaY):    
        coordenadaX, coordenadaY = int(coordenadaX), int(coordenadaY)
        listaMinas = [[int(x), int(y)] for x, y in campoBatalla.obtenerUbicacionMinas()]

        if [coordenadaX, coordenadaY] in self.minasEncontradas:
            print(f'La mina [{coordenadaX}, {coordenadaY}] ya fue encontrada\n')
        else:
            if [coordenadaX, coordenadaY] in listaMinas:
                self.minasEncontradas.append([coordenadaX, coordenadaY])
                self.incrementarPuntaje()
                print(f'¡¡Acertaste y ganas un punto!!\nEl nuevo puntaje es: {self.obtenerPuntaje()}\n')
            else:
                print('¡¡Fallaste el disparo!! Pierdes una oportunidad\n')
                self.decrementarOportunidad()

        self.agregarRegistro(coordenadaX, coordenadaY)
        self.turno += 1

    def reiniciarEstadisticas(self):
        self.establecerPuntaje(0)
        self.establecerTurno(1)
        self.establecerCantidadIntentos(1)
        self.eliminarRegistros()