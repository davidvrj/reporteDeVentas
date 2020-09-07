"""
Created on Fri Aug 28 16:39:15 2020

@author: DavidRojas
"""

#<---------------->INICIO CÓDIGO<------------------>

import os #Importamos esta libreria para algunas funciones de visualización del programa
from time import sleep #Importamos esta libreria para hacer pausas de transición de pantallas
import lifestoreFile as datos #Importamos las listas del archivo lifeStoreFile
import sys
os.system("clear")
def caratula():
      print("\t\t\t######################################")
      print("\t\t #Bienvenido al programa de lifeStore#")
      print("\t\t #####################################")
#---------Validación de usuario--------------

#Usaremos el ciclo while para condicionar el usuario y contraseña hasta coincidir los valores para el ingreso.
aux = 0 #usaremos esta variable auxiliar para guardar posiciones
aux2 = 4 #usaremos este auxiliar para contar el numero de intentos para ingresar al sistema

while aux2 > 0:# mientras los intentos de ingreso no se agoten, se repetirá el proceso de ingreso
    aux2 -=1 #quitamos un intento de ingreso
    caratula()
    #mprimimos una bienvenida al programa con la función print
    user = input('\nIngrese usuario:') #Pedimos al usuario el usuario
    pswd = input('Ingrese contraseña:') #Pedimos al usuario la contraseña
    if user in datos.users_name:
        aux = datos.users_name.index(user) #Si el nombre del usuario existe, guardaermos la posición para verificar que coincida las contraseña y si es admin.
        if pswd == datos.passwd[aux] and datos.esAdmin[aux]==0: #comparamos si los indices de las demas listas coinciden con su respectivo usuario como lo es la contraseña y si es Admin
            print("\nBienvenido administrador ",user) #si existe y es administrador, le damos la bienvenida al administrador
            aux2=-1
        elif pswd == datos.passwd[aux] and datos.esAdmin[aux]==1:
            print("\nBienvenido usuario ",user)# otra posibilidad es si existe y es usuario, al mismo tiempo le damos la bienvenida
            aux2=-1
        else: # si no coinciden la contraseña, tendremos que pedir de nuevo al usuario que ingrese el usuario y contraseña
            print("\nContraseña incorrecta, intente de nuevo")
            print("\nNumero de intentos restantes: ",aux2)
            sleep(4) # hacemos una pausa para que lea los mensajes
            os.system("clear") # limpiamos pantalla y haremos de nuevo el ingreso
    else:
        print("\nUsuario no encontrado, intente de nuevo")
        print("\nNumero de intentos restantes: ",aux2) 
        sleep(4)
        os.system("clear")#limpiamos pantalla y de nuevo reiniciamos el proceso de ingreso de usuario
       
   

#Si el usuario agotó el número de intentos, entonces procederemos a salir del programa para aumentar la seguridad.
if aux2 == 0:
    print("\nNumero de intentos excedidos, cerrando sistema...")
    sleep(1)
    sys.exit()
   
#---------Fin validación de usuario.----------
    
    

#--------------Menú principal-----------------
    
    
sleep(3) #Esperamos 3 segundos para darle la bienvenida al usuario
#Variables para llevar el control del menu del usuario
opc=''
opc2=''
opc3=''
opc4=''
opc5=''
salir = False

while not opc == '4': # control del menú principal
    os.system('clear') #limpiamos pantalla
    caratula() #imprimos portada
    #Imprimos las opción del menú principal
    print("\nOpciones de reportes:")
    print("""\n\n
    1)Productos más vendidos y productos rezagados
    2)Productos por reseñas en el servicio
    3)Total de ingresos y ventas promedio mensuales, total anual y meses con más ventas al año
    4)Salir sistema      """)
    
    #Leer 
    opc = input('Ingrese una opción:')#Leemos la opción del usuario para ingresar a los submenus
    #<------------->Submenú de la opción 1<------------->
    if opc == '1':#Daremos inicio al submenú 1 donde se encontrarán las opciones de la consignia 1
        while not opc2 == '8':
            os.system('clear')
            print("""
            1)Lista 30 productos con mayores ventas
            2)Lista 40 productos con mayores búsquedas
            3)Lista 30 productos menores ventas
            4)Lista 40 productos con menores búsquedas
            5)Lista categorias por número de búsquedas
            6)Lista categorias por número de ventas
            7)Lista productos sin ventas
            8)Salir
            \n\n""")
            opc2 = input("Ingrese una opción:")#Leemos la opción para desplegar los ejercicios de las consignias
            #<---------->Opción 1-1<----------->
            if opc2=='1': #Consignia lista 30 productos con mayores ventas
                os.system("clear")
                print("\t\t\t#################################")
                print("\t\t #LISTA 30 PRODUCTOS MAS VENDIDOS#")
                print("\t\t #################################")
                aux=1 #igualamos el auxiliar a 1 para llevar un contador
                listaAux=[]#Ocuparemos esta lista para vaciar el ID de los productos de las ventas y contarlas
                for dato in datos.lifestore_sales:
                    listaAux.append(dato[1])#hacemos la iteración para vaciar los id de los productos vendidos
                lista = [[x,listaAux.count(x)] for x in set(listaAux)]#creamos una lista de listas con el id del producto y el numero de ventas respectivamente
                for i in lista:#en este proceso, igualaremos si los indices de los productos en la lista que creamos son iguales al id de la lista de productos
                    for j in datos.lifestore_products:
                        if i[0] == j[0]:# Si son iguales, añadiremos el nombre del producto a nuestra lista de listas para conformar una lista de [id_producto, numero de ventas, nombre de producto]
                            i.append(j[1])
                lista = sorted(lista, key=lambda x : x[1] ,reverse=True)#Ordenamos nuestra lista dando como parametro que sea ordenada por el numero de ventas, es decir, de mayor a menor. 
                for i in lista:
                    if aux<=30:
                        print("\n",aux,".-",i[2]," con ",i[1],"número de ventas")
                        aux+=1
                    else:
                        break;              
                decision =input("\n\nPresione enter para salir...")
                if decision=="":
                    break;
            
            #<---------->Opción 1-2<----------->
            if opc2== '2':
                os.system("clear")
                print("\t\t\t#################################")
                print("\t\t #LISTA 40 PRODUCTOS MAS BUSCADOS#")
                print("\t\t #################################")
                aux=1 #igualamos el auxiliar a 1 para llevar un contador
                listaAux=[]#Ocuparemos esta lista para vaciar el ID de los productos de las ventas y contarlas
                for dato in datos.lifestore_searches:
                    listaAux.append(dato[1])#hacemos la iteración para vaciar los id de los productos vendidos
                lista = [[x,listaAux.count(x)] for x in set(listaAux)]#creamos una lista de listas con el id del producto y el numero de ventas respectivamente
                for i in lista:#en este proceso, igualaremos si los indices de los productos en la lista que creamos son iguales al id de la lista de productos
                    for j in datos.lifestore_products:
                        if i[0] == j[0]:# Si son iguales, añadiremos el nombre del producto a nuestra lista de listas para conformar una lista de [id_producto, numero de ventas, nombre de producto]
                            i.append(j[1])
                lista = sorted(lista, key=lambda x : x[1] ,reverse=True)#Ordenamos nuestra lista dando como parametro que sea ordenada por el numero de ventas, es decir, de mayor a menor. 
                for i in lista:
                    if aux<=40:
                        print("\n",aux,".-",i[2]," con ",i[1],"número de busquedas")
                        aux+=1
                    else:
                        break;             
                decision =input("\n\nPresione enter para salir...")
                if decision=="":
                    break;
            
            #<---------->Opción 1-3<----------->
            if opc2== '3':
                os.system("clear")
                print("\t\t\t###################################")
                print("\t\t #LISTA 30 PRODUCTOS MENOS VENDIDOS#")
                print("\t\ ##t#################################")
                aux=1 #igualamos el auxiliar a 1 para llevar un contador
                listaAux=[]#Ocuparemos esta lista para vaciar el ID de los productos de las ventas y contarlas
                for dato in datos.lifestore_sales:
                    listaAux.append(dato[1])#hacemos la iteración para vaciar los id de los productos vendidos
                lista = [[x,listaAux.count(x)] for x in set(listaAux)]#creamos una lista de listas con el id del producto y el numero de ventas respectivamente
                for i in lista:#en este proceso, igualaremos si los indices de los productos en la lista que creamos son iguales al id de la lista de productos
                    for j in datos.lifestore_products:
                        if i[0] == j[0]:# Si son iguales, añadiremos el nombre del producto a nuestra lista de listas para conformar una lista de [id_producto, numero de ventas, nombre de producto]
                            i.append(j[1])
                lista = sorted(lista, key=lambda x : x[1])#Ordenamos nuestra lista dando como parametro que sea ordenada por el numero de ventas, es decir, de mayor a menor. 
                for i in lista:
                    if aux<=30:
                        print("\n",aux,".-",i[2]," con ",i[1],"número de ventas")
                        aux+=1
                    else:
                        break;              
                decision =input("\n\nPresione enter para salir...")
                if decision=="":
                    break;
            #<---------->Opción 1-4<----------->
            if opc2== '4':
                os.system("clear")
                print("\t\t\t###################################")
                print("\t\t #LISTA 40 PRODUCTOS MENOS BUSCADOS#")
                print("\t\t ###################################")
                aux=1 #igualamos el auxiliar a 1 para llevar un contador
                listaAux=[]#Ocuparemos esta lista para vaciar el ID de los productos de las ventas y contarlas
                for dato in datos.lifestore_searches:
                    listaAux.append(dato[1])#hacemos la iteración para vaciar los id de los productos vendidos
                lista = [[x,listaAux.count(x)] for x in set(listaAux)]#creamos una lista de listas con el id del producto y el numero de ventas respectivamente
                for i in lista:#en este proceso, igualaremos si los indices de los productos en la lista que creamos son iguales al id de la lista de productos
                    for j in datos.lifestore_products:
                        if i[0] == j[0]:# Si son iguales, añadiremos el nombre del producto a nuestra lista de listas para conformar una lista de [id_producto, numero de ventas, nombre de producto]
                            i.append(j[1])
                lista = sorted(lista, key=lambda x : x[1])#Ordenamos nuestra lista dando como parametro que sea ordenada por el numero de ventas, es decir, de menor a menor. 
                for i in lista:
                    if aux<=40:
                        print("\n",aux,".-",i[2]," con ",i[1],"número de busquedas")
                        aux+=1
                    else:
                        break;              
                decision =input("\n\nPresione enter para salir...")
                if decision=="":
                    break;
                os.system("clear")
            #<------------>Opción 1-5<------------>
                
            if opc2=='5':
               os.system("clear")
               listaAux=[] #Lista auxiliar
               for i in datos.lifestore_products:
                   listaAux.append(i[3]) #Creamos una lista para vaciar todas las categorias de los productos
               lista2 = [[x,listaAux.count(x)] for x in set(listaAux)] #contabilizamos cuantos productos hay por cada categoria,para ello, creamos una lista [categoria,no.de productos]
               aux=0#auxiliar para agregar un tercer elemento a la listas de lista2
               for i in lista2:
                   i.append(0)#agregamos a cada lista de categorias un elemento más 0 que ocuparemos para contabilizar las busquedas
               listaAux=[]#lista auxiliar
               for dato in datos.lifestore_searches:
                   listaAux.append(dato[1])#hacemos la iteración para vaciar los id de los productos buscados
               lista = [[x,listaAux.count(x)] for x in set(listaAux)]#creamos una lista de listas con el id del producto y el numero de busquedas respectivamente
               for i in lista:#en este proceso, igualaremos si los indices de los productos en la lista que creamos son iguales al id de la lista de productos
                   for j in datos.lifestore_products:
                       if i[0] == j[0]:# Si son iguales, añadiremos el nombre del producto a nuestra lista y su categoria
                           i.append(j[1])
                           i.append(j[3])
               lista = sorted(lista, key=lambda x : x[1] ,reverse=True)#Ordenamos nuestra lista dando como parametro que sea ordenada por el numero de ventas, es decir, de mayor a menor. 

               for i in lista2:#Ocuparemos este ciclo para verificar si el elemento de categoria son iguales
                   for j in lista:
                       if i[0]==j[3]:#si las categorias son iguales, añadiremos el apartado de busquedas que tuvo el producto para contabilizarlos
                           i[2]+=j[1]#en cada categorias, se sumara las busqueda que tuvo si perteneció a esta categoria
               aux=0
               lista2 = sorted(lista2, key=lambda x : x[2] ,reverse=True)#ordenamos las categorias por numero de búsquedas de mayor a menor
               for i in lista2:
                   aux+=1
                   print(aux,".- ",i[0]," con  " ,i[2]," numero de búsquedas")  
               decision =input("\n\nPresione enter para salir...")
               if decision=="":  break;
               os.system("clear") 
             #<------------>Opción 1-6<------------>   
            if opc2=='6':
               os.system("clear")
               listaAux=[] #Lista auxiliar
               for i in datos.lifestore_products:
                   listaAux.append(i[3]) #Creamos una lista para vaciar todas las categorias de los productos
               lista2 = [[x,listaAux.count(x)] for x in set(listaAux)] #contabilizamos cuantos productos hay por cada categoria,para ello, creamos una lista [categoria,no.de productos]
               aux=0#auxiliar para agregar un tercer elemento a la listas de lista2
               for i in lista2:
                   i.append(0)#agregamos a cada lista de categorias un elemento más 0 que ocuparemos para contabilizar las ventas
               listaAux=[]#lista auxiliar
               for dato in datos.lifestore_sales:
                   listaAux.append(dato[1])#hacemos la iteración para vaciar los id de los productos bvendidos
               lista = [[x,listaAux.count(x)] for x in set(listaAux)]#creamos una lista de listas con el id del producto y el numero de ventas respectivamente
               for i in lista:#en este proceso, igualaremos si los indices de los productos en la lista que creamos son iguales al id de la lista de productos
                   for j in datos.lifestore_products:
                       if i[0] == j[0]:# Si son iguales, añadiremos el nombre del producto a nuestra lista y su categoria
                           i.append(j[1])
                           i.append(j[3])
               lista = sorted(lista, key=lambda x : x[1] ,reverse=True)#Ordenamos nuestra lista dando como parametro que sea ordenada por el numero de ventas, es decir, de mayor a menor. 

               for i in lista2:#Ocuparemos este ciclo para verificar si el elemento de categoria son iguales
                   for j in lista:
                       if i[0]==j[3]:#si las categorias son iguales, añadiremos el apartado de ventas que tuvo el producto para contabilizarlos
                           i[2]+=j[1]#en cada categorias, se sumara las ventas que tuvo si perteneció a esta categoria
               aux=0
               lista2 = sorted(lista2, key=lambda x : x[2] ,reverse=True)#ordenamos las categorias por numero de ventas de mayor a menor
               for i in lista2:
                   aux+=1
                   print(aux,".- ",i[0]," con  " ,i[2]," numero de ventas")  
               decision =input("\n\nPresione enter para salir...")
               if decision=="":  break;
               os.system("clear") 
             #<------------>Opción 1-7<------------>   
            if opc2=='7':
                os.system("clear")
                aux=1 #igualamos el auxiliar a 1 para llevar un contador
                listaAux=[]#Ocuparemos esta lista para vaciar el ID de los productos de las ventas y contarlas
                for dato in datos.lifestore_sales:
                    listaAux.append(dato[1])#hacemos la iteración para vaciar los id de los productos vendidos
                lista = [[x,listaAux.count(x)] for x in set(listaAux)]#creamos una lista de listas con el id del producto y el numero de ventas respectivamente
                listaAux=[]#Lista auxiliar
                listaAux2=[]#lista auxiliar
                for i in lista:
                    listaAux.append(i[0])#ingresamos el id que han tenido ventas en listaAux
                for i in datos.lifestore_products:
                    listaAux2.append(i[0])# ingresamos el id de todos los productos

                rezagados= list(set(listaAux2) - set(listaAux))#obtenemos los productos que no tengan ventas
                listaAux=[]
                listaAux2=[]
                #Usaremos este ciclo para crear una lista de listas de los productos sin ventas, que llevarán el siguiente comportamiento: [id,nombre del producto]
                for i in rezagados:
                    for j in datos.lifestore_products:
                        if i ==j[0]:
                            listaAux=[]#lista auxiliar para añadir a la lista de productos sin ventas
                            listaAux.append(i)#agregamos  el id del producto a la lista auxiliar
                            listaAux.append(j[1])#agregamos el nombre del producto a la lista auxiliar
                            listaAux2.append(listaAux)   #agregamos la listaAuxiliar a la lista de productos sin ventas 
                aux=0 #Auxiliar para llevar el contador           
                for i in listaAux2:
                    aux+=1#sumamos 1 al contador
                    print("",aux,".- ",i[1]) #desplegamos la lista de productos sin ventas
                decision =input("\n\nPresione enter para salir...")
                if decision=="":  break;
                os.system("clear")     

     #<------------->Submenú de la opción 2<------------->           
    if opc == '2':        
        while not opc3 == '3':
            os.system("clear")
            print("""
            1)Lista 20 productos mejores valorados.
            2)Lista 20 productos menores valorados.
            3)Salir
            \n\n""")
            opc3 = input("Ingrese una opcion:")
                 #<---------->Opción 2-1<----------->
            if opc3 == '1':
                print("\t\t\t#####################################")
                print("\t\t #LISTA 20 PRODUCTOS MEJORES VALORADOS#")
                print("\t\t #######################################")
                os.system("clear")
                listaAux=[]#Lista auxiliar para formar la lista con los elementos que deseamos
                for dato in datos.lifestore_sales:
                    listaAux.append(dato[1])#Ingresamos los ID de los productos para contabilizar cuantas ventas obtuvieron
                lista = [[x,listaAux.count(x)] for x in set(listaAux)]#Creamos la lista de listas que estara conformado como [ID_producto,Numero de ventas]
                for i in lista:
                    i.append(0)   #Crearemos un tercer elemento para contabilizar los ratings en total por cada producto
                for i in lista: #Usaremos este ciclo para contabilizar las valoraciones
                    for j in datos.lifestore_sales:
                        if i[0] == j[1]:#Si los  ID de los productos coinciden, entoces:
                            if j[4]==0:#Si el producto no fue devuelto:
                                i[2]+=j[2]#Sumaremos la valoración  a las valoraciones totales
                            else:#Si no fue vendido
                                i[2]+=0     #No contabilizaremos la valoración, puesto que fue devuelto     
                for i in lista: #Crearemos este ciclo para añadir las valoraciones promedio a nuestra lista principal
                    aux=i[2]/i[1]#Guardamos el promedio en un auxiliar
                    i.append(aux)#Y lo añadimos a la lista
                lista = sorted(lista, key=lambda x : x[3] ,reverse=True) #Ordenamos nuestra lista de mayor valoracion promedio a menor
                for i in lista:#Con este ciclo, añadiremos el nombre de los productos
                    for j in datos.lifestore_products:
                        if i[0] == j[0]:#Si los IDs de los productos coincide, entonces:
                            i.append(j[1])#Añadiremos el nombre del producto a nuestra lista
                aux=0#Usaremos este auxiliar para llevar el control del top 20
                for i in lista:
                    aux+=1#Sumaremos por cada iteracion un 1
                    if aux<=20:
                        print(aux,".-",i[4]," con una valoración promedio de: ",i[3],"y con numero de ventas de ",i[1]," en total." )#Imprimimos los enunciados
                    else:
                        break;#Cuando se cumplan los 20, salimos de la iteracion
                decision =input("\n\nPresione enter para salir...")
                if decision=="":
                    break;             
                 #<---------->Opción 2-2<----------->
            if opc3 == '2':
                os.system("clear")
                print("\t\t\t#####################################")
                print("\t\t #LISTA 20 PRODUCTOS MENORES VALORADOS#")
                print("\t\t #######################################")      
                listaAux=[]#Lista auxiliar para formar la lista con los elementos que deseamos
                for dato in datos.lifestore_sales:
                    listaAux.append(dato[1])#Ingresamos los ID de los productos para contabilizar cuantas ventas obtuvieron
                lista = [[x,listaAux.count(x)] for x in set(listaAux)]#Creamos la lista de listas que estara conformado como [ID_producto,Numero de ventas]
                for i in lista:
                    i.append(0)   #Crearemos un tercer elemento para contabilizar los ratings en total por cada producto
                for i in lista: #Usaremos este ciclo para contabilizar las valoraciones
                    for j in datos.lifestore_sales:
                        if i[0] == j[1]:#Si los  ID de los productos coinciden, entoces:
                            if j[4]==0:#Si el producto no fue devuelto:
                                i[2]+=j[2]#Sumaremos la valoración  a las valoraciones totales
                            else:#Si no fue vendido
                                i[2]+=0     #No contabilizaremos la valoración, puesto que fue devuelto     
                for i in lista: #Crearemos este ciclo para añadir las valoraciones promedio a nuestra lista principal
                    aux=i[2]/i[1]#Guardamos el promedio en un auxiliar
                    i.append(aux)#Y lo añadimos a la lista
                lista = sorted(lista, key=lambda x : x[3] ) #Ordenamos nuestra lista de menor valoracion promedio a mayor
                for i in lista:#Con este ciclo, añadiremos el nombre de los productos
                    for j in datos.lifestore_products:
                        if i[0] == j[0]:#Si los IDs de los productos coincide, entonces:
                            i.append(j[1])#Añadiremos el nombre del producto a nuestra lista
                aux=0#Usaremos este auxiliar para llevar el control del top 20
                for i in lista:
                    aux+=1#Sumaremos por cada iteracion un 1
                    if aux<=20:
                        print(aux,".-",i[4]," con una valoración promedio de: ",i[3],"y con numero de ventas de ",i[1]," en total." )#Imprimimos los enunciados
                    else:
                        break;#Cuando se cumplan los 20, salimos de la iteracion
                decision =input("\n\nPresione enter para salir...")
                if decision=="":
                    break;      
        

             
    #<------------->Submenú de la opción 3<------------->
    if opc == '3':        
       while not opc4 == '5':
           os.system("clear")
           print("""
           1)Total ingresos 
           2)Ventas promedio mensuales
           3)Total anual
           4)Meses con mas ventas al año
           5)Salir
           \n\n""")
           opc4 = input("Ingrese una opcion:")
           #<---------->Opción 3-1<----------->
           if opc4 == '1':
               os.system("clear")
               listaAux=[]#lista auxiliar
               for dato in datos.lifestore_sales:
                   listaAux.append(dato[1])#Añadimos los ID de los productos a una lista nueva
               lista = [[x,listaAux.count(x)] for x in set(listaAux)]#Contabilizamos las ventas por cada producto
               suma = 0 #Auxiliar para la suma de ventas           
               for i in lista:
                   for j in datos.lifestore_products:
                       if i[0] == j[0]:#Si los ID de los productos coinciden
                           i.append(j[2]*i[1])#Sumaremos el nuemero de ventas por el precio de los productos
                           suma+=j[2]*i[1]#Al mismo tiempo, la suma en total de ventas
            
               print("\n\n\t Total de ventas hasta el momento: $",suma)#Imprimimos el enunciado
               decision =input("\n\nPresione enter para salir...")
               if decision=="":
                   break;
           #<---------->Opción 3-2<----------->
           if opc4 == '2':
               print("\t\t\t#####################################")
               print("\t\t #      VENTAS PROMEDIO MENSUALES      #")
               print("\t\t #######################################")      
               os.system("clear")
               listaAux=[]#lista auxilia3 1
               listaAux2=[]#lista auxiliar 2
               for i in datos.lifestore_sales:
                   listaAux.append([i[3]])#vaciaremos en la lista aux, las fechas para un mejor control
               for i in listaAux: 
                   i.append(i[0][3:5])#vaciaremos en la misma lista, las fechas tomando unicamente los meses
               lista = sorted(listaAux, key=lambda x : x[1])#ordenamos las fechas por mes
               for i in lista:
                   listaAux2.append(i[1])#vaciaremos en esta lista solo los meses ordenados
               lista2 = [[x,listaAux2.count(x)] for x in set(listaAux2)] #Contaremos cuantas ventas hubo por cada mes formando una lista como a continuación: [mes,cantidad vendidos] 
               lista2 = sorted(lista2, key=lambda x : x[0])  #Ordenaremos la lista por mes
               suma=0    #variable auxiliar para la suma
               for i in lista2:   
                   suma+=i[1]#sumaremos las ventas de cada mes
               total=suma/len(lista2)  #dividiremos las ventas entre el total de numero de meses que se vendieron
               print("\n\n\nEl promedio de numero de ventas por mes es: ",total) 
               decision =input("\n\nPresione enter para salir...")
               if decision=="":
                   break;
               os.system("clear")
           
          
           #<---------->Opción 3-3<----------->
           if opc4 == '3':
               print("\t\t\t#####################################")
               print("\t\t #         VENTAS TOTAL AL AÑO        #")
               print("\t\t #######################################")      
               os.system("clear")
               listaAux=[]#lista auxiliar1
               listaAux2=[]#lista auxuliar2
               for i in datos.lifestore_sales:
                   listaAux.append([i[3]])#vaciaremos en la lista aux, las fechas para un mejor control
               for i in listaAux: 
                   i.append(i[0][3:5])#vaciaremos en la misma lista, las fechas tomando unicamente los meses
               lista = sorted(listaAux, key=lambda x : x[1])#ordenamos las fechas por mes
               for i in lista:
                   listaAux2.append(i[1])#vaciaremos en esta lista solo los meses ordenados
               lista2 = [[x,listaAux2.count(x)] for x in set(listaAux2)] #Contaremos cuantas ventas hubo por cada mes formando una lista como a continuación: [mes,cantidad vendidos] 
               lista2 = sorted(lista2, key=lambda x : x[0])  #Ordenaremos la lista por mes
               suma=0    #variable auxiliar para la suma
               for i in lista2:   
                   suma+=i[1]#sumaremos las ventas por año
               print("\n\n\nEl total de ventas al año es: ",suma,"unidades ") #imprimimos las ventas totales en el año 2020
               decision =input("\n\nPresione enter para salir...")
               if decision=="":
                   break;
               os.system("clear")

           #<---------->Opción 3-4<----------->
           if opc4 == '4':
               print("\t\t\t#####################################")
               print("\t\t #      MESES CON MAS VENTAS          #")
               print("\t\t #######################################")      
               os.system("clear")
               listaAux=[]
               listaAux2=[]
               for i in datos.lifestore_sales:
                   listaAux.append([i[3]])#vaciaremos en la lista aux, las fechas para un mejor control
               for i in listaAux: 
                   i.append(i[0][3:5])#vaciaremos en la misma lista, las fechas tomando unicamente los meses
               lista = sorted(listaAux, key=lambda x : x[1])#ordenamos las fechas por mes
               for i in lista:
                   listaAux2.append(i[1])#vaciaremos en esta lista solo los meses ordenados
               lista2 = [[x,listaAux2.count(x)] for x in set(listaAux2)] #Contaremos cuantas ventas hubo por cada mes formando una lista como a continuación: [mes,cantidad vendidos] 
               lista2 = sorted(lista2, key=lambda x : x[1],reverse=True) #Ordenaremos los meses por el numero de ventas que tuvieron de mayor a menor 
               aux=0 #auxiliar para llevar el orden de meses de forma descendiente
               for i in lista2:
                   print("\n\n")
                   aux+=1
                   print("Mes 1.-\t",i[0],"\ttotal de ventas: ",i[1])#imprimos el mes y las ventas obtenidas respectivamente
               decision =input("\n\nPresione enter para salir...")
               if decision=="":
                   break;
               os.system("clear")
               os.system("clear")
os.system("clear")
print("\nNos vemos pronto ",user)
sleep(1)
print("Cerrando sistema...")
sleep(2)
sys.exit()               

#<----------------->FIN CÓDIGO<------------------>
    











































