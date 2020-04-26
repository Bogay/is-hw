#include <stdio.h>
#include <openssl/bn.h>

BIGNUM *hex_new(const char *val)
{
    BIGNUM *r = BN_new();
    BN_hex2bn(&r, val);
    return r;
}

int main()
{
    BN_CTX *ctx = BN_CTX_new();
    // p - 1
    BIGNUM *p = hex_new("F7E75FDC469067FFDC4E847C51F452DE");
    BN_sub_word(p, 1);
    // q - 1
    BIGNUM *q = hex_new("E85CED54AF57E53E092113E62F436F4F");
    BN_sub_word(q, 1);
    // phi(n) = (p-1) * (q - 1)
    BIGNUM *phi_n = BN_new();
    BN_mul(phi_n, p, q, ctx);
    // d = e ^ -1 (mod phi(n))
    BIGNUM *e = hex_new("0D88C3");
    BIGNUM *d = BN_mod_inverse(NULL, e, phi_n, ctx);
    // print
    char *d_str = BN_bn2dec(d);
    printf("d = %s\n", d_str);
    OPENSSL_free(d_str);
    return 0;
}