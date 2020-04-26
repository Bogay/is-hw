#include <stdio.h>
#include <stdlib.h>
#define KEYSIZE 32 // 256 bits

int main()
{
    unsigned char key[KEYSIZE];
    // read random bytes
    FILE *random = fopen("/dev/urandom", "r");
    fread(key, sizeof(unsigned char) * KEYSIZE, 1, random);
    fclose(random);
    // print key
    for (int i = 0; i < KEYSIZE; i++)
        printf("%.2x", key[i]);
    puts("");
    return 0;
}