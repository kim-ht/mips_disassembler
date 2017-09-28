#!/usr/bin/python
import re

data = '''
/* Move Conditional on Floating Point False: SSSSSS sssss ccc 0 t ddddd 00000 MMMMMM */
#define MASK_MOVF           0b00000000000000000000000000000001
#define MASK_MOVF_FORM      0b11111100000000110000011111111111
#define MASK_MOVF_RS        0b00000011111000000000000000000000
#define MASK_MOVF_CC        0b00000000000111000000000000000000
#define MASK_MOVF_RD        0b00000000000000001111100000000000


/* Floating Point Move Conditional on Floating Point False: SSSSSS sssss ccc 0 t ddddd 00000 MMMMMM */
#define MASK_MOVF_FP        0b01000100000000000000000000010001
#define MASK_MOVF_FP_FORM   0b11111100000000110000011111111111
#define MASK_MOVF_FP_RS     0b00000011111000000000000000000000
#define MASK_MOVF_FP_CC     0b00000000000111000000000000000000
#define MASK_MOVF_FP_RD     0b00000000000000001111100000000000

/* Move Conditional on Floating Point True: SSSSSS sssss ccc 0 f ddddd 00000 MMMMMM */
#define MASK_MOVT           0b00000000000000010000000000000001
#define MASK_MOVT_FORM      0b11111100000000110000011111111111
#define MASK_MOVT_RS        0b00000011111000000000000000000000
#define MASK_MOVT_CC        0b00000000000111000000000000000000
#define MASK_MOVT_RD        0b00000000000000001111100000000000

/* Floating Point Move Conditional on Floating Point True: CCCCCC fffff ccc 0 f sssss ddddd MMMMMM */
#define MASK_MOVT_FP         0b01000100000000010000000000010001
#define MASK_MOVT_FP_FORM    0b11111100000000110000011111111111
#define MASK_MOVT_FP_RS      0b00000011111000000000000000000000
#define MASK_MOVT_FP_CC      0b00000000000111000000000000000000
#define MASK_MOVT_FP_RD      0b00000000000000001111100000000000
'''

mask = '0b11111100000000110000011111111111'
i = 97
n = 7

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




