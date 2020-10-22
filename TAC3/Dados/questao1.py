from Bio.Seq import Seq

dna = Seq(str(input('Insira sua sequência de DNA:')))
# a transcrição do DNA
mRNA = dna.transcribe()
# tradução a partir do RNA
ptn = mRNA.translate()

print('mRNA:',mRNA,'ptn:',ptn,sep='\n')