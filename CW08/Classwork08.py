#Classwork 08
import math

a = float(input("Enter the left endpoint of the interval "))
b = float(input("Enter the right endpoint of the interval "))

if str(a).lower() == "pi":
    a = math.pi
else: a = float(a)
if str(b).lower() == "pi":
    b = math.pi
else:    b = float(b)

f_x = input("Enter the function to integrate (use 'x' as the variable) ")
method = input("Enter the method to use (LRM/RRM/MPM) ")


area = 0.0
n = 1000 
h= (b - a) / n
shift = 0
constant = 0
if method == "RRM":
    shift = 1    
elif method == "MPM":
    constant = h/2
else:
    pass
for i in range(0 + shift, n + shift):
    xi = a + i * h
    height = eval(f_x.replace('x', str(xi)))
    x_i = a + i * h + constant
    area += height * h


print(f"The approximate area under the curve is: {area:.2f}")