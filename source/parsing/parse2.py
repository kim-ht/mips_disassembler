#!/usr/bin/python
import re

data = '''
#define MASK_B              0b00010000000000000000000000000000
#define MASK_B_FORM         0b11111111111111110000000000000000
#define MASK_B_OFFSET       0b00000000000000001111111111111111

/* Branch and Link: RRRRRR 00000 BBBBB oooooooooooooooo */
#define MASK_BAL            0b00000100000100010000000000000000
#define MASK_BAL_FORM       0b11111111111111110000000000000000
#define MASK_BAL_OFFSET     0b00000000000000001111111111111111
'''

mask = '0b11111111111111110000000000000000'
i = 53
n = 2

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




