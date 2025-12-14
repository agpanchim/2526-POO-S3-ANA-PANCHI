## Programa: Promedio semanal del clima
# Paradigma: Programación Orientada a Objetos
# Autor: Ana Gissela Panchi Mallitasig
# Descripción:
#   Contiene la clase Temperatura_POO que maneja las temperaturas
#   semanales y calcula el promedio.
# Clase que maneja Temperatura_POO semanal

class Temperatura_POO:
    def __init__(self):
        # Encapsulamiento: atributo privado
        self.__temperaturas = []

    def ingresar_temperaturas(self):
        # Método para ingresar temperaturas diarias
        for dia in range(7):
            temp = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
            self.__temperaturas.append(temp)

    def calcular_promedio(self):
        # Método para calcular el promedio semanal
        return sum(self.__temperaturas) / len(self.__temperaturas)