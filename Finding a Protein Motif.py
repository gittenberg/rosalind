import re
p = re.compile("[a-z]")
for m in p.finditer('a1b2c3d4'):
    print(m.start(), m.group())