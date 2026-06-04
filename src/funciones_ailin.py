from datos import cuentas

def alta_cuenta():
    numero = int(input("Ingrese número de cuenta: "))
    if numero in cuentas:
        print("El número de cuenta ya existe.")
        return
    dni = int(input("Ingrese DNI: "))
    nombre = input("Ingrese nombre del titular: ")
    tipo = input("Ingrese tipo de cuenta: ")
    saldo = float(input("Ingrese saldo inicial: "))
    cuentas[numero] = {
        "dni": dni,
        "nombre": nombre,
        "tipo": tipo,
        "saldo": saldo
    }
    print("Cuenta creada con éxito.")

def baja_cuenta():
    numero = int(input("Ingrese número de cuenta a eliminar: "))
    if numero in cuentas:
        del cuentas[numero]
        print("Cuenta eliminada con éxito.")
    else:
        print("La cuenta no existe.")

def modificar_cuenta():
    numero = int(input("Ingrese número de cuenta a modificar: "))
    if numero not in cuentas:
        print("La cuenta ingresada no existe.")
        return
    
    print("\nDatos actuales:")
    print("DNI:", cuentas[numero]["dni"])
    print("Nombre:", cuentas[numero]["nombre"])
    print("Tipo:", cuentas[numero]["tipo"])
    print("Saldo actual: $", cuentas[numero]["saldo"])
    print("-" * 30)
    
    # Se sobrescriben los datos de forma segura en el diccionario global
    cuentas[numero]["dni"] = int(input("Nuevo DNI: "))
    cuentas[numero]["nombre"] = input("Nuevo nombre: ")
    cuentas[numero]["tipo"] = input("Nuevo tipo de cuenta: ")
    # Conservamos el saldo que ya tenía la cuenta
    print("Cuenta modificada correctamente.")