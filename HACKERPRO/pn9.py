num1=int(input("ingresa el primer número"))
num2=int(input("ingresa el seundo número"))
while True:
    print("""opciones:
    1) suma
    2) resta
    3) salir""")
    opcion=int(input("ingresa la operacion a realizar"))
    if opcion == 1:
        print("la suma es: ", num1 + num2)
    elif opcion==2:
        print("la resta es: ", num1 - num2)
    elif opcion==3:
        print("vuelva a ingresar valores")
    break