import numpy as np

def neighbor_joining(dist_matrix, n):
    """
    dist_matrix: A 2D array (n x n) representing the pairwise distances.
    n: The number of taxa.
    Returns: The adjacency list of the resulting phylogenetic tree.
    """

    def compute_q_matrix(dist_matrix, n):
        """
        Compute the Q-matrix used in the neighbor-joining algorithm.
        Q[i][j] = (n-2) * D[i][j] - sum(D[i,k] for all k) - sum(D[j,k] for all k)
        """
        Q = np.zeros((n, n))
        row_sums = np.sum(dist_matrix, axis=1)
        for i in range(n):
            for j in range(i + 1, n):
                Q[i][j] = (n - 2) * dist_matrix[i][j] - row_sums[i] - row_sums[j]
                Q[j][i] = Q[i][j]
        return Q

    def find_closest_pair(Q_matrix, n):
        """
        Find the closest pair (i, j) based on the Q-matrix.
        """
        min_val = float('inf')
        pair = (-1, -1)
        for i in range(n):
            for j in range(i + 1, n):
                if Q_matrix[i][j] < min_val:
                    min_val = Q_matrix[i][j]
                    pair = (i, j)
        return pair

    # Initial tree with n leaves.
    tree = {i: [] for i in range(n)}

    # Start with a set of all taxa.
    taxa = list(range(n))
    
    # Repeat until there are only 2 taxa left.
    while len(taxa) > 2:
        Q_matrix = compute_q_matrix(dist_matrix, len(taxa))

        # Find the closest pair of taxa.
        i, j = find_closest_pair(Q_matrix, len(taxa))

        # Calculate the branch lengths for i and j.
        d_ij = dist_matrix[i][j]
        dist_to_new_node_i = (d_ij / 2) + ((np.sum(dist_matrix[i]) - np.sum(dist_matrix[j])) / (2 * (len(taxa) - 2)))
        dist_to_new_node_j = d_ij - dist_to_new_node_i

        # Add new node to the tree.
        new_node = len(tree)
        tree[new_node] = []
        tree[i].append((new_node, dist_to_new_node_i))
        tree[j].append((new_node, dist_to_new_node_j))

        # Calculate distances from the new node to all other taxa.
        new_distances = []
        for k in range(len(taxa)):
            if k != i and k != j:
                new_distances.append((dist_matrix[i][k] + dist_matrix[j][k] - d_ij) / 2)

        # Remove taxa i and j, add new node.
        
        taxa.remove(j)
        if i in taxa:
          taxa.remove(i)
        taxa.append(new_node)

        # Update the distance matrix.
        new_dist_matrix = np.zeros((len(taxa), len(taxa)))
        for k in range(len(new_distances)):
            new_dist_matrix[k, len(taxa) - 1] = new_distances[k]
            new_dist_matrix[len(taxa) - 1, k] = new_distances[k]

        dist_matrix = new_dist_matrix

    # Connect the last two taxa.
    tree[taxa[0]].append((taxa[1], dist_matrix[0, 1]))
    tree[taxa[1]].append((taxa[0], dist_matrix[0, 1]))

    return tree

# Example usage
dist_matrix = np.array([
    [0, 5, 9, 9, 8],
    [5, 0, 10, 10, 9],
    [9, 10, 0, 8, 7],
    [9, 10, 8, 0, 3],
    [8, 9, 7, 3, 0]
])

n = len(dist_matrix)
result_tree = neighbor_joining(dist_matrix, n)
for node, edges in result_tree.items():
    for (neighbor, weight) in edges:
        print(f"Edge: {node} -> {neighbor}, Weight: {weight:.2f}")
