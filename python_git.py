#Ejercicio diccionario de hoy: usuarios:

import os
import time
import msvcrt

nario = {
    "identificador": 1,
    "Nombre": "Hottely",
    "Direccion": "Avenida Bernando O'higgins 1833",
    "Funcionando": True,
    "valor_hab": 120000
}
usuarios = []
while True:
    print("""
          1. Inicio de sesion
          2. Registrar usuario
          3. Eliminar usuario
          4. Salir""")
    while True:
        try:
            opc = int(input("Ingrese opcion: "))
            if opc in (1,2,3,4):
                break
            else:
                print("Error, opcion no disponible")
        except:
            print("Error, solo se permiten numeros enteros!")
        
    if opc==1:
        pass
    elif opc==2:
        pass
    elif opc==3:
        pass
    else:
        print("Hasta luego!")
        break