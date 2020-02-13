import re

def bienvenida():
    print("Programa para resolver polinomios por el metodo de Newton-Raphson")
    print("ejemplo de un polinomio: ")
    print("x^4 + 4x^3 + 3x^2 + 2x + 11")
    print("")


def solicitar ():
    polinomio = input("ingrese un polinomio -> ")
    xo = input("ingrese el valor inicial ->")
    precision = input ("cuantos decimales de precisión ->")
    return polinomio,xo,precision


def tratamiento(polinomio):
    sin_negativos = polinomio.replace("-","+-")
    sin_espacios = sin_negativos.strip().replace(" ","")
    terminos = sin_espacios.split("+")
    limpio = [termino for termino in terminos if termino != '']
    return limpio


def separar(a_separar):
    lista = list()
    for termino in a_separar:
        if "x^" in termino:
            termino = termino.replace(variable,"")
            temp = termino.split("^")
            lista.append({'exponente':temp[1],'valor':temp[0]})
        elif "x" in termino:
            termino = termino.replace(variable,"^1")
            temp = termino.split("^")
            lista.append({'exponente':temp[1],'valor':temp[0]})
        else:
            lista.append({'exponente':'0','valor':termino})
    
    for elemento in lista:
        for k,v in elemento.items():
            if v =='':
                elemento[k] = "1"
            elif v =='-':
                elemento[k] = "-1"
    return lista


def derivar(terminos,variable):
    derivada = ''
    for termino in terminos:
        if int(termino['exponente'])>0:
            derivada+= str(int(termino['exponente'])*float(termino['valor']))+variable+'^'+str(int(termino['exponente'])-1)+"+"
    temp = tratamiento(derivada)
    derivadaL = separar(temp)
    return derivada,derivadaL


def evaluar(funcion,x,precision):
    res = 0.0
    for termino in funcion:
        res+= (float(x)**float(termino['exponente']))*float(termino['valor'])
    
    res = round(res,int(precision))
    return res

def iteracion(fx,fpx,xo,precision):
    aproximaciones = list()
    errAc = ('0.'+('0'*(int(precision)-1))+'1')
    errAcF = float(errAc)
    encontrada = False
    limite = 30
    while True:
        fxn = evaluar(fx,xo,precision)
        fpxn = evaluar(fpx,xo,precision)
        aproximacion = round(float(xo)-(fxn/fpxn),int(precision)) 
        xo = aproximacion
        aproximaciones.append(aproximacion)
        if(len(aproximaciones)>1):
            if abs(aproximaciones[len(aproximaciones)-1]-aproximaciones[len(aproximaciones)-2])<errAcF:
                encontrada = True
                break
        limite-=1
        if(limite == 0):
            break
    return aproximaciones, encontrada   
    
def imprimir(polinomio,aproximaciones,encontrada):
    
    print("polinomio ->"+polinomio)
    print("")
    if encontrada:
        tabla(aproximaciones)
    else:
        print("demasiadas iteraciones sin solucion")
        val = input("desea imprimir la tabla [y/n]-> ")
        if val.lower() == 'y':
            tabla(aproximaciones)
    
def tabla(aproximaciones):
    tamanio = 60
    print('-'*(tamanio+3))
    print('|{header}|'.format(header = 'APROXIMACIONES'.center(tamanio+1,'*').upper()))
    print('-'*(tamanio+2))
    for x in range(len(aproximaciones)):
        print('|{iteracion}|{aproximacion}|'.format(
            iteracion = str(x).center(int(tamanio/2)),
            aproximacion = str(aproximaciones[x]).center(int(tamanio/2))
        ))
        print('-'*(tamanio+2)) 


if __name__ == "__main__":
    bienvenida()
    polinomio,xo,precision = solicitar()
    variable = re.findall(r"[a-z]",polinomio)[0]
    a_separar = tratamiento(polinomio)
    #['-5x^3', '3x^2', '2x', '1']
    a_derivar = separar(a_separar)
    derivada,derivadaL = derivar(a_derivar,variable)
    aproximaciones,encontrada = iteracion(a_derivar,derivadaL,xo,precision)
    imprimir(polinomio,aproximaciones,encontrada)



    
    