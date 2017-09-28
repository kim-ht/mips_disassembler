#!/usr/bin/python
import re

data = '''
/* Move to HI Register: SSSSSS sssss 000 0000 0000 0000 MMMMMM */
#define MASK_MTHI           0b00000000000000000000000000010001
#define MASK_MTHI_FORM      0b11111100000111111111111111111111
#define MASK_MTHI_RS        0b00000011111000000000000000000000

/* Move to LO Register: SSSSSS sssss 000 0000 0000 0000 MMMMMM */
#define MASK_MTLO           0b00000000000000000000000000010011
#define MASK_MTLO_FORM      0b11111100000111111111111111111111
#define MASK_MTLO_RS        0b00000011111000000000000000000000
'''

mask = '0b11111100000111111111111111111111'
i = 149
n = 18

tmp_l = re.findall('MASK_([0-9A-Z]+_FP|[0-9A-Z]+)', data)
my_set = set()
l = []
for e in tmp_l:
    if e not in my_set:
        l.append(e)
        my_set.add(e)
print l

print '/* ' + mask + ' */'
for s in l:
    print '#define ID_' + s + '  ' + str(i)
    i += 1

print '#define FindCorrespondingMnemonic'+ str(n) +'(code) {  \\'
print '    switch ( code & ' + mask + ' ) {  \\'

for s in l:
    print '    case MASK_' + s + ':  \\'
    print '        return ID_' + s + ';  \\'

print '    }  \\'
print '}'




