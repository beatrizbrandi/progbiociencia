refArquivo = open("TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta")

sequencia = ""
for linha in refArquivo:
    if ">" in linha:
        cabecalho = linha
        print ("Cabecalho: %s\nSequencia:" % cabecalho)
    else:
        sequencia = linha
        print ("%s"%sequencia)

refArquivo.close()
