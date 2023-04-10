from collections import defaultdict

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskalMST(adj_matrix):
    num_vertices = len(adj_matrix)
    parent = []
    rank = []
    for v in range(num_vertices):
        parent.append(v)
        rank.append(0)
    mst = []
    edges = []
    for i in range(num_vertices):
        for j in range(i+1, num_vertices):
            edges.append((i, j, adj_matrix[i][j]))
    edges.sort(key=lambda x: x[2])
    for edge in edges:
        u, v, weight = edge
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            mst.append(edge)
            union(parent, rank, x, y)
    return mst

def read_adj_matrix_from_file(file_path):
    adj_matrix = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            row = [float(val) for val in line.strip().split(',')]
            adj_matrix.append(row)
    return adj_matrix

def write_mst_to_file(file_path, mst):
    with open(file_path, 'w') as file:
        for edge in mst:
            file.write(f"{edge[0]} - {edge[1]}: {edge[2]}\n")


if __name__ == "__main__":
    file_path = "test.txt"
    adj_matrix = read_adj_matrix_from_file(file_path)
    mst = kruskalMST(adj_matrix)
    write_mst_to_file("mst.txt", mst)
    print("Minimum Spanning Tree written to mst.txt")
