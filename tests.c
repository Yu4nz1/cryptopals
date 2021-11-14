/*********************************************************************
* Copyright (c) 2016 Jonas Schnelli                                  *
* Distributed under the MIT software license, see the accompanying   *
* file COPYING or http://www.opensource.org/licenses/mit-license.php.*
**********************************************************************/

#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>

#include "chacha.h"



/*
   Testvectors have been taken from the draft RFC
   https://tools.ietf.org/html/draft-agl-tls-chacha20poly1305-04#section-7
*/

void show(uint8_t* s,int len){
    printf("len:%d\n",strlen(s));
    for(int i=0;i<len;i++){
        printf("%c",s[i]);
    }
    printf("\n");
}

int main(void)
{
    struct chacha_ctx ctx;
    uint8_t iv[8] = "dotitsit";
	//uint8_t iv[8] = {0,0,0,0,0,0,0,0};
    unsigned int i = 0;
    uint8_t keystream[32]= 
	{
    0xEB, 0x8E, 0x5C, 0xA5, 0x62, 0xB4, 0x1C, 0x84, 0x5C, 0x59, 0xFC, 0x0D, 0x43, 0x3C, 0xAB, 0x20, 
    0xD8, 0x93, 0x33, 0x13, 0xA1, 0x9E, 0x39, 0x00, 0x76, 0x14, 0xB5, 0x04, 0x58, 0x9D, 0x06,0xb8
};
    unsigned char* flag=(unsigned char*)malloc(0x40);
    memset(flag,0,0x40);
    memcpy(flag,keystream,32);
    const uint8_t key[32]={0x30,0x4E,0x33,0x40,0x61,0x59,0x49,0x5F,0x4D,0x33,0x6C,0x30,0x64,0x79,0x5F,0x4B,0x75,0x72,0x4F,0x6D,0x31,0x5F,0x57,0x5F,0x53,0x75,0x6B,0x31,0x64,0x71,0x79,0x30};
    /* test chacha20 */
    
    chacha_ivsetup(&ctx, iv, NULL);
    chacha_keysetup(&ctx, key);
    chacha_encrypt_bytes(&ctx, flag, flag, 32);
    show(flag,32);
}


