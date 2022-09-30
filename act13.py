import sys
from random import randint
num_aleatori = randint(1,101)

num=-1

while True:
    num = (input("Introduix de l'1 al 100: "))
    if num>num_aleatori :
        raise Exception("Error massa gran")
    elif num<num_aleatori:
        raise Exception("Error masa menuf")
    elif num.isnumeric==False:
        raise Exception("Error no es un número")
    elif num==num_aleatori:
        print("Encertat")
        break
    
