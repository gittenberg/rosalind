# https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Longest_common_substring#Python_3

from Bio import SeqIO

input_file = 'rosalind_lcsm.txt'

with open(input_file) as f:
    fasta_sequences = list(SeqIO.parse(f, 'fasta'))
    sequences = [str(fasta.seq) for fasta in fasta_sequences]

def long_substr(data):
    substr = ''
    if len(data) > 1 and data[0]:
        for i in range(len(data[0])):
            for j in range(len(data[0]) - i + 1):
                if j > len(substr) and is_substr(data[0][i: i + j], data):
                    substr = data[0][i: i + j]
    return substr

def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for dat in data:
        if find not in dat:
            return False
    return True

print(long_substr(sequences))