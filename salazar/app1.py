import libreria
def agregar_nota():
    input("Agregar nota: ")
    print("Se ingreso nota")

def agregar_promedio():
    input("Agregar promedio: ")
    print("Se ingreso promedio")

opc=0
max=3
while(opc!=3):
    print("######### MENU ##########")
    print("# 1.agregar nota:       #")
    print("# 2.promedio            #")
    print("# salir                 #")
    print("#########################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        agregar_nota()
    if(opc==2):
        agregar_promedio()

print("fin del programa")
# fin de menu
