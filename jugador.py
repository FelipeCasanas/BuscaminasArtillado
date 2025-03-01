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

    def obtenerRegistros(self):
        for i in range(len(self.historialX)):
            print(f'Se disparo a las coordenadas [{self.historialX[i]}, {self.historialY[i]}] en el turno #{i + 1}')

    def disparar(self, campoBatalla, coordenadaX, coordenadaY):    
        coordenadaX, coordenadaY = int(coordenadaX), int(coordenadaY)
        listaMinas = [[int(x), int(y)] for x, y in campoBatalla.obtenerUbicacionMinas()]

        if campoBatalla.enRango(campoBatalla, coordenadaX, coordenadaY):
            if [coordenadaX, coordenadaY] in self.minasEncontradas:
                print(f'La mina [{coordenadaX}, {coordenadaY}] ya fue encontrada\n')
            else:
                if [coordenadaX, coordenadaY] in listaMinas:
                    self.minasEncontradas.append([coordenadaX, coordenadaY])
                    self.incrementarPuntaje()
                    self.incrementarOportunidad()
                    print(f'¡¡Acertaste!! Ganas un punto y una oportunidad!!\nEl nuevo puntaje es: {self.obtenerPuntaje()}\n')
                else:
                    print('¡¡Fallaste el disparo!! Pierdes una oportunidad\n')

                    if len(listaMinas) == 1:
                        distancia = self.obtenerDistanciaObjetivo(campoBatalla, coordenadaX, coordenadaY)
                        print(f'La mina esta a {distancia} unidades en alguna direccion')
                        
                    self.decrementarOportunidad()

            self.agregarRegistro(coordenadaX, coordenadaY)
            self.turno += 1

    def obtenerDistanciaObjetivo(self, campoBatalla, coordenadaX, coordenadaY):
        '''
        1. Obtiene coordenadaX y coordenadaY
        2. Obtiene la lista de minas
        3. Calcula la distancia manhattan (valor absoluto de la diferencia en X e Y)
        4. Devuelve la distancia
        '''

        # Obtener lista de minas
        listaMinas = [[int(x), int(y)] for x, y in campoBatalla.obtenerUbicacionMinas()]
        
        if not listaMinas:  # Verificar que haya al menos una mina
            return None  # O puedes devolver un valor indicativo, como -1

        # Tomar la primera mina de la lista
        posicionMinaX, posicionMinaY = listaMinas[0]

        # Calcular distancia de Manhattan
        distanciaX = abs(coordenadaX - posicionMinaX)
        distanciaY = abs(coordenadaY - posicionMinaY)

        return distanciaX + distanciaY

    def reiniciarEstadisticas(self):
        self.establecerPuntaje(0)
        self.establecerTurno(1)
        self.establecerOportunidades(1)
        self.eliminarRegistros()

    def cambiarNombre(self, nombre):
        self.nombre = nombre
        
    def obtenerNombre(self):
        return self.nombre

    def establecerOportunidades(self, oportunidades):
        self.oportunidades = oportunidades

    def obtenerOportunidades(self):
        return self.oportunidades
    
    def incrementarOportunidad(self):
        self.oportunidades += 1

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
        self.historialX = []
        self.historialY = []