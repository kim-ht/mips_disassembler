#!/usr/bin/python
import re

data = '''#define ID_ADDU  0
#define ID_ADD  1
#define ID_AND  2
#define ID_CLO  3
#define ID_CLZ  4
#define ID_MOVN  5
#define ID_MOVZ  6
#define ID_MUL  7   
#define ID_NOR  8
#define ID_OR  9
#define ID_SLTU  10
#define ID_SRLV  11
#define ID_SUB  12
#define ID_SUBU  13
#define ID_XOR  14
#define ID_SLT  15

/* 0b11111100000000000000000000000000 */
#define ID_ADDI  16
#define ID_ADDIU  17
#define ID_ANDI  18
#define ID_BEQ  19
#define ID_BEQL  20
#define ID_BNE  21
#define ID_BNEL  22
#define ID_CACHE  23
#define ID_J  24
#define ID_JAL  25
#define ID_LB  26
#define ID_LBU  27
#define ID_LDC1  28
#define ID_LDC2  29
#define ID_LH  30
#define ID_LHU  31
#define ID_LL  32
#define ID_LW  33
#define ID_LWC1  34
#define ID_LWC2  35
#define ID_LWL  36
#define ID_LWR  37
#define ID_ORI  38
#define ID_PREF  39
#define ID_SB  40
#define ID_SC  41
#define ID_SDC1  42
#define ID_SDC2  43
#define ID_SH  44
#define ID_SLTI  45
#define ID_SLTIU  46
#define ID_SW  47
#define ID_SWC1  48
#define ID_SWC2  49
#define ID_SWL  50
#define ID_SWR  51
#define ID_XORI  52

/* 0b11111111111111110000000000000000 */
#define ID_B  53
#define ID_BAL  54

/* 0b11111100000111110000000000000000 */
#define ID_BGEZ  55
#define ID_BGEZAL  56
#define ID_BGEZALL  57
#define ID_BGEZL  58
#define ID_BGTZ  59
#define ID_BGTZL  60
#define ID_BLEZ  61
#define ID_BLEZL  62
#define ID_BLTZ  63
#define ID_BLTZAL  64
#define ID_BLTZALL  65
#define ID_BLTZL  66
#define ID_TEQI  67
#define ID_TGEI  68
#define ID_TGEIU  69
#define ID_TLTI  70
#define ID_TLTIU  71
#define ID_TNEI  72

/* 0b11111111111000000000000000111111 */
#define ID_SLL  73
#define ID_SRA  74
#define ID_SRAV  75
#define ID_SRL  76

/* 0b11111100000000001111111111111111 */
#define ID_DIV  77
#define ID_DIVU  78
#define ID_MADD  79
#define ID_MADDU  80
#define ID_MSUB  81
#define ID_MSUBU  82
#define ID_MULT  83
#define ID_MULTU  84

/* 0b11111100000111110000000000111111 */
#define ID_ABS_FP  85
#define ID_CEIL_FP  86
#define ID_CVTD_FP  87
#define ID_CVTS_FP  88
#define ID_CVTW_FP  89
#define ID_FLOOR_FP  90
#define ID_JALR  91
#define ID_MOV_FP  92
#define ID_NEG_FP  93
#define ID_ROUND_FP  94
#define ID_SQRT_FP  95
#define ID_TRUNC_FP  96

/* 0b11111100000000110000011111111111 */
#define ID_MOVF  97
#define ID_MOVF_FP  98
#define ID_MOVT  99
#define ID_MOVT_FP  100

/* 0b11111100000111111111100000111111 */
#define ID_JR  101

/* 0b11111100000000000000000000111111 */
#define ID_ADD_FP  102
#define ID_BREAK  103
#define ID_DIV_FP  104
#define ID_MOVN_FP  105
#define ID_MOVZ_FP  106
#define ID_MUL_FP  107
#define ID_SDBBP  108
#define ID_SUB_FP  109
#define ID_SYSCALL  110
#define ID_TEQ  111
#define ID_TGE  112
#define ID_TGEU  113
#define ID_TLT  114
#define ID_TLTU  115
#define ID_TNE  116

/* 0b11111111111000110000000000000000 */
#define ID_BC1F  117
#define ID_BC1FL  118
#define ID_BC1T  119
#define ID_BC1TL  120
#define ID_BC2F  121
#define ID_BC2FL  122
#define ID_BC2T  123
#define ID_BC2TL  124

/* 0b11111111111000000000011111111111 */
#define ID_CFC1  125
#define ID_CFC2  126
#define ID_CTC1  127
#define ID_CTC2  128
#define ID_MFC1  129
#define ID_MTC1  130
#define ID_SLLV  131

/* 0b11111111111000000000011111111000 */
#define ID_MFC0  132
#define ID_MFC2  133
#define ID_MTC0  134
#define ID_MTC2  135

/* 0b11111111111111111111111111111111 */
#define ID_DERET  136
#define ID_ERET  137
#define ID_NOP  138
#define ID_SSNOP  139
#define ID_TLBP  140
#define ID_TLBR  141
#define ID_TLBWI  142
#define ID_TLBWR  143

/* 0b11111100000000000000000011110000 */
#define ID_COND  144

/* 0b11111111111000000000000000000000 */
#define ID_LUI  145

/* 0b11111110000000000000000000000000 */
#define ID_COP2  146

/* 0b11111111111111110000011111111111 */
#define ID_MFHI  147
#define ID_MFLO  148

/* 0b11111100000111111111111111111111 */
#define ID_MTHI  149
#define ID_MTLO  150

/* 0b11111111111111111111100000111111 */
#define ID_SYNC  151

/* 0b11111110000000000000000000111111 */
#define ID_WAIT  152'''

l = re.findall('ID_([0-9A-Z]+_FP|[0-9A-Z]+)', data)

s = ''
for i in range(len(l)):
    s += '"'+ l[i].lower() + '", '
    if ( (i + 1) % 5 == 0 ):
        s += '\n'

print s

