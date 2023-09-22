import math
# while True:
#     print("")
#     print("Welcome To Binary and Decimal Conversion")
#     print("Enter 'bd' To Convert Binary To Decimal OR 'db' To Convert Decimal To Binary")
#     opt = input("Choose your option(bd/db): ")
#     value = (input("Enter Number You Want To Convert: "))
def binary_con(opt, value):
    if opt == 'db' and value:
        x = (bin(int(value)))[2:]
        return int(x)
            
    elif opt == 'bd' and value:
        # value = str
        l = list(str(value))
            # dic = 0
            # value = str(value)
        sum = 0
        l.reverse()
        for i in range(len(l)) :
            sum = sum + int(l[i])*2**i
                # dic = dic*2 + int(i)
        return(sum)
    elif opt != 'db' or opt!='bd':
        print("CHECK YOUR OPTION AGAIN!")
        print("PLEASE MAKE SURE TO ENTER A CORRECT OPTION")
        False
 
   


















'''
    @param opt: 'bd' or 'db', binary to decimal or decimal to binary
    @param value: the value to be converted, integer
    @return: the converted value

    example binary_con('bd', 1001) should return 9 as int value, and binary_con('db', 8) should return 1000 as int.
    '''
...
