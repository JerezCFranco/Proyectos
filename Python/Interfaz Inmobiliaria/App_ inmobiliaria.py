def estadoValido(estado1):
    if (estado1=="disponible" or estado1=="reservado" or estado1=="vendido"):
       return estado1

def tieneGaraje(opcional):
    if(opcional=="Si" or opcional=="Sí" or opcional=="SÍ" or opcional=="sÍ" or opcional=="si" or opcional=="sí" or opcional=="SI"):
        garaje.append("True")
    else:
        garaje.append("False")

def zonaValida(laZona):
    if (laZona == "A" or laZona == "B" or laZona == "C"):
        return True
    else:
        return False
        
def verPlantilla(menuprincipal):
        print("Posicion | Año | Metros | Habitaciones| Garaje |  Zona  |  Estado ")
        for x in range(len(año)):
            print("   ",posicion[x],"   ",año[x],"  ",metro[x],"        ",habitaciones[x],"       ",garaje[x],"    ",zona[x],"      ",estado[x])

def insertarInmueble(menuprincipal):
    print("Llena los siguientes datos: ")
    posicion.append(input("Ingrese la posicion numerica del inmueble: "))
    añoint = int(input("Año del inmueble: "))
    if añoint>1999:
        añoint=str(añoint)
        año.append(añoint)
        metroint = int(input("Metros cuadrados del inmueble: "))
        if metroint>59:
            metroint=str(metroint)
            metro.append(metroint)
            habitacioneint = int(input("Cantidad de habitaciones del inmueble: "))
            if habitacioneint>1:
                habitacioneint=str(habitacioneint)
                habitaciones.append(habitacioneint)
                opcional = input("Tiene garaje?: ")
                tieneGaraje(opcional)
                laZona= input("Ingrese la zona a la que pertenece el inmueble: ")
                if (zonaValida(laZona)==True):
                    zona.append(laZona)
                    estadostr = input("Ingrese el estado del inmueble(Disponible,Reservado o Vendido): ")
                    estadostr = estadostr.lower()
                    if (estadoValido(estadostr)=="disponible" or estadoValido(estadostr)=="reservado" or estadoValido(estadostr)=="vendido"):
                        estado.append(estadostr)
                    else:
                        print("Estado del inmueble invalido.\n")
                else:
                    print("Se opera solo con inmuebles de zona A, B o C.\n")
                
            else:
                print("No opera con inmuebles menores a 2 habitaciones.\n")
            
        else:
            print("No opera con inmuebles menores a 60 metros cuadrados.\n")
    else:
         print("No opera con inmuebles anteriores al año 2000.\n")
    

def eliminarInmueble(menuprincipal):
    print("Eliminando inmueble")
    cod = input("Ingresa la posicion del inmueble a eliminar: ")
    for i in range(len(posicion)-1,-1,-1):
            if posicion[i] == cod:
                posicion.pop(i)
                año.pop(i)
                metro.pop(i)
                garaje.pop(i) 
                habitaciones.pop(i)
                zona.pop(i)
                estado.pop(i)
    print("Inmueble eliminado.")

def modificarInmueble(menuprincipal):
    print("Modificando inmueble")
    cod = input("Ingresa la posicion del inmueble a modificar: ")
    for x in range(len(posicion)):
            if posicion[x] == cod:
                nuevoaño=int(input("Ingrese el año del inmueble: "))
                if nuevoaño>1999:
                    año[x] = nuevoaño
                    metronuevo=int(input("Ingrese los nuevos metros cuadrados del inmueble: "))
                    if metronuevo>59:
                        metro[x] = metronuevo
                        habitacionesnuevo = int(input("Ingrese el nuevo número de habitaciones: "))
                        if habitacionesnuevo>1:
                            habitaciones[x] = habitacionesnuevo
                            opcional = input("Tiene garaje?: ")
                            if (tieneGaraje(opcional) == "true"):
                                garaje[x] = "True"
                                zonanuevo = input("Ingrese la nueva zona del inmueble: ")
                                if (zonaValida(zonanuevo)==True):
                                    zona[x] = zonanuevo
                                    estadonuevo = input("Ingrese el nuevo estado del inmueble(Disponible, Reservado o Vendido): ")
                                    estadonuevo = estadonuevo.lower()
                                    if (estadoValido(estadonuevo)=="disponible" or estadoValido(estadonuevo)=="reservado" or estadoValido(estadonuevo)=="vendido"):
                                        estado[x] = estadonuevo
                                    else:
                                        print("Estado del inmueble invalido.\n")
                                else:
                                    print("Se opera solo con inmuebles de zona A, B o C.")
                            else:
                                garaje[x] = "False"
                                zonanuevo = input("Ingrese la nueva zona del inmueble: ")
                                if (zonaValida(zonanuevo)==True):
                                    zona[x] = zonanuevo
                                    estadonuevo = input("Ingrese el nuevo estado del inmueble(Disponible, Reservado o Vendido): ")
                                    estadonuevo = estadonuevo.lower()
                                    if (estadoValido(estadonuevo)=="disponible" or estadoValido(estadonuevo)=="reservado" or estadoValido(estadonuevo)=="vendido"):
                                        estado[x] = estadonuevo
                                    else:
                                        print("Estado del inmueble invalido.\n")
                                else:
                                    print("Se opera solo con inmuebles de zona A, B o C.")
                        else:
                            print("No se opera con inmuebles menores a 2 habitaciones.\n")
                    else:
                        print("No se opera con inmuebles menores a 60 metros cuadrados.\n")
                else:
                    print("No se opera con inmuebles anteriores al año 2000.\n")

    print("Inmueble modificado.")

def calcularPrecioA(precio):
      
    print("Calculando precio del inmueble")
    presupuesto = int(input("Escribir presupuesto: "))
    nuevazona = input("Ingrese la zona del inmueble: ")
    for x in range(len(año)):       
        if(nuevazona==zona[x] and zona[x] == "A"):
            calculogaraje = 0
            antiguedad = 2023 - int(año[x])
            if garaje[x] == "True":
                calculogaraje = 1
                costo= (int(metro[x])*100+int(habitaciones[x])*500+calculogaraje*1500)*(1-antiguedad/100)
                if (costo<presupuesto and estado[x]!="Vendido"):
                    print(f"El costo de este inmueble es de {costo}$.")
                    print(f"Y tu presupuesto es de {presupuesto}$.")
                    print(f"Año: {año[x]}, Metros: {metro[x]}, Habitaciones: {habitaciones[x]}, Garaje: {garaje[x]}, Zona: {zona[x]}, Estado: {estado[x]}\n")
                else:
                    print("El presupuesto es insuficiente para cualquier inmobiliario.")
            else:
                calculogaraje = 0
                costo= (int(metro[x])*100+int(habitaciones[x])*500+calculogaraje*1500)*(1-antiguedad/100)
                if (costo<presupuesto and estado[x]!="Vendido"):
                    print(f"El costo de este inmueble es de {costo}$.")
                    print(f"Y tu presupuesto es de {presupuesto}$.")
                    print(f"Año: {año[x]}, Metros: {metro[x]}, Habitaciones: {habitaciones[x]}, Garaje: {garaje[x]}, Zona: {zona[x]}, Estado: {estado[x]}\n")
                else:
                    print("El presupuesto es insuficiente para cualquier inmobiliario.")
        
        elif(nuevazona==zona[x] and zona[x] == "B"):
            calculogaraje = 0
            antiguedad = 2023 - int(año[x])
            if garaje[x] == "True":
                calculogaraje = 1
                costo = (int(metro[x])*100+int(habitaciones[x])*500+calculogaraje*1500)*(1-antiguedad/100)*1.5
                if (presupuesto>costo and estado[x]!="Vendido"):
                    print(f"El costo de este inmueble es de {costo}$.")
                    print(f"Y tu presupuesto es de {presupuesto}$.")
                    print(f"Año: {año[x]}, Metros: {metro[x]}, Habitaciones: {habitaciones[x]}, Garaje: {garaje[x]}, Zona: {zona[x]}, Estado: {estado[x]}\n")
                else:
                    print("El presupuesto es insuficiente para cualquier inmobiliario.")
            else:
                calculogaraje = 0
                costo = (int(metro[x])*100+int(habitaciones[x])*500+calculogaraje*1500)*(1-antiguedad/100)*1.5
                if (presupuesto>costo and estado[x]!="Vendido"):
                    print(f"El costo de este inmueble es de {costo}$.")
                    print(f"Y tu presupuesto es de {presupuesto}$.")
                    print(f"Año: {año[x]}, Metros: {metro[x]}, Habitaciones: {habitaciones[x]}, Garaje: {garaje[x]}, Zona: {zona[x]}, Estado: {estado[x]}\n")
                else:
                    print("El presupuesto es insuficiente para cualquier inmobiliario.")
        elif(nuevazona==zona[x] and zona[x] == "C"):
            calculogaraje = 0
            antiguedad = 2023 - int(año[x])
            if garaje[x] == "True":
                calculogaraje = 1
                costo = (int(metro[x])*100+int(habitaciones[x])*500+calculogaraje*1500)*(1-antiguedad/100)*2
                if (presupuesto>costo and estado[x]!="Vendido"):
                    print(f"El costo de este inmueble es de {costo}$.")
                    print(f"Y tu presupuesto es de {presupuesto}$.")
                    print(f"Año: {año[x]}, Metros: {metro[x]}, Habitaciones: {habitaciones[x]}, Garaje: {garaje[x]}, Zona: {zona[x]}, Estado: {estado[x]}\n")
                else:
                    print("El presupuesto es insuficiente para cualquier inmobiliario o el inmobiliario esta vendido.")
            else:
                calculogaraje = 0
                costo = (int(metro[x])*100+int(habitaciones[x])*500+calculogaraje*1500)*(1-antiguedad/100)*2
                if (presupuesto>costo and estado[x]!="Vendido"):
                    print(f"El costo de este inmueble es de {costo}$.")
                    print(f"Y tu presupuesto es de {presupuesto}$.")
                    print(f"Año: {año[x]}, Metros: {metro[x]}, Habitaciones: {habitaciones[x]}, Garaje: {garaje[x]}, Zona: {zona[x]}, Estado: {estado[x]}\n")
                else:
                    print("El presupuesto es insuficiente para cualquier inmobiliario o el inmobiliario esta vendido.")
    if(nuevazona!="A" and nuevazona!="B" and nuevazona!="C"):
        print("No se opera con inmobiliarios de esa zona.\n")


posicion=["1","2","3","4"]
añoint= 0
año = ["2020","2005","2001","2014"]
metroint = 0
metro = ["50","100","70","90"]
habitacioneint = 0
habitaciones = ["5","3","7","5"]
garaje = ["True","False","True","True"]
laZona = "A"
zona = ["B","A","B","C"]
estado = ["reservado","disponible","disponible","Vendido"]
precio = 0
costo = 0
calculogaraje = 0


menuprincipal = int(input("Menú Principal: \n 1- Ver lista \n 2- Insertar inmueble \n 3- Eliminar inmueble \n 4- Modificar inmueble \n 5- Lista según presupuesto \n 0- Salir \n"))
while menuprincipal !=0:
    if menuprincipal == 1:
        verPlantilla(menuprincipal)
    
    elif menuprincipal == 2:
        insertarInmueble(menuprincipal)
    elif menuprincipal == 3:
        eliminarInmueble(menuprincipal)
    elif menuprincipal == 4:
        modificarInmueble(menuprincipal)
    elif menuprincipal == 5:
        calcularPrecioA(menuprincipal)
    else:
        print("Por favor digite una opcion correcta.")
    
    menuprincipal = int(input("Menú Principal: \n 1- Ver lista \n 2- Insertar inmueble \n 3- Eliminar inmueble \n 4- Modificar inmueble \n 5- Lista según presupuesto \n 0- Salir \n"))
print("El programa a finalizado.")
