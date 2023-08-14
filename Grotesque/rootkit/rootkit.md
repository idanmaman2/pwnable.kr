# getting out the bin 
We can download it like fricking losers from the link in or get if by force !!! 
```hexdump -Cv rootkit.ko```
and then I run that script : 
```
all = [] 
for line in x.split("\n"):
    line = line.strip()
    if line == "*": 
        continue
    line = line.partition("|")[0]
    linex = line.partition(" ")[2]
    all += list(map(bytearray.fromhex , linex.split(" ")))

data = reduce(lambda x ,y : x+y , all) 
print(*data,sep="\n")
with open("rootkit.ko", 'wb') as file : 
    file.write(data)
```
where x is the stdout I copied from hexdump! 
and that is it . 
we have the bin : 
![picture 24](../../images/8eaa3cf5f0b4a2f422111f457e79cc82da545468dc23598953edd1bced352afd.png)  

# let watch the ida code 

![picture 4](../../images/01c223b27f2bca445189fb0d576313ac39be32d0e043e951954bb6c79449443f.png)  
![picture 9](../../images/ba1931dd412af3ab3507b38b9ea330dcf5468aa45f7c81020a969e997ebdb1f2.png)  
![picture 5](../../images/1dab02212293dce7778d77c831db3677540e46c2d3ad0e0136f1d8cce6c83b6d.png)  
![picture 0](../../images/ba1931dd412af3ab3507b38b9ea330dcf5468aa45f7c81020a969e997ebdb1f2.png)  
and as we can see -> hex(5 * 4(size of entry)) = 20
so that is pretty neat 

and we can see that it is done to the rest : 
![picture 6](../../images/96e7dc62794c0c48da218bcf43f63c3d09d96dddc0f5528f3a2ef05c6bacb1f4.png)  

* syscall table base: 0C15FA020
* 0C15FA4BCh = base + 0x49c = entry 295 
![picture 12](../../images/4a31e067730d7b9629ea827408762c5743950b34b71a8279967927303a291331.png)  

* 0C15FA16Ch = base + 0x14c = entry 83 
![picture 11](../../images/1ce2e2af470e48c647e52af9ea15aac8201772f0f9aae3bc61a7fa0df005c1d7.png)  

* 0C15FA4E0h = base + 0x4c0 = entry 304
![picture 13](../../images/b077f36792045f6dc34120950355c2e57c427fcdc7555c2551fc7a64e7c8ebfa.png)  

* 0C15FA044h = base + 0x24 = entry 9
![picture 7](../../images/7d9f61fc650d9768971503f3cdb1da95147e515027808884a0e024c6a064b4db.png)  

* 0C15FA4DCh = base + 0x4bc = entry 303
![picture 15](../../images/78951487e793e2a99067d2d6c77e80d9f25e082f272a09f37fe337349759a8e7.png)  

* 0C15FA0B8h = base + 0x98 = entry 38
![picture 10](../../images/3753a821ce20f1f334a019760eb50f3943cb5f1f8719d160a6ce36118d42f8e2.png)  

* 0C15FA4D8h = base + 0x4b8 = entry 302 
![picture 14](../../images/815361c23f6ff3085c684a906039b99462f98c723d2c1c5840670eff740e9a7a.png)  

so as we can see I told you some stuff but what about the kaslr ? and how does I know that those address are really true ??? 

so lets answer you  : 
* let use cmdline to check if it is on
![picture 16](../../images/4334ce547a56fb69bd6ae519b4cd5745673b0818bcaacdc45e6fa77a26a5d576.png)  
and lets check one from machine with kaslr : 

![picture 17](../../images/8ec01de420ed24f1d8dc70f57257aab76ae027d0e9c0a02d95b7b31eac01ba19.png)  
![picture 18](../../images/91cd7e0976cadacb404e8111ffcba0dc9de4007627e5a6a51dbfcee291ffbe0d.png)  

for the second question : 
I just printed : `cat /proc/kallsyms`
and searched for intresing stuff - not a big deal at all!!! 

so let continue to dissamble : 
![picture 19](../../images/306110a285efe4660bc2c956027b2c28d40bf8120b185e5d2f603b89e5ec90b7.png)  
as you can see we hook all the functions . 

> note : before and after we call the wp function to set the write protection to the page of she syscall table on and off 
![picture 20](../../images/8e58b95758c091c5de96913c2b3e8b7acdec0cd28eae6da568be033b8cd3452a.png)  

let's analyze in what are the commands : 
![picture 21](../../images/d440cd22203e5d5af0923b884c729bbeee5d89d4d2868a448b0f63813760d3b6.png)  

and the opcodes of the mov on the syscall table are : 
![picture 22](../../images/a7275ccb8183839fd2b92f6ce6e7e91c6de6dc940a43ad15fea758e3c5d17f42.png)  
> note : remmber that the kaslr is not working !!! 
> 
so if we will return the open command to the original one that located in : 
![picture 23](../../images/fb103f908f85591eca3ea4d7cf15544ae700ed1a58411bcbc1d1ca292972686c.png)  
```c1158d70```

and formatted : 

```70 8D 15 C1```

it will return to work normaly 

# The plan  : 
create a new LKM that based on rootkit.ko that will change the open to the original one and then we will be able in theory to run the cat command . 

so let's validate in Ida that the byte sequence of the little endian of the address do not show up any where else
```50 02 00 08```


so let's run a few commands (I recommend to open new ssh session )

so let's patch with ida what we wanted and see the diff 

![picture 26](../../images/4f081b5b1ae965aa73ad6a6e662ef09dfc85fcc4fe79bb709c80514a3b1353ca.png)  

![picture 27](../../images/2ef955e8ab9b9bb9dee4f952f0e141bcd7925e8800844705ef07feef27d507d0.png)  

`A1 34 A0 5F C1`

in

`B8 70 8D 15 C1 `

![picture 28](../../images/aa2ff5b6d4f510cdc351c6ec0135c205b659895edc1d2a5f7dbe5413cf6d5c4e.png)  
![picture 29](../../images/9b238f492987c998b6443c25d214d32cf2b7c239922006bd1119f9b424d0cc23.png)  
![picture 30](../../images/e0393a6e37e075fb22ced5216558c8531967cc61c5e35cef8c39e9864ca8c0fa.png)  



## Commands
```cp rootkit.ko footkit.ko```

```sed -i $'s/\xA1\x34\xA0\x5F\xC1/\xB8\x70\x8D\x15\xC1/g' footkit.ko```

```sed -i 's/root/foot/g' footkit.ko```

```sed -i 's/flag/idan/g' footkit.ko```

```insmod footkit.ko```


and then decompress the file with gzip : 
```
import base64
import gzip

flag="""H4sIAMdtslUAA+3PMQrCQBCF4alzim3tZnY3K3gFO3OCFIlIAoG4It7eNaVFrEIQ/q95DDPFm35s
r7IxLVKMSxbfqRq8mA91sGMyn0RNo5k43brYx+Oe29k5macpr9392v+pS3lruOX8cs2z60qcl+F0
qPZuBgAAAAAAAAAAAAAAAABY8wZDzE0OACgAAA=="""

print(gzip.decompress(base64.b64decode(flag)))
```
# Important Reosurces : 
* [syscall table](https://x86.syscall.sh)
* [ubuntu sec fetures](https://wiki.ubuntu.com/Security/Features)