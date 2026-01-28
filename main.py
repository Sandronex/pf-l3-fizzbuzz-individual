numero = 1
while numero <= 1000:
    if numero % 3 == 0:
        print("Fizz", numero)
        if numero % 5 == 0:
            print ("Buzz", numero) 
            if numero % 3 == 0 and numero % 5 == 0:
                print ("FizzBuzz")
                

    numero = numero + 1