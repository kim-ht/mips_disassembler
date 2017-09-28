#!/usr/bin/python
import re

data = '''
/* Add Unsigned Word: SSSSSS sssss ttttt ddddd 00000 AAAAAA */
#define MASK_ADDU           0b00000000000000000000000000100001
#define MASK_ADDU_FORM      0b11111100000000000000011111111111
#define MASK_ADDU_RS        0b00000011111000000000000000000000
#define MASK_ADDU_RT        0b00000000000111110000000000000000
#define MASK_ADDU_RD        0b00000000000000001111100000000000

/* Add Word: SSSSSS sssss ttttt ddddd 00000 AAAAAA */
#define MASK_ADD            0b00000000000000000000000000100000
#define MASK_ADD_FORM       0b11111100000000000000011111111111
#define MASK_ADD_FORM_FS    0b00000011111000000000000000000000
#define MASK_ADD_FORM_FT    0b00000000000111110000000000000000
#define MASK_ADD_FORM_FD    0b00000000000000001111100000000000

/* And: SSSSSS sssss ttttt ddddd 00000 AAAAAA */
#define MASK_AND            0b00000000000000000000000000100100
#define MASK_AND_FORM       0b11111100000000000000011111111111
#define MASK_AND_RS         0b00000011111000000000000000000000
#define MASK_AND_RT         0b00000000000111110000000000000000
#define MASK_AND_RD         0b00000000000000001111100000000000

/* Count Leading Ones in Word: SSSSSS sssss ttttt ddddd 00000 CCCCCC */
#define MASK_CLO            0b01110000000000000000000000100001
#define MASK_CLO_FORM       0b11111100000000000000011111111111
#define MASK_CLO_RS         0b00000011111000000000000000000000
#define MASK_CLO_RT         0b00000000000111110000000000000000
#define MASK_CLO_RD         0b00000000000000001111100000000000

/* Count Leading Zeros in Word: SSSSSS sssss ttttt ddddd 00000 CCCCCC */
#define MASK_CLZ            0b01110000000000000000000000100000
#define MASK_CLZ_FORM       0b11111100000000000000011111111111
#define MASK_CLZ_RS         0b00000011111000000000000000000000
#define MASK_CLZ_RT         0b00000000000111110000000000000000
#define MASK_CLZ_RD         0b00000000000000001111100000000000

/* Move Conditional on Not Zero: SSSSSS sssss ttttt ddddd 00000 MMMMMM */
#define MASK_MOVN           0b00000000000000000000000000001011
#define MASK_MOVN_FORM      0b11111100000000000000011111111111
#define MASK_MOVN_RS        0b00000011111000000000000000000000
#define MASK_MOVN_RT        0b00000000000111110000000000000000
#define MASK_MOVN_RD        0b00000000000000001111100000000000

/* Move Conditional Zero: SSSSSS sssss ttttt ddddd 00000 MMMMMM */
#define MASK_MOVZ           0b00000000000000000000000000001010
#define MASK_MOVZ_FORM      0b11111100000000000000011111111111
#define MASK_MOVZ_RS        0b00000011111000000000000000000000
#define MASK_MOVZ_RT        0b00000000000111110000000000000000
#define MASK_MOVZ_RD        0b00000000000000001111100000000000

/* Multiply Word to GPR: SSSSSS sssss ttttt ddddd 00000 MMMMMM */
#define MASK_MUL            0b01110000000000000000000000000010
#define MASK_MUL_FORM       0b11111100000000000000011111111111
#define MASK_MUL_RS         0b00000011111000000000000000000000
#define MASK_MUL_RT         0b00000000000111110000000000000000
#define MASK_MUL_RD         0b00000000000000001111100000000000

/* Not Or: SSSSSS sssss ttttt ddddd 00000 NNNNNN */
#define MASK_NOR            0b00000000000000000000000000100111
#define MASK_NOR_FORM       0b11111100000000000000011111111111
#define MASK_NOR_RS         0b00000011111000000000000000000000
#define MASK_NOR_RT         0b00000000000111110000000000000000
#define MASK_NOR_RD         0b00000000000000001111100000000000

/* Or: SSSSSS sssss ttttt ddddd 00000 NNNNNN */
#define MASK_OR             0b00000000000000000000000000100101
#define MASK_OR_FORM        0b11111100000000000000011111111111
#define MASK_OR_RS          0b00000011111000000000000000000000
#define MASK_OR_RT          0b00000000000111110000000000000000
#define MASK_OR_RD          0b00000000000000001111100000000000

/* Set on Less Than Unsigned: SSSSSS sssss ttttt ddddd 00000 SSSSSS */
#define MASK_SLTU           0b00000000000000000000000000101011
#define MASK_SLTU_FORM      0b11111100000000000000011111111111
#define MASK_SLTU_RS        0b00000011111000000000000000000000
#define MASK_SLTU_RT        0b00000000000111110000000000000000
#define MASK_SLTU_RD        0b00000000000000001111100000000000

/* Shift Word Right Logical Variable */
#define MASK_SRLV           0b00000000000000000000000000000110
#define MASK_SRLV_FORM      0b11111100000000000000011111111111
#define MASK_SRLV_RS        0b00000011111000000000000000000000
#define MASK_SRLV_RT        0b00000000000111110000000000000000
#define MASK_SRLV_RD        0b00000000000000001111100000000000

/* Subtract Word: SSSSSS sssss ttttt ddddd 00000 SSSSS */
#define MASK_SUB            0b00000000000000000000000000100010
#define MASK_SUB_FORM       0b11111100000000000000011111111111
#define MASK_SUB_RS         0b00000011111000000000000000000000
#define MASK_SUB_RT         0b00000000000111110000000000000000
#define MASK_SUB_RD         0b00000000000000001111100000000000

/* Subtract Unsigned Word: SSSSSS sssss ttttt ddddd 00000 SSSSS */
#define MASK_SUBU           0b00000000000000000000000000100011
#define MASK_SUBU_FORM      0b11111100000000000000011111111111
#define MASK_SUBU_RS        0b00000011111000000000000000000000
#define MASK_SUBU_RT        0b00000000000111110000000000000000
#define MASK_SUBU_RD        0b00000000000000001111100000000000

/* Exclusive OR: SSSSSS sssss ttttt ddddd 00000 XXXXXX */
#define MASK_XOR            0b00111000000000000000000000000000
#define MASK_XOR_FORM       0b11111100000000000000011111111111
#define MASK_XOR_RS         0b00000011111000000000000000000000
#define MASK_XOR_RT         0b00000000000111110000000000000000
#define MASK_XOR_RD         0b00000000000000001111100000000000

/* Set on Less Than: SSSSSS sssss ttttt ddddd 00000 SSSSSS */
#define MASK_SLT            0b00000000000000000000000000101010
#define MASK_SLT_FORM       0b11111100000000000000011111111111
#define MASK_SLT_RS         0b00000011111000000000000000000000
#define MASK_SLT_RT         0b00000000000111110000000000000000
#define MASK_SLT_RD         0b00000000000000001111100000000000
'''

mask = '0b11111100000000000000011111111111'
i = 0
n = 0

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




