from __future__ import division

#fasta = open('rosalind_test.txt', 'r').read()

max_gc = 0.0

with open('rosalind_gc.txt') as f:
    content = f.readlines()
    for i, line in enumerate(content):
        if line.startswith('>'):
            id = line[1:]
            # reset sequence string
            seq = ''
        else:
            newseq = line.strip()
            seq = seq + newseq
            # print if last substring or if next substring starts with '>'
            if i==len(content)-1 or content[i+1].startswith('>'):
                gc = 100 * (seq.count('G') + seq.count('C')) / len(seq)
                if gc > max_gc:
                    max_gc = gc
                    max_id = id

print(max_id, end='')
print(max_gc)