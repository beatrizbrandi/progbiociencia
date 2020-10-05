'''''
autora: Beatriz Brandi
Data de criacao: 11/09/20
Ultima modificacao: 14/09/20
'''
#open(caminho do arquivo):função usada para abrir o arquivo
refArquivo = open("../Amostras/TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta")
#loop usado para percorrer o arquivo
for linha in refArquivo:
#condicao usada para determinar o cabecalho
    if ">" in linha:
#atribuindo a variavel ao cabecalho
        cabecalho = linha
#imprimindo o cabecalho
        print ("Cabecalho: %s\nSequencia:" % cabecalho)
#caso nao seja cabecalho, sera atribuido a variavel sequencia
    else:
        sequencia = linha
#imprimindo a linha da sequencia
        print ("%s"%sequencia)
#por fim, fechando o arquivo
refArquivo.close()
