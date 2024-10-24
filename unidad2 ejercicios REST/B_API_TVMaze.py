import requests
import json

def obtener_datos_programa(nombre_programa):
    url = f"https://api.tvmaze.com/search/shows?q={nombre_programa}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        if datos:
            return datos[0]
        else:
            return None
    else:
        return None

def obtener_datos_genero(genero):
    url = f"https://api.tvmaze.com/search/shows?q={genero}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        return datos
    else:
        return None

def mostrar_menu():
    print("Menú:")
    print("1. Buscar por nombre")
    print("2. Buscar por género")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            nombre_programa = input("Ingrese el nombre del programa: ")
            if nombre_programa:
                datos = obtener_datos_programa(nombre_programa)
                if datos:
                    print("Nombre:", datos["show"]["name"])
                    print("Resumen:", datos["show"]["summary"])
                    print("Género:", datos["show"]["genres"])
                    print("País:", datos["show"]["network"]["country"]["name"])
                else:
                    print("No se encontraron datos para el programa")
            else:
                print("Ingrese un nombre válido")
        elif opcion == "2":
            genero = input("Ingrese el género: ")
            if genero:
                datos = obtener_datos_genero(genero)
                if datos:
                    for programa in datos:
                        print("Nombre:", programa["show"]["name"])
                        print("Resumen:", programa["show"]["summary"])
                        print("Género:", programa["show"]["genres"])
                        print("País:", programa["show"]["network"]["country"]["name"])
                        print("--------------------")
                else:
                    print("No se encontraron datos para el género")
            else:
                print("Ingrese un género válido")
        elif opcion == "3":
            print("Adiós")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()