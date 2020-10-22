sequencia = str(raw_input('seq nucleotideo: '))
#variavel auxiliar para contar a quantidade de G e C
aux = 0
for i in sequencia:
# 'or' booleano. Reescreve a variavel(x==y or x==z) ou utiliza elif
    if str(i).upper() == "G" or str(i).upper() == "C":
# contador recebe valor
        aux = aux + 1

#print 'total = ' + len(sequencia) + ' GC = ' + aux + (aux/float(len(sequencia)))*100
print("total = {} GC = {} {}".format(len (sequencia), aux, (aux/float(len(sequencia)))*100))
