from Bio import SeqIO

k = 3
input_file = 'rosalind_grph.txt'

with open(input_file) as f:
    fasta_sequences = list(SeqIO.parse(f, 'fasta'))

for fasta1 in fasta_sequences:
    for fasta2 in fasta_sequences:
        name1, sequence1 = fasta1.id, str(fasta1.seq)
        name2, sequence2 = fasta2.id, str(fasta2.seq)
        if sequence1 == sequence2:
            continue
        suffix = sequence1[-k:]
        prefix = sequence2[:k]
        if prefix == suffix:
            print(name1, name2)
