# Classwork 08
import math


class IntegrationError(Exception):
    pass


def leer_limite(mensaje):
    texto = input(mensaje).strip()
    if texto.lower() == "pi":
        return math.pi
    try:
        return float(texto)
    except ValueError:
        raise IntegrationError("debe ser numerico")


try:
    try:
        a = leer_limite("Enter the left endpoint of the interval ")
    except IntegrationError:
        raise IntegrationError("El limite inferior debe ser numerico")

    try:
        b = leer_limite("Enter the right endpoint of the interval ")
    except IntegrationError:
        raise IntegrationError("El limite superior debe ser numerico")

    if a >= b:
        raise IntegrationError("El limite inferior debe ser menor que el limite superior")

    f_x = input("Enter the function to integrate (use 'x' as the variable) ").strip()

    if f_x == "":
        raise IntegrationError("La funcion ingresada no es valida")

    if "^" in f_x:
        raise IntegrationError("La funcion ingresada no es valida")

    variables_usadas = set(ch for ch in f_x if ch.isalpha())
    palabras_permitidas = {"m", "a", "t", "h", "s", "i", "n", "c", "o", "e", "x", "l", "g", "p", "q", "r", "u", "d"}
    if "x" not in f_x:
        raise IntegrationError("La funcion debe estar escrita en terminos de x")

    try:
        prueba = f_x.replace('x', str((a + b) / 2))
        eval(prueba)
    except ZeroDivisionError:
        raise IntegrationError("La funcion no esta definida en algun punto del intervalo")
    except Exception:
        raise IntegrationError("La funcion ingresada no es valida")

    method = input("Enter the method to use (LRM/RRM/MPM/TM) ").strip().upper()

    if method not in ("LRM", "RRM", "MPM", "TM"):
        raise IntegrationError("El metodo de integracion no es valido. Usa LRM, RRM, MPM o TM")

    n = 1000
    h = (b - a) / n

    try:
        if method == "TM":
            total = 0.0
            for i in range(n + 1):
                xi = a + i * h
                yi = eval(f_x.replace('x', str(xi)))
                if i == 0 or i == n:
                    total += yi
                else:
                    total += 2 * yi
            area = (h / 2) * total
        else:
            shift = 0
            constant = 0
            if method == "RRM":
                shift = 1
            elif method == "MPM":
                constant = h / 2

            area = 0.0
            for i in range(0 + shift, n + shift):
                xi = a + i * h + constant
                height = eval(f_x.replace('x', str(xi)))
                area += height * h
    except ZeroDivisionError:
        raise IntegrationError("La funcion no esta definida en algun punto del intervalo")

except IntegrationError as error:
    print(f"{error}")

except Exception as error:
    print(f"Ocurrio un error inesperado: {error}")

else:
    print(f"The integration of {f_x} is {area:.3f}")
