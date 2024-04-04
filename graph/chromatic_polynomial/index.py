import networkx as nx

def main():
    edges_to_add = (
        (0, 4),
        (0, 5),
        (0, 1),
        (0, 2),
        (1, 3),
        (1, 2),
        (2, 3),
        (3, 4),
        (3, 5),
    )
    graph = nx.Graph(edges_to_add)
    poly = nx.chromatic_polynomial(graph)
    def eval_poly(x: float):
        return poly.subs("x", x).evalf()

    print(f"{poly=}")
    for i in (2, 3, 4, 5):
        poly_value = eval_poly(i)
        print(f"poly({i}) = {poly_value=}")
    
    greedy_color = nx.greedy_color(graph)
    available_colors = ("green", "red", "blue")
    res = { f"x{v + 1}": available_colors[c] for v, c in greedy_color.items() }
    print(res)

if __name__ == "__main__":
    main()