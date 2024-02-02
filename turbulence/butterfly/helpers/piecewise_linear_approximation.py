class LinearApproximationArgumentRangeException(Exception):
    pass


def piecewise_linear_approximation(domain, image):
    def approximation(arg):
        if arg <= 0:
            raise LinearApproximationArgumentRangeException('аргумент вышел за границы')
        for index, domain_value in enumerate(domain):
            if arg <= domain_value:
                if index + 1 >= len(domain):
                    raise LinearApproximationArgumentRangeException('аргумент вышел за границы')
                shift_coefficient = (arg - domain[index]) / (domain[index + 1] - domain[index])
                result = (image[index + 1] - image[index]) * shift_coefficient + image[index]
                return result
        raise LinearApproximationArgumentRangeException('аргумент вышел за границы')

    return approximation