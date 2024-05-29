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
listuser = []
listpass = []
while True:
    os.system("cls")
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

    os.system("cls")   
    if opc==1:
        pass
    elif opc==2:
        print("-"*20)
        print("Registrar usuario")
        print("-"*20)
        while True:
            usuario = input("Ingrese nombre de usuario: ")
            if len(usuario) > 3:
                break
            else:
                print("Error, el usuario debe contener al menos 3 caracteres!")
        while True:
            senia = input("Ingrese contraseña: ")
            if len(senia) > 3:
                break
            else:
                print("Error, la contraseña debe contener al menos 3 caracteres")
        print("-"*20)
        print("Usuario registrado!")
        print("Presione una tecla para continuar")
        print("-"*20)
        msvcrt.getch()

        listuser.append(usuario)
        listpass.append(senia)

    elif opc==3:
        print("-"*20)
        print("Eliminar usuario")
        print("-"*20)
        while True:
            elim = input("Ingrese usuario a eliminar: ")
            if elim in listuser:
                listuser.remove(usuario)
                print("-"*20)
                print("Usuario eiminado con exito!")
                print("Presione tecla para continuar")
                print("-"*20)
                msvcrt.getch()
                break
            else:
                print("Usuario no existente!")

    else:
        print("Hasta luego!")
        break