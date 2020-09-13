import csv
with open('species.csv') as csvfile:
    refArquivoEntrada = csv.reader(csvfile, delimiter=',', quotechar='|')
    for linha in refArquivoEntrada:
        data = linha
        if data[3].upper().rstrip() == "BIRD":
            print ("%s\t%s\t%s\t%s" %(data[0], data[1], data[2], data[3].rstrip()))

