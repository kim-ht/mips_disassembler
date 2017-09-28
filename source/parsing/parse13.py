#!/usr/bin/python
import re

data = '''
/* Debug Exception Return */
#define MASK_DERET          0b01000010000000000000000000011111
#define MASK_DERET_FORM     0b11111111111111111111111111111111

/* Exception Return: CCCCCC C 000 0000 0000 0000 0000 EEEEEE */
#define MASK_ERET           0b01000010000000000000000000011000
#define MASK_ERET_FORM      0b11111111111111111111111111111111

/* No Operation: 000000 00000 00000 00000 00000 000000 */
#define MASK_NOP            0b00000000000000000000000000000000
#define MASK_NOP_FORM       0b11111111111111111111111111111111

/* Superscalar No Operation: 000000000000000000000000001000000 */
#define MASK_SSNOP          0b00000000000000000000000001000000
#define MASK_SSNOP_FORM     0b11111111111111111111111111111111

/* Probe TLB for Matching Etnry: CCCCCC C 000 0000 0000 0000 0000 TTTTTT */
#define MASK_TLBP           0b01000010000000000000000000001000
#define MASK_TLBP_FORM      0b11111111111111111111111111111111

/* Read Indexed TLB Entry: CCCCCC C 000 0000 0000 0000 0000 TTTTTT */
#define MASK_TLBR           0b01000010000000000000000000000001
#define MASK_TLBR_FORM      0b11111111111111111111111111111111

/* Write Indexed TLB Entry: CCCCCC C 000 0000 0000 0000 0000 TTTTTT */
#define MASK_TLBWI          0b01000010000000000000000000000010
#define MASK_TLBWI_FORM     0b11111111111111111111111111111111

/* Write Random TLB Entry: CCCCCC C 000 0000 0000 0000 0000 TTTTTT */
#define MASK_TLBWR          0b01000010000000000000000000000110
#define MASK_TLBWR_FORM     0b11111111111111111111111111111111
'''

mask = '0b11111111111111111111111111111111'
i = 136
n = 13

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




