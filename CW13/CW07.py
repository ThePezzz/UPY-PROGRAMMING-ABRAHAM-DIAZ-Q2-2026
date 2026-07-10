# DÍGITO VERIFICADOR - ROL UTFSM

rol = input("Escribe un rol: ")

try:

    rol_sin_digito, digito = rol.split("-")
except ValueError:
    print("El rol debe tener el formato XXXX-0")
    exit()

inverso = rol_sin_digito[::-1] + "-"

secuencia  = [2, 3, 4, 5, 6, 7]
suma = 0

for index in range(len(inverso)):
    numero = int(inverso[index])
    suma += numero * secuencia[index % 6]

resultado = suma % 11
digito_calculado = 11 - resultado

print(f"\nRol invertido:      {rol_invertido}")
print(f"Suma total:         {suma}")
print(f"Suma % 11:          {modulo}")
print(f"11 - {modulo}:             {digito_verificador}")
print(f"\nROL completo: {rol}-{digito_verificador}")