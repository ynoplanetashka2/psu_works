# def teta_basis(x):
#     return x * (1 - x)


# def dd_teta_basis(x):
#     return np.full(x.shape, -2)


# def w_basis(x):
#     return x**2 * (1 - x**2)


# def dd_w_basis(x):
#     return 2 - 4 * 3 * x**2


# def dddd_w_basis(x):
#     return np.full(x.shape, 4 * 3 * 2 * 1)


# def L(w_args, teta, k, Ra_c):
#     (dddd_w, dd_w, w) = w_args
#     return dddd_w - 2 * k**2 * dd_w + k**4 * w - Ra_c * k**2 * teta


# def M(w, teta_args, k):
#     (dd_teta, teta) = teta_args
#     return dd_teta - k**2 * teta + w


# def a_part_in_L(w_args, k):
#     (dddd_w, dd_w, w) = w_args
#     return dddd_w - 2 * k**2 * dd_w + k**4 * w


# def b_part_in_L(teta, k, Ra_c):
#     return -Ra_c * k**2 * teta


# def a_part_in_M(w):
#     return w


# def b_part_in_M(teta_args, k):
#     (dd_teta, teta) = teta_args
#     return dd_teta - k**2 * teta

    
    
    # exit()
    # domain = np.linspace(0, 1, 100)
    # domain_step = domain[1]
    # teta_basis_values = teta_basis(domain)
    # dd_teta_basis_values = dd_teta_basis(domain)
    # w_basis_values = w_basis(domain)
    # dd_w_basis_values = dd_w_basis(domain)
    # dddd_w_basis_values = dddd_w_basis(domain)
    # K_VALUE = 2
    # RA_C = 1_500

    # a_coeff_in_L = np.linalg.multi_dot(
    #     [
    #         a_part_in_L(
    #             (dddd_w_basis_values, dd_w_basis_values, w_basis_values), K_VALUE
    #         )
    #         * domain_step,
    #         w_basis_values,
    #     ]
    # )
    # b_coeff_in_L = np.linalg.multi_dot(
    #     [b_part_in_L(dd_teta_basis_values, K_VALUE, RA_C) * domain_step, w_basis_values]
    # )
    # a_coeff_in_M = np.linalg.multi_dot(
    #     [a_part_in_M(w_basis_values) * domain_step, teta_basis_values]
    # )
    # b_coeff_in_M = np.linalg.multi_dot(
    #     [
    #         b_part_in_M((dd_teta_basis_values, teta_basis_values), K_VALUE)
    #         * domain_step,
    #         teta_basis_values,
    #     ]
    # )
    # a_and_b_coefficients_equation_matrix = np.array(
    #     [[a_coeff_in_L, b_coeff_in_L], [a_coeff_in_M, b_coeff_in_M]]
    # )
    # a_coeff, b_coeff = np.linalg.solve(
    #     a_and_b_coefficients_equation_matrix,
    #     np.array([0, 0]),
    # )
    # print(a_coeff, b_coeff)
    # print(np.linalg.det(a_and_b_coefficients_equation_matrix))
