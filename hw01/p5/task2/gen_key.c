#include "gen_key.h"
#include <stdlib.h>
#include <time.h>

char *gen_key(unsigned int seed)
{
    srand(seed);
    char *key = malloc(KEYSIZE);
    for (int i = 0; i < KEYSIZE; i++)
        key[i] = rand() % 256;
    return key;
}