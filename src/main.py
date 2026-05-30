# Módulos de funcionalidades del sistema bancario.
# Cada integrante desarrolló un conjunto de funciones
# que son integradas desde este archivo principal.

from funciones_ailin import alta_cuenta, baja_cuenta, modificar_cuenta
from funciones_ailen import consultar_cuenta, realizar_deposito, realizar_extraccion, listar_clientes

# Menú principal del sistema.
# El programa permanece en ejecución hasta que el usuario seleccione
# la opción 8 (Salir). La variable 'opcion' se utiliza para controlar
# la continuidad del bucle principal.

opcion = 0

while opcion !=8:
    print("1. Alta de cuenta")
    print("2. Baja de cuenta")
    print("3. Modificar datos")
    print("4. Consultar cuenta")
    print("5. Realizar Depósito")
    print("6. Realizar Extracción")
    print("7. Listar Clientes")
    print("8. Salir")

    opcion = int(input("Opción: "))

    if opcion == 1:
        alta_cuenta()
    
    elif opcion == 2:
        baja_cuenta()
    
    elif opcion == 3:
        modificar_cuenta()
    
    elif opcion == 4:
        consultar_cuenta()
    
    elif opcion == 5:
        realizar_deposito()

    elif opcion == 6:
        realizar_extraccion()

    elif opcion == 7:
        listar_clientes()
