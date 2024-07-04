import csv

def ingreso(listaPaciente, listaDireccion, listaTotalHospitalizacion, listaInsumos, listaBonificacion, listaTotal):
        varNombre=input("Ingrese el nombre del paciente: ")
        varDireccion=input("Ingrese la dirección del paciente: ")
        varDiasHosp=int(input("Ingrese los días de hospitalizacion: "))
        varTotalHosp=(varDiasHosp*90_000)
        varInsumos=200_000
        varBonSalud=float(input("Ingrese el porcentaje de bonificacion que cubre su operador de salud (Solo en valor decimal es deir 0=0%, 0,1=10% 1=100% etc): "))
        varBonificacion=(varTotalHosp+varInsumos)*(varBonSalud)
        varTotal=(varTotalHosp+varInsumos)-varBonificacion

        listaPaciente.append(varNombre)
        listaDireccion.append(varDireccion)
        listaTotalHospitalizacion.append(varTotalHosp)
        listaInsumos.append(varInsumos)
        listaBonificacion.append(varBonificacion)
        listaTotal.append(varTotal)

def mostrar(listaPaciente, listaDireccion, listaTotalHospitalizacion, listaInsumos, listaBonificacion, listaTotal):
    print("Cobros Registrados")
    print("Paciente\t Direccion\t Hospitalizacion\t Insumos\t Bonificacion\t Total\t")
    for i in range(len(listaPaciente)):
        print(f"{listaPaciente[i]}\t\t {listaDireccion[i]}\t\t {listaTotalHospitalizacion[i]}\t\t\t {listaInsumos[i]}\t\t {listaBonificacion[i]}\t {listaTotal[i]}")


def definirsector(listaPaciente, listaDireccion, listaTotalHospitalizacion, listaInsumos, listaBonificacion, listaTotal, listaDatos):
    varSector="a"
    listaSectores=["centro", "norte", "sur"]
    while (varSector not in listaSectores):
        varSector=input("Ingrese el sector de despacho:")
        if (varSector not in listaSectores):
            print("El sector ingresado no es válido")
    listaDatos.append([varNombre, varDireccion, varTotalHosp, varInsumos ,varBonificacion, varTotal])
    with open ('ArchivoHospital.csv', 'w') as salidaLogica:
        objetoCsv=csv.writer(salidaLogica)
        objetoCsv.writerows(listaDatos) 

    varNombre=input("Ingrese el nombre del paciente: ")
    varDireccion=input("Ingrese la dirección del paciente: ")
    varDiasHosp=int(input("Ingrese los días de hospitalizacion: "))
    varTotalHosp=(varDiasHosp*90_000)
    varInsumos=200_000
    varBonSalud=float(input("Ingrese el porcentaje (%) de bonificacion que cubre su operador de salud: "))
    varBonificacion=(varTotalHosp+varInsumos)*varBonSalud
    varTotal=(varTotalHosp+varInsumos)-varBonificacion

    listaPaciente.append(varNombre)
    listaDireccion.append(varDireccion)
    listaTotalHospitalizacion.append(varTotalHosp)
    listaInsumos.append(varInsumos)
    listaBonificacion.append(varBonificacion)
    listaTotal.append(varTotal)
    