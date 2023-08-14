# The challnge 
```
fd@pwnable:~$ cat fd.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char buf[32];
int main(int argc, char* argv[], char* envp[]){
        if(argc<2){
                printf("pass argv[1] a number\n");
                return 0;
        }
        int fd = atoi( argv[1] ) - 0x1234;
        int len = 0;
        len = read(fd, buf, 32);
        if(!strcmp("LETMEWIN\n", buf)){
                printf("good job :)\n");
                system("/bin/cat flag");
                exit(0);
        }
        printf("learn about Linux file IO\n");
        return 0;

}
```




# Solution 

## explaination : 
 as you can see we just open the fd that got in the argv[1] - 0x1234 and then read from it - so I wanted to read from stdin ( fd - 0 )
 so I entered in argv[0] - 0x1234 and in the stdin through pipe I inserted the stringed it comparing to  - LETMEWIN - simple shit 



## code 
```
fd@pwnable:~$ echo -en "LETMEWIN\n" |./fd 4660
good job :)
mommy! I think I know what a file descriptor is!!

```
