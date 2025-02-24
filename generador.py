import random

class CampoBatalla():

    def __init__(self, tamanoCuadricula, cantidadMinas):
        self.tamanoCuadricula = tamanoCuadricula
        self.cantidadMinas = cantidadMinas
        self.listaMinas = []

    def establecerTamano(self, tamano):
        self.tamanoCuadricula = tamano

    def obtenerTamanoCuadricula(self):
        return self.tamanoCuadricula

    def establecerMinasManualmente(self):
        opcionInvalida = True

        while opcionInvalida:
            cantidadMinas = int(input('\nCuantas minas va a tener el campo de batalla?: '))
            if cantidadMinas < self.tamanoCuadricula**2:
                self.cantidadMinas = cantidadMinas
                opcionInvalida = False
            else:
                print('La cantidad de minas no puede superar el tamaño de la cuadricula')
        
    def establecerMinasAleatorias(self, multiplicador):
        self.cantidadMinas = random.randint(1, int((self.tamanoCuadricula**2) - self.tamanoCuadricula * multiplicador))
        print(f'Minas generadas: {self.obtenerCantidadMinas()}\n')

    def obtenerCantidadMinas(self):
        return self.cantidadMinas
    
    def establecerCantidadMinas(self, cantidadMinas):
        self.cantidadMinas = cantidadMinas
    
    def obtenerUbicacionMinas(self):
        return self.listaMinas


    def plantarMinas(self):
        cantidadMinas = self.cantidadMinas
        while cantidadMinas > 0:
            coordenadaX = random.randint(1, self.tamanoCuadricula)
            coordenadaY = random.randint(1, self.tamanoCuadricula)

            if [coordenadaX, coordenadaY] not in self.listaMinas:
                self.listaMinas.append([coordenadaX, coordenadaY])
                cantidadMinas -= 1
