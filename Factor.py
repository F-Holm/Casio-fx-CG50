#!/usr/bin/env python3

"""
Script de factorización en números primos para Casio fx-CG50
------------------------------------------------------------
Este programa recibe un número natural desde la entrada
y muestra su descomposición en factores primos en formato:

Factor(n)

p^k
q
r^m

Donde p, q, r son números primos y k, m son sus exponentes.

Restricciones:
- Solo acepta números naturales (>= 1).
- Si la entrada no es válida, el programa termina con un error.
"""

def prime_factors_lines(n):
    """
    Devuelve una lista de strings representando
    los factores primos de n en forma legible.
    Ejemplo: 72 -> ["2^3", "3^2"]
    """
    parts = []
    d = 2
    while d * d <= n:
        exp = 0
        while n % d == 0:
            n //= d
            exp += 1
        if exp > 0:
            if exp == 1:
                parts.append(str(d))                    # factor sin exponente
            else:
                parts.append("{}^{}".format(d, exp))    # factor con exponente
        d += 1 if d == 2 else 2                         # optimización: después del 2 solo impares
    if n > 1:
        parts.append(str(n))                            # si queda un primo grande al final
    return parts

def main():
    """Función principal: lee, valida y muestra la factorización"""
    try:
        num = int(input("Numero: "))
    except ValueError:
        print("Error: el programa solo acepta numeros naturales")
        return

    if num < 1:
        print.exit("Error: el programa solo acepta numeros naturales (>= 1)")
        return

    factors = prime_factors_lines(num)

    print("Factor({})\n".format(num))
    for f in factors:
        print(f)

main()