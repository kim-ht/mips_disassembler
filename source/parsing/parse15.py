#!/usr/bin/python
import re

data = '''
/* Load Upper Immediate: LLLLLL 00000 ttttt iiii iiii iiii iiii */
#define MASK_LUI            0b00111100000000000000000000000000
#define MASK_LUI_FORM       0b11111111111000000000000000000000
#define MASK_LUI_RT         0b00000000000111110000000000000000
#define MASK_LUI_IMM        0b00000000000000001111111111111111
'''

mask = '0b11111111111000000000000000000000'
i = 145
n = 15

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




