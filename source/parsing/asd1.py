#!/usr/bin/python
import re

data = '''static void GetInstructionStringRsRtRd(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "0x%08x    %s \t%s, %s, %s", addr, mnem_str[mnem_id],
        gpr_str[operands->rd], gpr_str[operands->rs], gpr_str[operands->rt]);
}

static void GetInstructionStringRsRtImm(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "0x%08x    %s \t%s, %s, 0x%x", addr, mnem_str[mnem_id],
        gpr_str[operands->rt], gpr_str[operands->rs], operands->imm);
}

static void GetInstructionStringRsRtOffset(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "0x%08x    %s \t%s, %s, 0x%x", addr, mnem_str[mnem_id],
        gpr_str[operands->rs], gpr_str[operands->rt], operands->offset);
}

// required to be modified.
static void GetInstructionStringBaseOpOffset(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "not implemented.\n");
}

static void GetInstructionStringIdx(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "0x%08x    %s \t0x%x", addr, mnem_str[mnem_id],
        operands->idx*4);
}

static void GetInstructionStringBaseRtOffset(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "0x%08x    %s \t%s, 0x%x(%s)", addr, mnem_str[mnem_id],
        gpr_str[operands->rt], operands->offset, gpr_str[operands->base]);
}

// required to be modified.
static void GetInstructionStringBaseFtOffset(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "not implemented.\n");
}

// required to be modified.
static void GetInstructionStringBaseHintOffset(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "not implemented.\n");
}

// required to be modified.
static void GetInstructionStringOffset(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "not implemented.\n");
}

static void GetInstructionStringRsOffset(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "0x%08x    %s \t0x%x", addr, mnem_str[mnem_id],
        addr + operands->offset);
}

static void GetInstructionStringRsImm(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "0x%08x    %s \t%s, 0x%x", addr, mnem_str[mnem_id],
        gpr_str[operands->rs], operands->imm);
}

static void GetInstructionStringRtRdSa(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "0x%08x    %s \t%s, %s, 0x%x", addr, mnem_str[mnem_id],
        gpr_str[operands->rd], gpr_str[operands->rt], operands->sa);
}

static void GetInstructionStringRsRt(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "0x%08x    %s \t%s, %s", addr, mnem_str[mnem_id],
        gpr_str[operands->rs], gpr_str[operands->rt]);
}

// required to be modified.
static void GetInstructionStringFmtFsFd(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "not implemented.\n");
}

// required to be modified.
static void GetInstructionStringRsRdHint(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "not implemented.\n");
}

// required to be modified.
static void GetInstructionStringRsCcRd(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "not implemented.\n");
}

// required to be modified.
static void GetInstructionStringFmtFtFsFd(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "not implemented.\n");
}

// required to be modified.
static void GetInstructionStringRsHint(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "not implemented.\n");
}

// required to be modified.
static void GetInstructionStringCode20(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "not implemented.\n");
}

// required to be modified.
static void GetInstructionStringFmtRtFsFd(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "not implemented.\n");
}

// required to be modified.
static void GetInstructionStringCcOffset(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "not implemented.\n");
}

// required to be modified.
static void GetInstructionStringRtFs(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "not implemented.\n");
}

// required to be modified.
static void GetInstructionStringRtRdSel(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "not implemented.\n");
}

// required to be modified.
static void GetInstructionStringFmtFtFsCcCond(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "not implemented.\n");
}

static void GetInstructionStringRtImm(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "0x%08x    %s \t%s 0x%x", addr, mnem_str[mnem_id],
        gpr_str[operands->rt], operands->imm);
}

// required to be modified.
static void GetInstructionStringCofun(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "not implemented.\n");
}

static void GetInstructionStringRd(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "0x%08x    %s \t%s", addr, mnem_str[mnem_id],
        gpr_str[operands->rd]);
}

// required to be modified.
static void GetInstructionStringRs(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "0x%08x    %s \t%s", addr, mnem_str[mnem_id],
        gpr_str[operands->rs], operands->imm);
}

// required to be modified.
static void GetInstructionStringStype(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "not implemented.\n");
}

// required to be modified.
static void GetInstructionStringImp(char *buf, int mnem_id,
    struct operands_t *operands, unsigned int addr) {
    sprintf(buf, "not implemented.\n");
}

kim'''

l = re.findall('static void [0-9a-zA-Z]+', data)
print l

for s in l:
    print s+ '(char *buf, int mnem_id,'
    print '    struct operands_t *operands, unsigned int addr);'
