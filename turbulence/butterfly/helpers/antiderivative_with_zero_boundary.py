from helpers.integrate import integrate


def antiderivative_with_zero_boundary(domain, image):
    sorted_values = sorted(zip(domain, image), key=lambda x: x[0])
    sorted_domain = list(map(lambda x: x[0], sorted_values))
    sorted_values = list(map(lambda x: x[1], sorted_values))
    intermidiate_values = [
        integrate(sorted_domain[i:], sorted_values[i:])
        for i in range(1, len(sorted_values))
    ]
    return (sorted_domain[1:], intermidiate_values)
