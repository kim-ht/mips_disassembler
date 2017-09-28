#!/usr/bin/python
import re

data = '''
/* Shift Word Left Logical */
#define MASK_SLL            0b00000000000000000000000000000000
#define MASK_SLL_FORM       0b11111111111000000000000000111111
#define MASK_SLL_RT         0b00000000000111110000000000000000
#define MASK_SLL_RD         0b00000000000000001111100000000000
#define MASK_SLL_SA         0b00000000000000000000011111000000

/* Shift Word Right Arithmetic: SSSSSS 00000 ttttt ddddd aaaaa SSSSSS */
#define MASK_SRA            0b00000000000000000000000000000011
#define MASK_SRA_FORM       0b11111111111000000000000000111111
#define MASK_SRA_RT         0b00000000000111110000000000000000
#define MASK_SRA_RD         0b00000000000000001111100000000000
#define MASK_SRA_SA         0b00000000000000000000011111000000

/* Shift Word Right Arithmetic Variable: SSSSSS 00000 ttttt ddddd aaaaa SSSSSS */
#define MASK_SRAV           0b00000000000000000000000000000111
#define MASK_SRAV_FORM      0b11111111111000000000000000111111
#define MASK_SRAV_RT        0b00000000000111110000000000000000
#define MASK_SRAV_RD        0b00000000000000001111100000000000
#define MASK_SRAV_SA        0b00000000000000000000011111000000

/* Shift : SSSSSS 00000 ttttt ddddd aaaaa SSSSSS */
#define MASK_SRL            0b00000000000000000000000000000111
#define MASK_SRL_FORM       0b11111111111000000000000000111111
#define MASK_SRL_RT         0b00000000000111110000000000000000
#define MASK_SRL_RD         0b00000000000000001111100000000000
#define MASK_SRL_SA         0b00000000000000000000011111000000
'''

mask = '0b11111111111000000000000000111111'
i = 73
n = 4

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




