instring = '18599 17290 18335 19009 18071 18849'

gs = [int(elem) for elem in instring.split(" ")]

print(gs)
'''
AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa
'''
dominant = 2 * (gs[0] + gs[1] + gs[2] + 0.75 * gs[3] + 0.5 * gs[4])

print(dominant)