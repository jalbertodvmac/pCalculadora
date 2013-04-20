# -*- coding: utf-8 -*-


def pCalculadora(salir):

    while not salir:
        print ("Seleccione una operacion:")
        print ("+ para sumar")
        print ("- para restar")
        print ("* para multiplicar")
        print ("/ para dividir")

        operacion = raw_input("Su operacion es: ")

        print ("Introduzca los operadores:")

        operador1 = float(raw_input("Primer operador: "))
        operador2 = float(raw_input("Segundo operador: "))

        if operacion == "+":
            resultado = operador1 + operador2

        elif operacion == "-":
            resultado = operador1 - operador2

        elif operacion == "*":
            resultado = operador1 * operador2

        elif operacion == "/":
            resultado = operador1 / operador2

        else:
            print ("Opcion incorrecta")
            pCalculadora(False)

        print ("El resultado es:")
        print (resultado)

        if (raw_input("Desea salir de la aplicacion? s n: ") == "s"):
            salir = True

pCalculadora(False)