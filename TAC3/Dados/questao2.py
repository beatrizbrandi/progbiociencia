from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

# abrindo, lendo e identificando os itens do arquivo fasta:
multifasta = SeqIO.parse(open("../Amostra/sequencias.fasta", 'r'), "fasta")
# contador para os arquivos:
num = 0
# leitura das linhas:
for line in multifasta:
    num = num + 1
# o SeqRecord precisa ser gerado nessa ordem (id primeiro e seq depois dá bug)
    record = SeqRecord(line.seq, line.id)
# escrevendo o fasta inserindo a variável num no nome do arquivo
    SeqIO.write(record, 'Sequencia_%d.fasta' % num,"fasta")
    # cria apenas 2 arquivos .fasta. Quando chega ao limite o programa é interrompido
    if num == 2:
        break