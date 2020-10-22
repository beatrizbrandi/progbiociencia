seqA = str(input('Sequência 1:'))
seqB = str(input('Sequência 2:'))
sequencia = seqA + seqB
# invertendo a ordem da sequência
rev_seq = sequencia[::-1]
complemento_reverso = ''
for i in rev_seq:
    if i.upper() == 'A':
        complemento_reverso += 'T'
    if i.upper() == 'T':
        complemento_reverso += 'A'
    if i.upper() == 'G':
        complemento_reverso += 'C'
    if i.upper() == 'C':
        complemento_reverso += 'G'
print("Complemento reverso: {}".format(complemento_reverso))