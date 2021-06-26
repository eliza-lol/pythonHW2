def solve_quadratic( a, b ,c ):

    import math
    discriminant = b*b-4*a*c
    sDis = math.sqrt(abs(discriminant))

    if discriminant > 0:
        print(int((-b+sDis)/(2*a)))
        print(int((-b-sDis)/(2*a)))

    elif discriminant == 0:
        print(int(-b/(2*a)))
        
    else:
        return None
    


