from get_graph_thickness import get_complete_graph_thickness
from get_graph_genus import get_complete_graph_genus

def main():
    n: int = 6
    graph_thickness: int = get_complete_graph_thickness(n)
    graph_genus: int = get_complete_graph_genus(n)
    graph_overlapping_count: int = 3
    coarseness = 1

    print("граф K6")
    print(f" толщина {graph_thickness=};\n род {graph_genus=};\n число скрещиваний {graph_overlapping_count=};\n крупность {coarseness=}")


if __name__ == "__main__":
    main()