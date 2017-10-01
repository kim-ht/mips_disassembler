/* main.c
 * by kimht
 */
#include "./disassembler/disassembler.h"
#include "./disassembler_printer/disassembler_printer.h"

#define MACHINE_CODE 0b00000001000010010101100000100001
                    //       ssssstttttddddd

int main(void) {
    struct operands_t operands;
    char buf[128];

    GetOperandFromCode(MACHINE_CODE, FindCorrespondingMnemonic(MACHINE_CODE), &operands);
    GetInstructionString(buf, ID_ADDU, &operands, 0x1000);
    printf("%s\n", buf);

    return 0;
}

