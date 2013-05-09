#converter.py
#convert numbers into different bases

import math
dec_hex_map={0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:'A',11:'B',12:'C'
             ,13:'D',14:'E',15:'F'}
hex_dec_map={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
             'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    
def dec_to_bin():
    decnum = int(input("enter decimal number"))
    binnum = ""
    while decnum != 0:
        remainder = decnum % 2
        binnum = str(remainder) + binnum
        decnum = decnum // 2
    return binnum
    
def dec_to_oct():
    decnum = int(input("enter decimal number"))
    octnum = ""
    while decnum != 0:
        remainder = decnum % 8
        octnum = str(remainder) + octnum
        decnum = decnum // 8
    return octnum    

def dec_to_hex():

    decnum = int(input("enter decimal number"))
    hexnum = ""
    while decnum != 0:
        remainder = decnum % 16
        hexnum = str(dec_hex_map[remainder]) + hexnum
        decnum = decnum // 16
    return hexnum  

def bin_to_oct():
    binnum = str(input("enter binary number"))
    i = 0
    octnum = ''
    decnum = 0
    while i < len(binnum):
        decnum = decnum + (int(binnum[i])) * (2**(len(binnum)-1-i))
        i = i +1
    while decnum != 0:
        remainder = decnum % 8
        octnum = str(remainder) + octnum
        decnum = decnum // 8
    return octnum  
    
def bin_to_dec():
    binnum = str(input("enter binary number"))
    i = 0
    decnum = 0
    while i < len(binnum):
        decnum = decnum + (int(binnum[i])) * (2**(len(binnum)-1-i))
        i = i +1
    return decnum
    
def bin_to_hex():
    binnum = str(input("enter binary number"))
    i = 0
    decnum = 0
    hexnum = ""
    while i < len(binnum):
        decnum = decnum + (int(binnum[i])) * (2**(len(binnum)-1-i))
        i = i +1   
    while decnum != 0:
        remainder = decnum % 16
        hexnum = str(dec_hex_map[remainder]) + hexnum
        decnum = decnum // 16
    return hexnum  
    
def oct_to_bin():
    octnum = str(input("enter octnum"))
    i = 0
    decnum = 0
    binnum = ""
    while i < len(octnum):
        decnum = decnum + (int(octnum[i])) * (8**(len(octnum)-1-i))
        i = i +1
    
    while decnum != 0:
        remainder = decnum % 2
        binnum = str(remainder) + binnum
        decnum = decnum // 2
    return binnum
    
def oct_to_dec():
    octnum = str(input("enter octnum"))
    i = 0
    decnum = 0
    while i < len(octnum):
        decnum = decnum + (int(octnum[i])) * (8**(len(octnum)-1-i))
        i = i +1
    return decnum
    
def oct_to_hex():
    octnum = str(input("enter octnum"))
    i = 0
    decnum = 0
    hexnum = ""
    while i < len(octnum):
        decnum = decnum + (int(octnum[i])) * (8**(len(octnum)-1-i))
        i = i +1
        
    while decnum != 0:
        remainder = decnum % 16
        hexnum = str(dec_hex_map[remainder]) + hexnum
        decnum = decnum // 16
    return hexnum  
    
def hex_to_bin():
    hexnum = (input("enter hexadecimal number")).upper()
    i = 0
    decnum = 0
    binnum = ""
    while i < len(hexnum):
        decnum = decnum + int((hex_dec_map[hexnum[i]]) * (16**(len(hexnum)-1-i)))
        i = i + 1
    
    while decnum != 0:
        remainder = decnum % 2
        binnum = str(remainder) + binnum
        decnum = decnum // 2
    return binnum
    
def hex_to_oct():
    hexnum = (input("enter hexadecimal number")).upper()
    i = 0
    decnum = 0
    octnum = ""
    while i < len(hexnum):
        decnum = decnum + int((hex_dec_map[hexnum[i]]) * (16**(len(hexnum)-1-i)))
        i = i + 1
        
    while decnum != 0:
        remainder = decnum % 8
        octnum = str(remainder) + octnum
        decnum = decnum // 8
    return octnum   
        
def hex_to_dec():

    hexnum = (input("hexadecimal number")).upper()
    i = 0
    decnum = 0
    while i < len(hexnum):
        decnum = decnum + int((hex_dec_map[hexnum[i]]) * (16**(len(hexnum)-1-i)))
        i = i + 1
    return decnum

