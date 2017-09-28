#!/usr/bin/python
import re

data = '''
/* Enter Standby Mode: CCCCCC C IIIIIIIIIIIIIIIIIIIIIII WWWWWW */
#define MASK_WAIT           0b01000000000000000000000000100000
#define MASK_WAIT_FORM      0b11111110000000000000000000111111
#define MASK_WAIT_IMP       0b00000001111111111111111111000000
'''

mask = '0b11111110000000000000000000111111'
i = 152
n = 20

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




