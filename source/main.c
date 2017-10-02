/* main.c
 * by kimht
 */
#include "./disassembler/disassembler.h"
#include "./disassembler_printer/disassembler_printer.h"

#define MACHINE_CODE 0x02002021

int main(void) {
    struct operands_t operands;
    char buf[128];
    int mnem_id;

    mnem_id = FindCorrespondingMnemonic(MACHINE_CODE);
    GetOperandFromCode(MACHINE_CODE, mnem_id, &operands);
    GetInstructionString(buf, mnem_id, &operands, 0x1000);
    printf("%s\n", buf);

    return 0;
}

