dna = open('rosalind_revc.txt', 'r').read().strip()
#dna = "AAAACCCGGT"

crick_watson = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

print(''.join(crick_watson[s] for s in dna)[::-1])