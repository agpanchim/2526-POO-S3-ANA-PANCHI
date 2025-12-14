# Programa: Promedio semanal del clima
# Paradigma: Programación Tradicional
# Autor: Ana Gissela Panchi Mallitasig

# Función que solicita al usuario las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []           # lista vacía para almacenar las temperaturas

    for dia in range(7):        # Bucle que se repite 7 veces
        temp = float(input(f"Ingrese la temperatura del día {dia + 1}: ")) #solicitud temperatura
        temperaturas.append(temp)       # Agrega la temperatura ingresada a la lista

    return temperaturas

# Función que calcula el promedio semanal
def calcular_promedio(temperaturas):
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio

# Función principal del programa
def main():
    print ()
    print(" Promedio semanal del clima (Tradicional) ")
    print()

    lista_temperaturas = ingresar_temperaturas()        # llama a la función para ingresar las temperaturas

    # Se calcula el promedio semanal llamando a la función correspondiente
    promedio_semanal = calcular_promedio(lista_temperaturas)
    print()

    # Se muestra el resultado final en pantalla
    print(f"El promedio semanal es: {promedio_semanal:.2f} °C")


# Llamada a la función principal para ejecutar el programa
main()