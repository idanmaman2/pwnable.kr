a="""3\rG[S/%\x1c\x1d#0?\rIS\x0f\x1c\x1d\x18;,4\x1b\x00\x1bp;5\x0b\x1b\x08\x45+"""
b="cat: password: Permission denied\n"
for i,j in zip(a.encode(),b.encode()):
    print(chr(i^j), end="")