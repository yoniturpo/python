lista = ["febrero","marzo"]
cantidad=int(input("cantidad de productos a ingresar"))
for i in range(cantidad):
    producto=input("ingresa el producto")
    lista.append(producto)
print(lista)