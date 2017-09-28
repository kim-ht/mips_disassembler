#!/usr/bin/python
import re

data = '''
i/* Jump Register: SSSSSS sssss 00 0000 0000 hhhhh JJJJJJ */
#define MASK_JR             0b00000000000000000000000000001000
#define MASK_JR_FORM        0b11111100000111111111100000111111
#define MASK_JR_RS          0b00000011111000000000000000000000
#define MASK_JR_HINT        0b00000000000000000000011111000000
'''

mask = '0b11111100000111111111100000111111'
i = 101
n = 8

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




