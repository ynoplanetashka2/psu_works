from math import floor

def get_complete_graph_thickness(verticesCount: int) -> int:
    return floor((verticesCount + 7) / 6)
