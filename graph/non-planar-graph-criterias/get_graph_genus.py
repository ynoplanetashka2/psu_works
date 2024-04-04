from math import ceil

def get_complete_graph_genus(n: int) -> int:
    return ceil((n - 3) * (n - 4) / 12)