# Q: Write a program to implement Min-Max and Alpha-Beta pruning algorithms

def minimax(depth, index, is_max, scores, max_depth):
    if depth == max_depth:
        return scores[index]
    left = minimax(depth + 1, index * 2, not is_max, scores, max_depth)
    right = minimax(depth + 1, index * 2 + 1, not is_max, scores, max_depth)
    return max(left, right) if is_max else min(left, right)

def alphabeta(depth, index, is_max, scores, max_depth, alpha, beta):
    if depth == max_depth:
        return scores[index]

    for i in range(2):
        val = alphabeta(depth + 1, index * 2 + i, not is_max, scores, max_depth, alpha, beta)
        if is_max:
            alpha = max(alpha, val)
        else:
            beta = min(beta, val)
        if beta <= alpha:
            break
    return alpha if is_max else beta

# Example input: depth 3 (8 leaves)
scores = [3, 5, 6, 9, 1, 2, 0, -1]
depth = 3

print("Minimax Optimal Value:", minimax(0, 0, True, scores, depth))
print("Alpha-Beta Optimal Value:", alphabeta(0, 0, True, scores, depth, float('-inf'), float('inf')))
