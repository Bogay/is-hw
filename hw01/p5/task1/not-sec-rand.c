#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define KEYSIZE 16

char *gen_key(unsigned int seed)
{
    srand(seed);
    char *key = malloc(KEYSIZE);
    for (int i = 0; i < KEYSIZE; i++)
        key[i] = rand() % 256;
    return key;
}

int main()
{
    int i;
    char key[KEYSIZE];

    printf("%lld\n", (long long)time(NULL));
    srand(time(NULL));

    for (i = 0; i < KEYSIZE; i++)
    {
        key[i] = rand() % 256;
        printf("%.2x", (unsigned char)key[i]);
    }
    puts("");

    return 0;
}
