

a = float(input("Inserte límite a: "))        #PEDIMOS LOS VALORES AL CLIENTE
b= float(input("Inserte límite b: "))
n = float(input("inserte numero de rectangulos n: "))
x = a
area = 0
xintervalo = a  #DEFINIMOS DONDE EMPIEZA (X)

base = (b - a)/n        #LA BASE VA A SER SIEMPRE LA MISMA (FUERA DEL BUCLE)
#INTEGRAL = (X^3)/3
#SOLUCION ANALITICA
sol_analitica = (((b*b*b)/3) - ((a*a*a)/3))

while xintervalo <= b:
    h = (xintervalo*xintervalo) #altura del rectangulo = posicion de x ^2
    area = area + (base * h)   #SUMA SUCESIVA DE LOS RECTANGULOS OBTENIDOS Y SU OBTENCION
    xintervalo = xintervalo + base  #sumamos la base para la proxima operacion (DEFINIR X SIGUIENTE)

error = sol_analitica - area    #determinar el error (diferencia de resultados)


print("Solucion analitica: %.2f" %sol_analitica)
print ("Solucion numerica: %.2f" %area)
print ("Error: %.2f"%error)
print ("")
