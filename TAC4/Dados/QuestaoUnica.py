import re
from Bio.Seq import Seq
from Bio import SeqIO

# Função que conta os motivos usando count()
def Counting_Motifs(sequence, motif):
    _id = str(line.id)
    mc = sequence.count(motif)
    if mc != 0:
        print("Identificador:", _id,"Motivo:", motif,"Count:", mc,sep=" ")

    # retornar 0 ou um número nao faz diferença, visto que 0 não irá interferir na acumulação.
    return mc
        
# Lendo sequencia do usuário
motif = str(input("Insira seu motivo de DNA ou AA:")).upper()
contador = 0

# se o motif tiver APENAS as letras A,C,G ou T, será considerada uma sequência de DNA
if re.search('^[ACGT]+$', motif):
    print("É DNA.")
    multifasta = SeqIO.parse(open("../Amostra/TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta","r"), "fasta")
    for line in multifasta:
        sequence = str(line.seq)
        contador += Counting_Motifs(sequence, motif)

# se o motif tiver outra letra que não A,C,G ou, T, será considerada uma sequencia de AA
else:
    print("É uma sequência de AA.")
    multifasta = SeqIO.parse(open("../Amostra/TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta",'r'), "fasta")
    for line in multifasta:
        sequence = str(line.seq)
        contador += Counting_Motifs(sequence, motif)

print("Quantidade de repeticoes {}".format(contador))