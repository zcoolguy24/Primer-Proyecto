from sumar import sumar
from restar import restar
from multiplicar import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def mostrar_menu():
    print("--- Calculadora ---")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Sumar N cantidad de números")
    print("6. Salir")

def obtener_opcion():
    try:
        opcion = int(input("Elige una opción: "))
        if 1 <= opcion <= 6:
            return opcion
        else:
            print("No válido. Elige un número del 1 al 6.")
            return obtener_opcion()
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número.")
        return obtener_opcion()

def obtener_dos_numeros():
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    return a, b

def ejecutar_opcion(opcion):
    if opcion == 1:
       a, b = obtener_dos_numeros()
       print(f"Resultado: {sumar(a, b)}")

    elif opcion == 2:
       a, b = obtener_dos_numeros()
       print(f"Resultado: {restar(a, b)}")

    elif opcion == 3:
       a, b = obtener_dos_numeros()
       print(f"Resultado: {multiplicar(a, b)}")

    elif opcion == 4:
       a, b = obtener_dos_numeros()
       print(f"Resultado: {dividir(a, b)}")

    elif opcion == 5:
       numeros = input("Introduce los números separados por comas: ")
       try:
           lista_numeros = [float(num) for num in numeros.split(",")]
           print(f"Resultado: {suma_avanzada(*lista_numeros)}")
       except ValueError:
           print("Entrada no válida. Por favor, introduce números separados por comas.")

    elif opcion == 6:
       print("Saliendo del programa...")
       exit()

def main():
    while True:
        mostrar_menu()
        opcion = obtener_opcion()
        ejecutar_opcion(opcion)

if __name__ == "__main__":
    main()