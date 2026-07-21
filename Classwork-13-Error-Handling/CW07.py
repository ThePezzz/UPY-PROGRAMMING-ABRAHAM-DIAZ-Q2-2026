# DIGITO VERIFICADOR - ROL UTFSM

class RolInvalidError(Exception):
    pass


def calcular_digito(rol_sin_digito):
    secuencia = [2, 3, 4, 5, 6, 7]
    inverso = rol_sin_digito[::-1]
    suma = 0

    for index in range(len(inverso)):
        numero = int(inverso[index])
        suma += numero * secuencia[index % 6]

    resultado = suma % 11
    digito = 11 - resultado

    if digito == 11:
        digito = "0"
    elif digito == 10:
        digito = "K"
    else:
        digito = str(digito)

    return digito


rol = input("Escribe el rol (formato XXXXXXXXX-X): ").strip()

try:
    partes = rol.split("-")

    if len(partes) != 2:
        raise RolInvalidError("No tiene el formato XXXXXXXXX-X")

    rol_sin_digito, digito_ingresado = partes

    if not rol_sin_digito.isdigit():
        raise RolInvalidError("Los digitos del rol deben ser numericos")

    if not digito_ingresado.isdigit() and digito_ingresado.upper() != "K":
        raise RolInvalidError("El digito verificador debe ser numerico")

    digito_calculado = calcular_digito(rol_sin_digito)

    if digito_calculado != digito_ingresado.upper():
        raise RolInvalidError(
            f"Error: El digito verificador no coincide, se esperaba {digito_calculado}"
        )

except RolInvalidError as error:
    print(f"Rol invalido: {error}")

except Exception as error:
    print(f"Ocurrio un error inesperado: {error}")

else:
    print(f"{rol_sin_digito}-{digito_calculado}")
