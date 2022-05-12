


datosx = []
X = input("ingrese valores para X y presione y para añadir valores en Y: ")
while X != "y":
     datosx.append(X)
     X = input("ingrese valores para X y presione y para añadir valores en Y: ")
datosx = list(map(int, datosx))
datosy = []
Y = input("ingrese valores para Y y presione -fin- para terminar: ")
while Y != "fin":
     datosy.append(Y)
     Y = input("ingrese valores para Y y presione -fin- para terminar: ")
datosy = list(map(int, datosy))
largo =(len(datosy)-2)

lista1 = 0
while lista1 < 1:
    lista1 = lista1 +1
    

    lista2 = 0
    lista3 = 1
    lista4 = 2
    while lista3 <=(len(datosy)-3):
        suma_y = int(int(datosy[lista3]) -int(datosy[lista2]))
        prueba = int(int(datosy[lista4]) - int(datosy[lista3]))
        lista2 = int(lista2 +1)
        lista3 = int(lista2 +1)
        lista4 = int(lista4+1)
        
      
    if suma_y == prueba:
            print("La serie de datos dada se ajusta mejor a una regresión lineal")
            def sumar(datosx):
                #se define una funcion para hacer una sumatoria de los elementos de una lista.
                suma = 0
                for elemento in datosx:
                    suma += int(elemento)
                return suma
                # total x , y
            totalx = sumar(datosx)
            totaly =sumar(datosy)
        
            product =list([x*y for x,y in zip(datosx, datosy)])
            

            # se crea una variable que multiplique las dos listas x, y, y sea una lista

            totalxy = sumar(product)

            #indicacion de los datos de ajuste

            print('sumatoria valores x: ', totalx)
            print('sumatoria valores y: ', totaly)
            print('sumatoria valores xy: ', totalxy)


            def potenciacion(datosx):
                # se define una funcion que potencie en grado 2 todos los elementos de uan lista y retorne una lista
                return list(n**2 for n in datosx)
            potencia =potenciacion(datosx)
        
            totalpotencia = sumar(potencia)
            print('La sumatoria de los datos de x al cuadrado es: ', totalpotencia)
            
            #se realizan los valores de ajuste
            #pendiente
            m = ((len(datosx)*totalxy) - (totalx*totaly))/((len(datosx)*totalpotencia)-totalx**2)
            print('La pendiente de crecimiento que tienen los valores es:', m)
            
            #hayando la ordenada
            b = ((totaly/len(datosy))-(m*(totalx/len(datosx))))
            print ("La ordenada de los datos dados es: ", b)
            print('la ecuacion de la recta de la regresion lineal es: Y=',m,'X',b)






            
    else:
        print("se ajustan los valores a una regresion logaritmica")
        def sumar(datosx):
            #se define una funcion para hacer una sumatoria de los elementos de una lista.
                suma = 0
                for elemento in datosx:
                    suma += int(elemento)
                return suma
                #totales x , y
        totalx = sumar(datosx)
        totaly =sumar(datosy)
        
        #logaritmo natural de los valores en x
        import math as ma

        def logaritmo(datosx):
            # se define una funcion que claculo el ln de los datos y retorne una lista con ellos
   
            return list(ma.log(n) for n in datosx)
        ln_x = logaritmo(datosx)
        

        #total ln para x

        totalln_x = sumar(ln_x)
        print('Sumatoria de los ln de los valores de x: ', totalln_x)

        # se crea una variable que multiplique las dos listas x, y, y sea una lista


        product =list([x*y for x,y in zip(ln_x, datosy)])
        

        # sumatoria del producto

        totalxy = sumar(product)

        #indicacion de los datos de ajuste

        print('sumatoria valores x: ', totalx)
        print('sumatoria valores y: ', totaly)
        print('sumatoria valores xy: ', totalxy)
        def potenciacion(ln_x):
            # se define una funcion que potencie en grado 2 todos los elementos de uan lista y retorne una lista
                return list(n**2 for n in ln_x)


        potencia =potenciacion(datosx)
        
        totalpotencia = sumar(potencia)
        print('La sumatoria de los datos ln x elevandos al cuadrado es: ',totalpotencia)
            
            #se realizan los valores de ajuste
            #pendiente
        m = ((len(datosx)*totalxy) - (totalln_x*totaly))/((len(datosx)*totalpotencia)-totalx**2)
        print('La pendiente de crecimiento que tienen los valores es:', m)
            
            #hayando la ordenada
        b = ((totaly/len(datosy))-(m*(totalln_x/len(datosx))))
        print ("La ordenada de los datos dados es: ", b)
        print('la ecuacion de la recta de la regresion lineal es: Y=',m,b,'ln X')
        
        break

        
