with open('rosalind_hamm.txt') as f:
    content = f.readlines()
    seq1 = content[0].strip()
    seq2 = content[1].strip()

    print(len([(i1, i2) for (i1, i2) in zip(seq1, seq2) if i1!=i2]))