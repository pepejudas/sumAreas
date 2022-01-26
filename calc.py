import sympy

print("ingrese el valor  del intervalo inicial")
#nombre = input()
a = input()
a = int(a)
print("ingrese el valor  del intervalo final")
#nombre=input()
b = input()
b = int(b)
print("desea ingresar el numero de diviones del intervalo?") 
c = input()

if c == "no": 
    d = 10000
else: 
    print( "ingrese el valor de divisiones") 
    d = input()
    d = int(d)

dx = (b-a)/d

print("ingrese la funcion")
funcion = input()

def evalfuncion(f,i):
    #sympy.init_printing()
    #x = sympy.symbols('x')
    Poly2 = sympy.Poly(f)
    w = Poly2.eval(i)
    print("i="+str(i))
    print("f(i)="+str(w))

    return w

area = 0 
ax = a
cont = 0

while ax <= b:
    m = evalfuncion(funcion,ax)
    v = m * dx
    area += v
    ax += dx

    print("contador:"+str(cont))
    print("ax:"+str(ax))
    print("area:"+str(area))

    cont+=1

print("el area bajo la curva del intervalo es:")
print(area)
