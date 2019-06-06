"""
'Stupid' script for creating binaries from an hex string
(example: you have a .txt file with an hex sequence,
i.e. 18fe00080100080404080705080805080,and you want to encode that
sequence into the file itself instead of considering it as ascii)
Created by: regi18
Version: 1.1.0
Github: https://github.com/regi18/hexascii2bin
"""

from sys import argv

dump = ""
inputfile = ""
outputfile = "hex.bin"

if len(argv) == 1:
    print("Usage: " + argv[0] + " " + "file" + " [output file]")
elif len(argv) == 2:
    inputfile = argv[1]
elif len(argv) == 3:
    inputfile = argv[1]
    inputfile = argv[2]
else:
    print(argv[0] + ": Invalid arguments")

print("[*] Reading...")

with open("mouse.dump") as f:
    dump = f.read()

with open("hex.bin", "wb") as f:
    f.write(bytes.fromhex(dump))

print("[+] Done!")
