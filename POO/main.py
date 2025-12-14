# Descripción:
#   Archivo principal que ejecuta el programa POO.

# Importamos la clase Temperatura_POO desde Temperatura_POO.py
from Temperatura_POO import Temperatura_POO  # IMPORTACIÓN

def main():
    print()
    print(f" Promedio semanal de la temperatura (POO) ")
    print()

    clima = Temperatura_POO()       # Crear objeto
    clima.ingresar_temperaturas()   # Ingresar datos
    promedio = clima.calcular_promedio()  # Calcular promedio

    print()
    print(f"El promedio semanal es: {promedio:.2f} °C")

# Punto de entrada del programa
if __name__ == "__main__":
    main()