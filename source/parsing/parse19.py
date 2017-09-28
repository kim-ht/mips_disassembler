#!/usr/bin/python
import re

data = '''
/* Synchronize Shared Memory: SSSSSS 00 0000 0000 0000 0 sssss SSSSSS */
#define MASK_SYNC           0b00000000000000000000000000001111
#define MASK_SYNC_FORM      0b11111111111111111111100000111111
#define MASK_SYNC_STYPE     0b00000000000000000000011111000000
'''

mask = '0b11111111111111111111100000111111'
i = 151
n = 19

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




