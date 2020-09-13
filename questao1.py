refArquivo = open("TcCLB.506717.80mRNA-p1.fasta")

sequencia = ""
for linha in refArquivo:
    if ">" in linha:
        cabecalho = linha.split('|')[2].split('=')[1].rstrip()
    else:
        sequencia += linha.rstrip()
print (cabecalho + "\t"+sequencia)


refArquivo.close()
