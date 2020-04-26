#include <stdlib.h>
#include <time.h>
#include <stdio.h>

#define OUTPUT_SIZE 1048576

int main()
{
    srand(time(NULL));
    FILE *output = fopen("c-output.bin", "wb");
    unsigned char b = 0;
    for (int i = 0; i < OUTPUT_SIZE; i++)
    {
        b = rand() % 256;
        fwrite(&b, 1, 1, output);
    }
    fclose(output);

    return 0;
}