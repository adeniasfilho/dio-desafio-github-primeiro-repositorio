segundos = int(input())

minutos = int(segundos/60)   #TODO Implementar a formula para calcular os minutos.
segundos = int(segundos - (minutos * 60))
horas = int(minutos/60) #TODO Implementar a formula para calcular as horas.
minutos = int(minutos - (horas * 60))

print("{}:{}:{}".format(horas, minutos, segundos))