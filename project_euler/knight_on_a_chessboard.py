def knightL(i, j, a, b, n):
    posible_pairs = [(i + a, j + b), (i + a, j - b),
                     (i - a, j + b), (i - a, j - b),
                     (i + b, j + a), (i + b, j - a),
                     (i - b, j + a), (i - b, j - a)]
    moves = {}
    for x in posible_pairs:
        if x[0] < n and x[1] < n and x[0] >= 0 and x[1] >= 0:
            moves[x] = 1
    return moves 

def knight_bfs(a, b, n):
    deq = deque([(0, 0, 0)])
    seen = {(0, 0): 1}
    while deq:
        i, j, t = deq.popleft()
        children = knightL(i, j, a, b, n)
        for child in children:
            if child == (n - 1, n - 1):
                return t + 1
            if child not in seen:
                child_i, child_j = child
                seen[(child_i, child_j)] = 1
                deq.append((child_i, child_j, t + 1))
    return -1

