
# escribe un programa en py. que impirma los numeors del 1 al 100 pero siguiendo las siguientes reglas

'''
 - por cada numero divisible por 3, imprime "Fizz"
 - por cada numero d por 5 impirme "Buzz!
 - para los numero d por ambos 3 y 5 imprime "FizzBuzz"
 - si el numero no es fivisible ni por 3 ni por 5 imprime el numero    
 
'''

for i in range(1, 101):
    
    if(i%3 ==0  and i%5 == 0):
        print("FizzBuzz")
    elif(i%3 == 0):
        print("Fizz")
    elif(i%5 == 0):
        print("Buzz")
    else:
        print(i)