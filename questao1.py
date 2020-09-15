'''''
autora: Beatriz Brandi
Data de criacao: 11/09/20
Ultima modificacao: 14/09/20
'''
#open(caminho do arquivo): função usada para abrir o arquivo
refArquivo = open("TcCLB.506717.80mRNA-p1.fasta")
#inicializacao da variavel sequencia
sequencia = ""
#loop usado para percorrer o arquivo
for linha in refArquivo:
#condicao usada para determinar o cabecalho
    if ">" in linha:
#isolando apenas o nome gene
        cabecalho = linha.split('|')[2].split('=')[1].rstrip()
#caso nao seja cabecalho, sera atribuido a variavel sequencia
    else:
        sequencia += linha.rstrip()
#imprimindo gene e sequencia no formato tabulado
print (cabecalho + "\t"+sequencia)

#por fim, fechando o arquivo
refArquivo.close()
