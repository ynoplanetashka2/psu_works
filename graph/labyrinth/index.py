def index_from_pair(n, i, j):
    return n * i + j

def pair_from_index(n, idx):
    return (idx // n, idx % n)

def compute_connected_component(adj_matrix, start_point=0, connected_component=None):
    if connected_component is None:
        connected_component = [start_point]
    vertex = start_point
    adj_verts = []
    for i, _ in enumerate(adj_matrix):
        if adj_matrix[i][vertex]:
            adj_verts.append(i)
    for v in adj_verts:
        if v not in connected_component:
            connected_component.append(v)
            compute_connected_component(adj_matrix, v, connected_component)
    return connected_component

def compute_sides_count(building_matrix):
    n = len(building_matrix)
    adj_matrix = [[False for _ in range(n**2)] for _ in range(n**2)]
    for i, _ in enumerate(building_matrix):
        for j, _ in enumerate(building_matrix):
            if not building_matrix[i][j]:
                continue
            if i > 0:
                if building_matrix[i - 1][j]:
                    idx0 = index_from_pair(n, i, j)
                    idx1 = index_from_pair(n, i - 1, j)
                    adj_matrix[idx0][idx1] = True
                    adj_matrix[idx1][idx0] = True
            if j > 0:
                if building_matrix[i][j - 1]:
                    idx0 = index_from_pair(n, i, j)
                    idx1 = index_from_pair(n, i, j - 1)
                    adj_matrix[idx0][idx1] = True
                    adj_matrix[idx1][idx0] = True
    connected = compute_connected_component(adj_matrix)
    connected = [pair_from_index(n, v) for v in connected]
    sides_count = 0
    print(connected)
    print(len(connected))
    for vertex in connected:
        idx = index_from_pair(n, *vertex)
        adj_vert_count = len(list(filter(lambda i: adj_matrix[idx][i[0]], enumerate(adj_matrix))))
        sides_count += 4 - adj_vert_count
    return sides_count

SINGLE_SIDE_SPACE = 9
EXTRA_SIDES_COUNT = 4

def main():
    lines_count = int(input())
    lines = []
    for _ in range(lines_count):
        line = input()
        line = [symbol == "." for symbol in line]
        lines.append(line)
    
    sides_count = compute_sides_count(lines)
    space = (sides_count - EXTRA_SIDES_COUNT) * SINGLE_SIDE_SPACE
    print(space)

if __name__ == "__main__":
    main()