rna = str(input('Digite sua sequência de rna:'))
# recebendo coordenadas exônicas
# ao utilizar split, transformo as variaveis em um array.
# Como temos uma coordenada (x;y), teremos um array com tamanho 2, começando em 0 e indo até 1
coordenada_a = str(input('coordenada 1:')).split(';')
coordenada_b = str(input('coordenada 2:')).split(';')
exon1 = rna[int(coordenada_a[0])-1:int(coordenada_a[-1])-1]
exon2 = rna[int(coordenada_b[0])-1:int(coordenada_b[-1])-1]
mrna = exon1+exon2
print(mrna)