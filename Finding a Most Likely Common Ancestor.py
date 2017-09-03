import numpy as np

ns = "ACGT"
counts = {n: None for n in ns}
dna = ""


def count(dna):
    for n in ns:
        mask = np.array([1 if letter == n else 0 for letter in dna])
        if counts[n] is None:
            # first time
            counts[n] = mask
        else:
            counts[n] += mask

with open('rosalind_cons.txt') as f:
    content = f.readlines()
    for line in content:
        if not line.startswith(">"):
            dna += line.strip()
        if line.startswith(">") and dna:
            # count
            count(dna)
            # reset
            dna = ""
    # last time
    count(dna)

preprofile = np.array([counts[n] for n in ns])
argmaxes = np.argmax(preprofile, axis=0)
consensus = "".join([ns[i] for i in argmaxes])

print(consensus)
for n in ns:
    print("{}: {}".format(n, " ".join([str(c) for c in counts[n]])))
