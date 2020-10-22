seq = str(input('Sequência de AA:')).upper()
total = len(seq)
aa_count = { 'A': 0, 'C': 0, 'D' : 0,'E' : 0,'F' : 0,'G' : 0,'H' : 0,'I' : 0,'K' : 0,'L' : 0,'M' : 0,
'N' : 0,'P' : 0,'Q' : 0,'R' : 0,'S' : 0,'T' : 0,'V' : 0,'W' : 0,'Y' : 0}
for i in seq:
    aa_count[i] += 1
# calculo da porcentagem
for key , value in aa_count.items():
    if value != 0:
       percentage = float((value/total)*100)
# imprimir AAs e sua porcentagem
       print(key, percentage)
