# -*- coding: utf-8 -*-
import os


def pCalculadora(salir):

    while not salir:
        os.system('clear')

        print ("Seleccione una operacion:")
        print ("+ para sumar")
        print ("- para restar")
        print ("* para multiplicar")
        print ("/ para dividir")

        operacion = raw_input("Su operacion es: ")

        if operacion == "+" or operacion == "-" or operacion == "*" \
        or operacion == "/":

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

            print ("El resultado es:")
            print (resultado)

        else:
            print ("Opcion incorrecta")

        respuesta = raw_input("Desea salir de la aplicacion? s n: ")

        while respuesta != "s" and respuesta != "n":
            respuesta = raw_input("Desea salir de la aplicacion? s n: ")

        if respuesta == "s":
            salir = True

pCalculadora(False)