#!/usr/bin/python
import re

data = '''
/* Floating Point Add: CCCCCC fffff ttttt sssss ddddd AAAAAA */
#define MASK_ADD_FP         0b01000100000000000000000000000000
#define MASK_ADD_FP_FORM    0b11111100000000000000000000111111
#define MASK_ADD_FP_FMT     0b00000011111000000000000000000000
#define MASK_ADD_FP_FT      0b00000000000111110000000000000000
#define MASK_ADD_FP_FS      0b00000000000000001111100000000000
#define MASK_ADD_FP_FD      0b00000000000000000000011111000000

/* Breakpoint: SSSSSS 00000000000000000000 BBBBBB */
#define MASK_BREAK          0b00000000000000000000000000001101
#define MASK_BREAK_FORM     0b11111100000000000000000000111111
#define MASK_BREAK_CODE     0b00000011111111111111111111000000

/* Floating Point Divide: CCCCCC fffff ttttt sssss ddddd DDDDDD */
#define MASK_DIV_FP         0b01000100000000000000000000000011
#define MASK_DIV_FP_FORM    0b11111100000000000000000000111111
#define MASK_DIV_FP_FMT     0b00000011111000000000000000000000
#define MASK_DIV_FP_FT      0b00000000000111110000000000000000
#define MASK_DIV_FP_FS      0b00000000000000001111100000000000
#define MASK_DIV_FP_FD      0b00000000000000000000011111000000

/* Floating Point Move Conditional Not Zero: CCCCCC fffff ttttt sssss ddddd MMMMMM */
#define MASK_MOVN_FP        0b01000100000000000000000000010011
#define MASK_MOVN_FP_FORM   0b11111100000000000000000000111111
#define MASK_MOVN_FP_FMT    0b00000011111000000000000000000000
#define MASK_MOVN_FP_RT     0b00000000000111110000000000000000
#define MASK_MOVN_FP_FS     0b00000000000000001111100000000000
#define MASK_MOVN_FP_FD     0b00000000000000000000011111000000

/* Floating Point Move Conditional on Zero: CCCCCC fffff ttttt sssss ddddd MMMMMM */
#define MASK_MOVZ_FP        0b01000100000000000000000000010010
#define MASK_MOVZ_FP_FORM   0b11111100000000000000000000111111
#define MASK_MOVZ_FP_FMT    0b00000011111000000000000000000000
#define MASK_MOVZ_FP_RT     0b00000000000111110000000000000000
#define MASK_MOVZ_FP_FS     0b00000000000000001111100000000000
#define MASK_MOVZ_FP_FD     0b00000000000000000000011111000000

/* Floating Point Multiply: CCCCCC fffff ttttt sssss ddddd MMMMMM */
#define MASK_MUL_FP         0b01000100000000000000000000000010
#define MASK_MUL_FP_FORM    0b11111100000000000000000000111111
#define MASK_MUL_FP_FMT     0b00000011111000000000000000000000
#define MASK_MUL_FP_FT      0b00000000000111110000000000000000
#define MASK_MUL_FP_FS      0b00000000000000001111100000000000
#define MASK_MUL_FP_FD      0b00000000000000000000011111000000

/* Software Debug Breakpoint: SSSSSS cccc cccc cccc cccc cccc SSSSSS */
#define MASK_SDBBP          0b01110000000000000000000000111111
#define MASK_SDBBP_FORM     0b11111100000000000000000000111111
#define MASK_SDBBP_CODE     0b00000011111111111111111111000000

/* Floating Point Subtract: CCCCCC fffff ttttt sssss ddddd MMMMMM */
#define MASK_SUB_FP         0b01000100000000000000000000000001
#define MASK_SUB_FP_FORM    0b11111100000000000000000000111111
#define MASK_SUB_FP_FMT     0b00000011111000000000000000000000
#define MASK_SUB_FP_FT      0b00000000000111110000000000000000
#define MASK_SUB_FP_FS      0b00000000000000001111100000000000
#define MASK_SUB_FP_FD      0b00000000000000000000011111000000

/* System Call: SSSSSS cccc cccc cccc cccc cccc SSSSSS */
#define MASK_SYSCALL        0b00000000000000000000000000001100
#define MASK_SYSCALL_FORM   0b11111100000000000000000000111111
#define MASK_SYSCALL_CODE   0b00000011111111111111111111000000

/* Trap if Equal: SSSSSS sssss ttttt cccccccccc TTTTTT */
#define MASK_TEQ            0b00000000000000000000000000110100
#define MASK_TEQ_FORM       0b11111100000000000000000000111111
#define MASK_TEQ_RS         0b00000011111000000000000000000000
#define MASK_TEQ_RT         0b00000000000111110000000000000000
#define MASK_TEQ_CODE       0b00000000000000001111111111000000

/* Trap if Greater or Equal: SSSSSS sssss ttttt cccccccccc TTTTTT */
#define MASK_TGE            0b00000000000000000000000000110000
#define MASK_TGE_FORM       0b11111100000000000000000000111111
#define MASK_TGE_RS         0b00000011111000000000000000000000
#define MASK_TGE_RT         0b00000000000111110000000000000000
#define MASK_TGE_CODE       0b00000000000000001111111111000000

/* Trap if Greater or Equal Unsigned: SSSSSS sssss ttttt cccccccccc TTTTTT */
#define MASK_TGEU           0b00000000000000000000000000110001
#define MASK_TGEU_FORM      0b11111100000000000000000000111111
#define MASK_TGEU_RS        0b00000011111000000000000000000000
#define MASK_TGEU_RT        0b00000000000111110000000000000000
#define MASK_TGEU_CODE      0b00000000000000001111111111000000

/* Trap if Less Than: SSSSSS sssss ttttt cccccccccc TTTTTT */
#define MASK_TLT            0b00000000000000000000000000110010
#define MASK_TLT_FORM       0b11111100000000000000000000111111
#define MASK_TLT_RS         0b00000011111000000000000000000000
#define MASK_TLT_RT         0b00000000000111110000000000000000
#define MASK_TLT_CODE       0b00000000000000001111111111000000

/* Trap if Less Than Unsigned: SSSSSS sssss ttttt cccccccccc TTTTTT */
#define MASK_TLTU           0b00000000000000000000000000110011
#define MASK_TLTU_FORM      0b11111100000000000000000000111111
#define MASK_TLTU_RS        0b00000011111000000000000000000000
#define MASK_TLTU_RT        0b00000000000111110000000000000000
#define MASK_TLTU_CODE      0b00000000000000001111111111000000

/* Trap if Not Equal: SSSSSS sssss ttttt cccccccccc TTTTTT */
#define MASK_TNE            0b00000000000000000000000000110011
#define MASK_TNE_FORM       0b11111100000000000000000000111111
#define MASK_TNE_RS         0b00000011111000000000000000000000
#define MASK_TNE_RT         0b00000000000111110000000000000000
#define MASK_TNE_CODE       0b00000000000000001111111111000000
'''

mask = '0b11111100000000000000000000111111'
i = 102
n = 9

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



