'''
    Reto: 

        Eres un desarrollador junior en una empresa de software, y te han asignado la tarea de crear un
        programa que calcule el costo total de una compra en una tienda. El programa debe interactuar con
        el usuario a través de la consola, solicitando cuatro datos esenciales: 
        el nombre del producto, 
        el precio unitario, 
        la cantidad de productos adquiridos
        el porcentaje de descuento que se aplicará si es que existe alguno. 
        

        Es fundamental que el programa maneje adecuadamente las entradas,
        validando que tanto el precio como la cantidad sean números positivos, y que el descuento esté
        dentro del rango aceptable de 0 a 100%.


        Con estos datos, el programa debe calcular el costo total de la compra. 
        Primero, debe determinar el costo sin aplicar ningún descuento y,
        luego, si corresponde, aplicar el descuento especificado para calcular el monto final. 
        Además, este costo total debe ser mostrado junto con el nombre del producto, de manera clara y formateada, asegurando que el resultado sea fácil de interpretar, por
        ejemplo, presentando el valor con dos decimales.


    
        Es importante que consideres la estructura y legibilidad de tu código, asegurándote de que esté
        bien organizado y libre de errores. Por último, prueba el programa con distintos escenarios,
        incluyendo casos extremos, para garantizar que funcione correctamente en todas las situaciones
        posibles.

'''
'''
entrada 
 
 - nombre_producto
 - precio_producto
 - cantidad
 - % descuento

Ejecucion

    - calcular costo totla de la compra
    - costo sin apilicar descuento 
    - consto aplicando el descuento 
    - mostrar el costo con el nombre del producto con 2 decimales 


requerimientos

    - validar que el precio y cantidades sean positivas
    - que el descuento este entre el 0 y  100%
    - aplicar costo si el producto lo tiene 
    - hacer ensayos incluyento casos extremos 

'''

date= "si"
while ("si" in date):
    while True:
        productName = input("\v\tpor favor ingresar nombre del producto: ")
        if(productName.isalpha()):
            break
        print("\t\tError")


    while True:

        productPrice=input("\v\tPor favor ingrese el valor del producto: ")
        if(productPrice.isnumeric()):
            productPrice = float(productPrice)
            if(productPrice > 0 ):
                break
            else:
                print( "\t\tEl valor tiene que ser superiro a 0!")
                continue
        print("\t\tError tiene que ser un numero ")


    while True:

        productQuantity = input("\v\tpor favor ingresar la cantidad de producto ")
        if(productQuantity.isnumeric()):
            productQuantity = int(productQuantity)
            if(productQuantity > 0 ):
                break
            else:
                print( "\t\tEl valor tiene que ser superiro a 0!")
                continue
        print("Error tiene que ser un numero ")


    if (productQuantity >=12):
        #aplicar descuento 
        while True:
                discountPercentage = input("v\t\por favor ingresar el /%/ de descuento ")
                if(discountPercentage.isnumeric()):
                    discountPercentage = float(discountPercentage)
                    if(discountPercentage> 0 and discountPercentage <= 100):
                        break
                    else:
                        print( "\t\tEl valor tiene que ser entre 0 a 100%")
                        continue
                print("\t\tError tiene que ser un numero ")
    else:
        print("Para aplicar decuento necesita mas de 12 productos ")
        discountPercentage = 0.0 



    print(f"nombre del producto {productName}, precio del porducto por unidad {productPrice}, cantidad de producto {productQuantity} descuento aplicado {discountPercentage}")

    date=input("Deseas continuar con otro producto : si / no:  ")