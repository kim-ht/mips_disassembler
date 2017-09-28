/* main.c
 * by kimht
 */
#include "./disassembler/disassembler.h"

int main(void) {
    printf("%x %x\n\n", 0x12345678, swap_endian32(0x12345678));

    printf("%d\n", FindCorrespondingMnemonic(123123312));
    printf("%d\n", FindCorrespondingMnemonic(1233636));
    printf("%d\n", FindCorrespondingMnemonic(232612));
    printf("%d\n", FindCorrespondingMnemonic(34323129));
    printf("%d\n", FindCorrespondingMnemonic(0xafc40020));
    printf("%d\n", FindCorrespondingMnemonic(0x0c100148));
    printf("%d\n", FindCorrespondingMnemonic(0x8c63000c));
    printf("%d\n", FindCorrespondingMnemonic(0x27bdff20));
    printf("%d\n", FindCorrespondingMnemonic(0x00200825));
    printf("%d\n", FindCorrespondingMnemonic(0x00402021));
    printf("%d\n", FindCorrespondingMnemonic(0x00200825));
    printf("%d\n", FindCorrespondingMnemonic(0x00002821));
    printf("%d\n", FindCorrespondingMnemonic(0x00403021));

    return 0;
}


