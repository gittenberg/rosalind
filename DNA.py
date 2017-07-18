import collections as col

dna = open('rosalind_dna.txt', 'r').read()
vals = col.Counter(dna)

print(vals['A'], vals['C'], vals['G'], vals['T'])