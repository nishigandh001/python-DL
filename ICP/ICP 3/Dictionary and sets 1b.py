A = input("The Input sequence is:")
print("The Individual code sequences are:",[A[i:i+3] for i in range(0, len(A), 3)])
import csv

with open("codon.tsv") as tsvfile:
    reader=csv.reader(tsvfile,delimiter='\t')
    first_col=list(zip(*reader))[0]

with open("codon.tsv") as tsvfile1:
    reads=csv.reader(tsvfile1,delimiter='\t')
    second_col=list(zip(*reads))[1]

wordfreq = {}
for word in second_col:
    wordfreq[word]= wordfreq.setdefault(word,0)+1
print("The names and count of codons:", wordfreq)