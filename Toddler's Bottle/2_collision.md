
# The challnge : 
```
#include <stdio.h>
#include <string.h>
unsigned long hashcode = 0x21DD09EC;
unsigned long check_password(const char* p){
        int* ip = (int*)p;
        int i;
        int res=0;
        for(i=0; i<5; i++){
                res += ip[i];
        }
        return res;
}

int main(int argc, char* argv[]){
        if(argc<2){
                printf("usage : %s [passcode]\n", argv[0]);
                return 0;
        }
        if(strlen(argv[1]) != 20){
                printf("passcode length should be 20 bytes\n");
                return 0;
        }

        if(hashcode == check_password( argv[1] )){
                system("/bin/cat flag");
                return 0;
        }
        else
                printf("wrong passcode.\n");
        return 0;
}
```





# The soultion 



## code 
Python - to struct the hex 
```
>>> x=struct.unpack(">iiiii" , b"\x08\x77\x42\x7b\x08\x77\x42\x7b\x08\x77\x42\x7b\x08\x77\x42\x7c\xff\xff\xff\xff")
>>> x
(142033531, 142033531, 142033531, 142033532, -1)
>>> sum(x)
568134124
```


I swaped the order of the bytes for each 4 bytes cause little endian ( it writes the argument as char (one by one) so when it reads it as int it fetchs 4 bytes and thinks it little endian - so the order of the bytes is swaped cause of little endian - so I swapped it back ;) ) 
```
echo -en \\x7b\\x42\\x77\\x08\\x7b\\x42\\x77\\x08\\x7b\\x42\\x77\\x08\\x7c\\x42\\x77\\x08
\\xff\\xff\\xff\\xff |xargs ./col
```