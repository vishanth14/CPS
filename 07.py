#Finding the roots of a quadratic equation
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

d = b**2 - 4*a*c

if d >= 0:
    r1 = (-b + d**0.5)/(2*a)
    r2 = (-b - d**0.5)/(2*a)
    print("Roots: {:.3f} , {:.3f}".format(r1, r2))
else:
    real = -b/(2*a)
    imag = (-d)**0.5/(2*a)
    print("Roots: {:.3f}+{:.3f}i , {:.3f}-{:.3f}i".format(real, imag, real, imag))