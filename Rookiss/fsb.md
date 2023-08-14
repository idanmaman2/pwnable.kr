

let's watch the stack for one moment : 
![picture 0](../images/760d6b8fda34ca3c27925d7ad460c1399aaf5c3af985660cfd0d623cd8867b77.png)  

so as you can see we are pushing 0,buf,100 in read
but we clean the stack and when we are calling printf we are overiding the 0 so we have 
![picture 1](../images/976fc845d0cb4d7240b7f2f9d319d5d3bcb288af1a8ba4f9086f0952894ab753.png)  

and from gdb : 
![picture 3](../images/5351bff16a12ec1fba193333ef84b43353b484e35a93ac6c19c761dabf28c6b3.png)  

so as we can see we can mess up with buf as much as we want - but we need to go back !  
so how can we do that ? 


so if we specify something we are getting : buf - as you can see it is address is : 
* key address (always the same - no PIE ) : 0x804a060 <key> : 20B
* buf2 address (always the same-no PIE  ) : 0x804a080 <buf2> : 128B 
* buf address (always the same - no PIE ) : 0x804a100 <buf>

so we want to change the value of 0x804a060
so let's see how we can do that : 
