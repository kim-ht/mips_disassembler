#!/usr/bin/python
import re

data = '''
/* Move from Coprocessor 0 */
#define MASK_MFC0           0b01000000000000000000000000000000
#define MASK_MFC0_FORM      0b11111111111000000000011111111000
#define MASK_MFC0_RT        0b00000000000111110000000000000000
#define MASK_MFC0_RD        0b00000000000000001111100000000000
#define MASK_MFC0_SEL       0b00000000000000000000000000000111

/* Move from Coprocessor 2 */
#define MASK_MFC2           0b01001000000000000000000000000000
#define MASK_MFC2_FORM      0b11111111111000000000011111111000
#define MASK_MFC2_RT        0b00000000000111110000000000000000
#define MASK_MFC2_RD        0b00000000000000001111100000000000
#define MASK_MFC2_SEL       0b00000000000000000000000000000111

/* Move to Coprocessor 0: CCCCCC MMMMM ttttt ddddd 0000 000 sss */
#define MASK_MTC0           0b01000000100000000000000000000000
#define MASK_MTC0_FORM      0b11111111111000000000011111111000
#define MASK_MTC0_RT        0b00000000000111110000000000000000
#define MASK_MTC0_RD        0b00000000000000001111100000000000
#define MASK_MTC0_SEL       0b00000000000000000000000000000111

/* Move to Coprocessor 2: CCCCCC MMMMM ttttt ddddd 0000 000 sss */
#define MASK_MTC2           0b01001000100000000000000000000000
#define MASK_MTC2_FORM      0b11111111111000000000011111111000
#define MASK_MTC2_RT        0b00000000000111110000000000000000
#define MASK_MTC2_RD        0b00000000000000001111100000000000
#define MASK_MTC2_SEL       0b00000000000000000000000000000111
'''

mask = '0b11111111111000000000011111111000'
i = 132
n = 12

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




