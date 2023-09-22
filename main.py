from binary_con import binary_con
from pyfiglet import print_figlet


# user interface to get the user input and provide output
# your code here!
while True:
    print('             *ੈ✩‧₊˚༺☆༻*ੈ✩‧₊˚ ')
    print("Welcome To Binary and Decimal Conversion")
    print("Enter ❗bd❗ To Convert Binary To Decimal OR ❗db❗ To Convert Decimal To Binary")
    print('          ♡❀˖⁺. ༶ ⋆˙⊹❀♡')
    opt = input("💭 Choose your option(bd/db): ")
    value = (input("🧮 Enter Number You Want To Convert: "))

    print(f"🔎 The Result After Coversion is 👉{binary_con(opt, value)}👈") 
    print('-----------------------------------------------------------')
    decision = input("Do You Want To Continue Using The App?🤔(y/n): ")
    print('-----------------------------------------------------------')
    False
    if decision == 'y':
        True
    elif decision == 'n':
        print('Thank You For Using Our App! Have A Good Day!🥰🥰')
        print(print_figlet('Thank   You!!', font ='isometric3', colors = 'BLUE'))
        break

 