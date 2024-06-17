import csv
lista=[]



def val_porcentaje(a):
    
    while a<0 or a>100:
        a=int(input('El valor de porcentaje debe estar entre 0 a 100, vuelva a ingresar porcentaje\n'))
    
    return a
 
def categoria(x):
    if x>=0 and x<=25:
        cat_interna='Chiste'
    elif x>=26 and x<=50:
        cat_interna='Anécdota'
    elif x>=51 and x<=75:
        cat_interna='Peligro'   
    elif x>=76 and x<=99:
        cat_interna='Atención'          
    elif x==100:
        cat_interna='Esclavitud'      
    return cat_interna    
def decision():
    deci=False
    confi=input('¿Desea eliminar el plan (Si/No)?\n').lower()
    if confi=='si':
        deci=True
    else:
        deci=False
    return deci
def promedio():
    acum=0
    for x in lista:
        acum=acum+x[2]
    prom=acum/len(lista)
    print(f'El porcentaje de efectividad promedio es {prom}')
    
def mayor():
    mayor=0
    for x in lista:
        if x[2]>mayor:
            mayor=x[2]
    print(f'El valor de porcentaje de efectividad más alto es {mayor}%')        
    
while True:
    try:
        print("*"*30)
        print("-.-.-.- M E N Ú -.-.-.-")
        print("")
        print("1.- Agregar plan")
        print("2.- Listar planes")
        print("3.- Eliminar plan por ID")
        print("4.- Generar CSV")
        print("5.- Cargar CSV")
        print("6.- Estadísticas")
        print("0.- Salir")
        print("")
        op=int(input('Ingrese una opción\n'))
        if op==1:
            id=int(input('Ingrese ID\n'))
            nombre=input('Ingrese nombre\n')
            porcentaje=int(input('Ingrese porcentaje de efectividad\n'))
            porcentaje=val_porcentaje(porcentaje)
            interna_cat=categoria(porcentaje)
            listita=[id,nombre,porcentaje,interna_cat]
            lista.append(listita)
            print('Plan agregado exitosamente')    
        elif op==2:
            if len(lista)==0:
                print('No se han ingresado datos...')
            else:
                for x in lista:
                    print('ID:',x[0],'Nombre:',x[1],'Porcentaje de efectividad:',x[2],'%','Categoría interna:', x[3])      
        elif op==3:
            encontrado=False
            id=int(input('Ingrese ID para eliminar plan\n'))
            for x in lista:
                if id== x[0]:
                    print('ID:',x[0],'Nombre:',x[1],'Porcentaje de efectividad:',x[2],'%','Categoría interna:', x[3])
                    encontrado=True
                    break
            if encontrado==False:
                print('La ID no existe...')    
            else:
                confirmacion=decision()    
                if confirmacion:
                    lista.remove(x)
                    print('Se ha eliminado el plan exitosamente')
                else:
                    print('Se ha cancelado la eliminación')
          
        elif op==4:
            print("-.-.-.- G E N E R A R  C S V -.-.-.-")
            with open ('Plan.csv','w',newline='') as Planes:
                escritor=csv.writer(Planes)
                escritor.writerow(['ID','Nombre','Porcentaje de efectividad','Categoría interna'])
                escritor.writerows(lista)
                print('Archivo generado exitosamente...')
        elif op==5:
            print("-.-.-.- C A R G A R  C S V -.-.-.-")
            lista.clear()
            cont=0
            with open ('Plan.csv','r',newline='') as Planes:
                lector=csv.reader(Planes)
                for x in lector:
                    if cont==0:
                        cont=cont+1
                        continue
                    else:
                        ID=int(x[0])
                        nom=x[1]
                        por=int(x[2])
                        cat=x[3]
                        new=[ID,nom,por,cat]
                        lista.append(new)
            print('Archivo cargado correctamente')            
            
        elif op==6:
            print("-.-.-.- E S T A D Í S T I C A S -.-.-.-")
            print('')
            if len(lista)==0:
                print('No se ha agregado ningún plan...')
            else:
                promedio()
                mayor()
                
        elif op==0:
            print("Saliendo del programa...")
            break
        else: 
            print("Comando desconocido, volviendo al menú principal...")    
    except:
        print('Error desconocido, volviendo al menú principal')                        
        
#Enlace Github: https://github.com/Romi316/Hormazabal-Romina-03.git       