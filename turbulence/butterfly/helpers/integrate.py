def integrate(domain, image):
    integral_sum = 0
    sorted_values = sorted(zip(domain, image), key=lambda x: x[0])
    (prev_x, prev_y) = sorted_values[0]
    for x, y in sorted_values[1:]:
        delta_x = x - prev_x
        y_mid = (y + prev_y) / 2
        integral_sum += delta_x * y_mid
        (prev_x, prev_y) = (x, y)
    return integral_sum
