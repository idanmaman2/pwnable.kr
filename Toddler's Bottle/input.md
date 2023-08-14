```
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include <fcntl.h>
int main(){ 
        char *  payload[100] ;
        char * payload2[2];
        for(size_t i = 0 ; i < 100 ; i++){payload[i]="";}
        payload['B'] = "\x20\x0a\x0d";
        payload['A'] = "\x00";
        payload[100] = NULL; 
        // stag2 
        write(0, "\x00\x0a\x00\xff" , 4 );
        write(2,"\x00\x0a\x02\xff" , 4 );
        
        //stag3 
        payload2[0] = "\xde\xad\xbe\xef=\xca\xfe\xba\xbe";
        payload2[1]=NULL; 
        //stag4
        int fd3 = open("\x0a",O_RDWR) ; 
        write(fd3 , "\x00\x00\x00\x00" , 4 );
        close(fd3); 
        //stage5
        payload['C']  = "3333"; 
 
	    printf("runing!!!");
	    execv("/home/input2/input",payload); 
        return 0;
}

```

```
./a.out > out& 
echo -en \xde\xad\xbe\xef| nc 0 3333
```