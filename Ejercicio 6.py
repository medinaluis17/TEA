from this import d


def calculoSalario(horas,tarifa):
 horasextras = horas - maxhoras_semanales
 if(horasextras>0):
    pago = (maxhoras_semanales * tarifa) + (horasextras * (tarifa * 1.5))
 else:
    pago = horas * tarifa
 return pago

maxhoras_semanales = 40
horas = int (input("Ingrese la cantidad de horas: "))
tarifa = float(input("Ingrese la tarifa por hora: "))
salario = calculoSalario(horas, tarifa)
print("Su salario es:")
print (salario)

