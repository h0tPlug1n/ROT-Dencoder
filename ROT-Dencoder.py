print("""


██████╗  ██████╗ ████████╗    ██████╗ ███████╗    ███╗   ██╗ ██████╗ ██████╗ ██████╗ ███████╗██████╗ 
██╔══██╗██╔═══██╗╚══██╔══╝    ██╔══██╗██╔════╝    ████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗
██████╔╝██║   ██║   ██║       ██║  ██║█████╗█████╗██╔██╗ ██║██║     ██║   ██║██║  ██║█████╗  ██████╔╝
██╔══██╗██║   ██║   ██║       ██║  ██║██╔══╝╚════╝██║╚██╗██║██║     ██║   ██║██║  ██║██╔══╝  ██╔══██╗
██║  ██║╚██████╔╝   ██║       ██████╔╝███████╗    ██║ ╚████║╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║
╚═╝  ╚═╝ ╚═════╝    ╚═╝       ╚═════╝ ╚══════╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                                     
""")
rotNum = int(input("Enter your ROT Algorithm Number {1,2,3,...,25}: "))
string = input("Enter the string to decode/encode: ")
d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+rotNum) % 26 + c)

print("".join([d.get(c, c) for c in string]))
