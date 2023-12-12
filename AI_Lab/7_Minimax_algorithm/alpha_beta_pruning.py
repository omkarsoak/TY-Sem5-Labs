import math

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth, alpha, beta):

    if curDepth == targetDepth:
        return scores[nodeIndex]

    if maxTurn:
        best = float('-inf')
        for i in range(2):
            val = minimax(curDepth + 1, nodeIndex * 2 + i, False, scores, targetDepth, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                print("Pruned at depth", curDepth + 1, ", nodeIndex", nodeIndex * 2 + i)
                break
        return best

    else:
        best = float('inf')
        for i in range(2):
            val = minimax(curDepth + 1, nodeIndex * 2 + i, True, scores, targetDepth, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                print("Pruned at depth", curDepth + 1, ", nodeIndex", nodeIndex * 2 + i)
                break
        return best

# Driver code
scores = [3, 4, 2, 1, 7, 8, 9, 10, 2, 11, 1, 12, 14, 9, 13, 16]

treeDepth = math.log(len(scores), 2)

print("The optimal value is : ", end="")
print(minimax(0, 0, True, scores, treeDepth, float('-inf'), float('inf')))
