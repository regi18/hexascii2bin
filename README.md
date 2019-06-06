# hexascii2bin
Script for creating binaries from an hex string. Takes a file with an hex string and creates a new one with those hex values

For Example: you have a .txt file with an hex sequence, e.g. "18fe00080100080404080705080805080", and you want to encode that sequence into the file itself instead of considering it as ascii

usage: hexascii2bin.py file [output file]

# Use case example:
For example, in CTFs, if they stream a file via netcat (or similar) as a hex string, you can use this script to convert it to a binary file.
