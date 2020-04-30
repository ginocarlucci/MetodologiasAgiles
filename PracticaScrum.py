import re

def sumar(caracteres):

    separator = ","

    if "\n" in caracteres:
        particion = caracteres.partition("\n")
        if particion[0][:2] == '//':
            separator = particion[0][2:]
            caracteres = particion[2]

    caracteres = caracteres.replace("\n", separator)
    arreglo_de_numeros = caracteres.split(separator)
    sumatoria = 0

    negative_numbers = []
    if caracteres == "":
        return 0
    for i in arreglo_de_numeros:
        if i == "":
            continue
        float_value = float(i)
        if float_value < 0:
            negative_numbers.append(str(float_value))

        float_value = round(float_value)
        if float_value <= 1000:
            sumatoria = sumatoria + float_value

    if len(negative_numbers):
        raise Exception("Se han ingresado numeros negativos: " + ",".join(negative_numbers))

    return sumatoria

#cadena = str(input())
#print(sumar(cadena))
