import funciones as fun
import csv

listaPaciente=[]
listaDireccion=[]
listaTotalHospitalizacion=[]
listaInsumos=[]
listaBonificacion=[]
listaTotal=[]
listaDatos=[]


opc=0


while (True):
    print("Registro cobros Hospital")
    print("1.-Registrar cobro")
    print("2.-Listar cobros registrados")
    print("3.-Definir sector de despacho")
    print("4.-Salir del programa")


    opc=int(input("Ingrese una opción (1-4): "))

    if (opc==1):
      fun.ingreso(listaPaciente, listaDireccion, listaTotalHospitalizacion, listaInsumos, listaBonificacion, listaTotal)
        
    if (opc==2):
        fun.mostrar(listaPaciente, listaDireccion, listaTotalHospitalizacion, listaInsumos, listaBonificacion, listaTotal)

    if (opc==3):
        fun.definirsector(listaPaciente, listaDireccion, listaTotalHospitalizacion, listaInsumos, listaBonificacion, listaTotal, listaDatos)

    if (opc==4):
        print("Gracias por preferirnos, adios!")
        break
            

