H_e = 1.016
H_c = 0.984

def star_pulsing_for_n(n):
    def star_pulsing_equation(r, r_prime):
        if r_prime >= 0:
            return H_e / r**n - 1 / r**2
        else:
            return H_c / r**n - 1 / r**2
    return star_pulsing_equation
