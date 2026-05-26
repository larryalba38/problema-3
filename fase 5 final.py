# MODULO / FUNCION: determinar la cantidad exacta a pedir
Definir ("cantidad_a_pedir")

Si stock_actual < stock_minimo Entonces
     cantidad_a_pedir <- stock_minimo - stock_actual
Sino
     cantidad_a_pedir <- 0
FinSi
FinFuncion

# Matriz: datos de invntario (codigo, nombre, stock actual, stock minimo)

    inventatio[0,0] <- "001"; inventario[0,1] <- "cuadernos"; inventario[0,2] <- "12"; inventario[0,3] <- "20"
    inventario[1,0] <- "002"; inventario[1,1] <- "boligrafos"; inventario[1,2] <- "45"; inventario[1,3] <- "30"
    inventario[2,0] <- "003"; inventario[2,1] <- "marcadores"; inventario[2,2] <- "5"; inventario[2,3] <- "15"
    inventario[3,0] <- "004"; inventario[3,1] <- "borradores"; inventario[3,2] <- "8"; inventario[3,3] <- "10"
    inventario[4,0] <- "005"; inventario[4,1] <- "reglas"; inventario[4,2] <- "25"; inventario[4,3] <- "20"

print("==============================================")
print("    LISTA DE PEDIDOS - REABASTECIMIENTO       ")
print("==============================================")
print(f"{'ARTICULO':<20} | {'cantidad a pedir':<15}")
print("----------------------------------------------")

for articulo in inventario: 
     nombre = articulo[1]
     stock_actual = articulo[2]
     stock_minimo = articulo[3]

     # uso del modulo
     cantidad_pedir = calcular_cantidad_a_pedir(stock_actual, stock_minimo)

     # imprimir el resultado
     print(f"{nombre:<20} | {cantidad_pedir:<15}")
           
print("========================================")