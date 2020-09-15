'''''
autora: Beatriz Brandi
Data de criacao: 11/09/20
Ultima modificacao: 14/09/20
'''
#import: importando da biblioteca
import csv
#com o arquivo aberto
with open('species.csv') as csvfile:
#arquivo de entrada recebe o arquivo em csv ja no formato de tabela
    refArquivoEntrada = csv.reader(csvfile, delimiter=',', quotechar='|')
#percorrendo o arquivo de entrada
    for linha in refArquivoEntrada:
        data = linha
#se a casa 3 do arquivo data for = a palavra "BIRD"
        if data[3].upper().rstrip() == "BIRD":
#imprimindo as informacoes da tabela
            print ("%s\t%s\t%s\t%s" %(data[0], data[1], data[2], data[3].rstrip()))
#o arquivo e fechado automaticamento, por causa da funcao da biblioteca "CSV"