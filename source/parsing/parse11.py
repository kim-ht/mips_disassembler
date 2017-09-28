#!/usr/bin/python
import re

data = '''
/* Move Control Word From Floating Point: CCCCCC CCCCC ttttt sssss 000 0000 0000 */
#define MASK_CFC1           0b01000100010000000000000000000000
#define MASK_CFC1_FORM      0b11111111111000000000011111111111
#define MASK_CFC1_RT        0b00000000000111110000000000000000
#define MASK_CFC1_FS        0b00000000000000001111100000000000

/* Move Control Word From Coprocessor 2: CCCCCC CCCCC ttttt sssss 000 0000 0000 */
#define MASK_CFC2           0b01001000010000000000000000000000
#define MASK_CFC2_FORM      0b11111111111000000000011111111111
#define MASK_CFC2_RT        0b00000000000111110000000000000000
#define MASK_CFC2_FS        0b00000000000000001111100000000000

/* Move Control Word to Floating Point: CCCCCC CCCCC ttttt sssss 000 0000 0000 */
#define MASK_CTC1           0b01000100110000000000000000000000
#define MASK_CTC1_FORM      0b11111111111000000000011111111111
#define MASK_CTC1_RT        0b00000000000111110000000000000000
#define MASK_CTC1_FS        0b00000000000000001111100000000000

/* Move Control Word to Coprocessor 2: CCCCCC CCCCC ttttt sssss 000 0000 0000 */
#define MASK_CTC2           0b01001000110000000000000000000000
#define MASK_CTC2_FORM      0b11111111111000000000011111111111
#define MASK_CTC2_RT        0b00000000000111110000000000000000
#define MASK_CTC2_FS        0b00000000000000001111100000000000

/* Move Word From Floating Point: CCCCCC MMMMM ttttt sssss 000 0000 0000 */
#define MASK_MFC1           0b01000100000000000000000000000000
#define MASK_MFC1_FORM      0b11111111111000000000011111111111
#define MASK_MFC1_RT        0b00000000000111110000000000000000
#define MASK_MFC1_FS        0b00000000000000001111100000000000

/* Move Word to Floating Point: CCCCCC MMMMM ttttt sssss 000 0000 0000 */
#define MASK_MTC1           0b01000100000000000000000000000000
#define MASK_MTC1_FORM      0b11111111111000000000011111111111
#define MASK_MTC1_RT        0b00000000000111110000000000000000
#define MASK_MTC1_FS        0b00000000000000001111100000000000

/* Shift Word Left Logical Variable: SSSSSS sssss ttttt ddddd 00000 SSSSSS */
#define MASK_SLLV           0b00000000000000000000000000000100
#define MASK_SLLV_FORM      0b11111111111000000000011111111111
#define MASK_SLLV_RT        0b00000000000111110000000000000000
#define MASK_SLLV_RD        0b00000000000000001111100000000000
#define MASK_SLLV_SA        0b00000000000000000000011111000000

'''

mask = '0b11111111111000000000011111111111'
i = 125
n = 11

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




