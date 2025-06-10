import random
from os import system
from msvcrt import getch
numeros=[]

for i in range(100):
    n=random.randint(0,10)
    numeros.append(n)

# 1
print(numeros)
print("========================================================================================================")

# 2
for i in range(0,len(numeros),2):
 print(numeros[i],end="/")
print(f"\n========================================================================================================")

# 3
maximo=max(numeros)
print(f"Numero maximo : {maximo}")

# 4
print("Indice del numero maximo: ")
print(numeros.index(maximo))
for i in range (len(numeros)):
  if maximo==numeros[i]:
    print(f"{i}",end=" ")
print("")

# 5
minimo=min(numeros)
print(f"Numero minimo : {minimo}")

# 6
print("Indice del numero minimo: ")
print(numeros.index(minimo))
for i in range (len(numeros)):
  if minimo==numeros[i]:
    print(f"{i}",end=" ")
print("")

# 7 y 8 
print("========================================================================================================")
personas=[]
while True:
    try:
     print("Presione una tecla para continuar")
     getch()
     system("cls")
     print("""
     1) Agregar persona
     2) Buscar persona
     3) Ver personas      
     4) Terminar programa
     """)
     opcion=int(input("Seleccione una opcion : "))
     match opcion:
       case 1:
          if len(personas)<10:
            nombre=input("Ingrese el nombre de la persona: ").capitalize()
            if len(nombre.strip())>0:
              if not nombre in personas:
                personas.append(nombre)
                print("Nombre registrado con exito")
              else:
                print("Nombre ya registrado")
            else:
              print("Nombre ingresado no valido")
          else:
            print("Maximo de personas ingresadas")
       case 2:
            if (len(personas))>0: 
             indice=int(input("Ingrese el numero de la persona que desea ver : "))
             if indice>0 and indice<=10:
              print(personas[indice-1])
             else:
               print("Indice no existente")
            else:
              print("No hay ingresos")
       case 3:
            if (len(personas))>0:
                for i in range(len(personas)):
                 print(f"{i+1}) {personas[i]}")
            else:
              print("No hay ingresos")
       case 4:
         break
       case _:
          print("opcion no valida")
    except Exception as e:
     print(e)
