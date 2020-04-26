#include "gen_key.h"
#include <stdio.h>

int main()
{
    unsigned int seed;
    scanf("%u", &seed);
    char *key = gen_key(seed);
    for (int i = 0; i < KEYSIZE; i++)
        printf("%.2x", (unsigned char)key[i]);
    return 0;
}