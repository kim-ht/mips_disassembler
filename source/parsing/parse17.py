#!/usr/bin/python
import re

data = '''
/* Move From HI Register: SSSSSS 00 0000 0000 ddddd 00000 MMMMMM */
#define MASK_MFHI           0b00000000000000000000000000010000
#define MASK_MFHI_FORM      0b11111111111111110000011111111111
#define MASK_MFHI_RD        0b00000000000000001111100000000000

/* Move From LO Register: SSSSSS 00 0000 0000 ddddd 00000 MMMMMM */
#define MASK_MFLO           0b00000000000000000000000000010010
#define MASK_MFLO_FORM      0b11111111111111110000011111111111
#define MASK_MFLO_RD        0b00000000000000001111100000000000
'''

mask = '0b11111111111111110000011111111111'
i = 147
n = 17

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




