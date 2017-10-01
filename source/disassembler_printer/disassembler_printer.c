/* disassembler_printer.c
 * by kimht
 */

#include "./disassembler_printer.h"

///////////////////////////////////////////////////////////////////////////////
/// macro functions
///////////////////////////////////////////////////////////////////////////////
#define GetGPR(r)  \
    r & 0b11111  \

///////////////////////////////////////////////////////////////////////////////
/// function declarations
///////////////////////////////////////////////////////////////////////////////
static void GetInstructionStringAdd(char *buf, struct operands_t *operands,
    unsigned int addr);

///////////////////////////////////////////////////////////////////////////////
/// variables
///////////////////////////////////////////////////////////////////////////////
static char *gpr_str[] = {
    "zero",  /* 0... */
    "at",
    "v0",
    "v1",
    "a0",
    "a1",  /* 5... */
    "a2",
    "a3",
    "t0",
    "t1",
    "t2",  /* 10... */
    "t3",
    "t4",
    "t5",
    "t6",
    "t7",  /* 15... */
    "s0",
    "s1",
    "s2",
    "s3",
    "s4",  /* 20... */
    "s5",
    "s6",
    "s7",
    "t8",
    "t9",  /* 25... */
    "k0",
    "k1",
    "gp",
    "sp",
    "fp",  /* 30... */
    "ra",
};

static void (*GetInstructionStringCallTable[])(char *, struct operands_t *,
    unsigned int) = {
    &GetInstructionStringAdd,
    0
};

///////////////////////////////////////////////////////////////////////////////
/// function definitions
///////////////////////////////////////////////////////////////////////////////

/*
 * GetInstructionString - Gets string of instruction disassembled.
 *
 * @buf - Buffer to store the result string.
 * @mnem_id - The mnemonic id of the instrcution.
 * @operands - The operands of the instruction.
 * @addr - The address the instruction locating.
 * @return - 0 on success; -1 on failure.
 */
int GetInstructionString(char *buf, int mnem_id, struct operands_t *operands,
    unsigned int addr) {
    GetInstructionStringCallTable[mnem_id](buf, operands, addr);

    return 0;
}

static void GetInstructionStringAdd(char *buf, struct operands_t *operands,
    unsigned int addr) {
    sprintf(buf, "0x%08x    %s $%s, $%s, $%s", addr, "addu",
        gpr_str[GetGPR(operands->rd)], gpr_str[GetGPR(operands->rs)],
        gpr_str[GetGPR(operands->rt)]);
}

