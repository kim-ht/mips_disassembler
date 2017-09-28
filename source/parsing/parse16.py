#!/usr/bin/python
import re

data = '''
/* Coprocessor Operation to Coprocessor 2: CCCCCC C ccccccccccccccccccccccccc */
#define MASK_COP2           0b01001010000000000000000000000000
#define MASK_COP2_FORM      0b11111110000000000000000000000000
#define MASK_COP2_COFUN     0b00000001111111111111111111111111
'''

mask = '0b11111110000000000000000000000000'
i = 146
n = 16

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




