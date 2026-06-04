from datos import cuentas

def consultar_cuenta():
    numero = int(input("Ingrese número de cuenta: "))
    while numero not in cuentas:
        print("Datos incorrectos, intente nuevamente.")
        numero = int(input("Ingrese número de cuenta: "))
    
    # Ahora está FUERA del while, se ejecuta siempre que la cuenta sea válida
    print("\nDatos de la cuenta")
    print("DNI:", cuentas[numero]["dni"])
    print("Nombre:", cuentas[numero]["nombre"])
    print("Tipo:", cuentas[numero]["tipo"])
    print("Saldo: $", cuentas[numero]["saldo"])

def realizar_deposito():
    numero = int(input("Ingrese numero de cuenta: "))
    while numero not in cuentas:
        print("Los datos son incorrectos, intente nuevamente.")
        numero = int(input("Ingrese número de cuenta: "))
    monto = float(input("Ingrese el monto que desea depositar: "))
    if monto > 0:
        cuentas[numero]["saldo"] += monto
        print("Depósito realizado, retire su ticket")
        print("Nuevo saldo: $", cuentas[numero]["saldo"])
    else:
        print("El monto debe ser mayor a cero.") 

def realizar_extraccion():
    numero = int(input("Ingrese numero de cuenta: "))
    while numero not in cuentas:
        print("Datos incorrectos, intente nuevamente.")
        numero = int(input("Ingrese número de cuenta: "))
    monto = float(input("Ingrese el monto que desea extraer: "))
    if monto > 0:
        if cuentas[numero]["saldo"] >= monto:
            cuentas[numero]["saldo"] -= monto
            print("Extracción realizada, retire su ticket")
            print("Nuevo saldo: $", cuentas[numero]["saldo"])
        else:
            print("Saldo insuficiente para realizar la extracción.")
    else:
        print("El monto debe ser mayor a cero.")

def listar_clientes():
    print("\nLISTADO DE CLIENTES")
    for numero, datos in cuentas.items():
        print("--------------------------------------")
        print("Número de cuenta:", numero)
        print("DNI:", datos["dni"])
        print("Nombre:", datos["nombre"])
        print("Tipo:", datos["tipo"])
        print("Saldo: $", datos["saldo"])