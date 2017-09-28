#!/usr/bin/python
import re

data = '''
/* Floating Point Compare */
#define MASK_COND           0b01000100000000000000000000110000
#define MASK_COND_FORM      0b11111100000000000000000011110000
#define MASK_COND_FMT       0b00000011111000000000000000000000
#define MASK_COND_FT        0b00000000000111110000000000000000
#define MASK_COND_FS        0b00000000000000001111100000000000
#define MASK_COND_CC        0b00000000000000000000011100000000
#define MASK_COND_COND      0b00000000000000000000000000001111
'''

mask = '0b11111100000000000000000011110000'
i = 144
n = 14

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




