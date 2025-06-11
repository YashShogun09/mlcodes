def build_tree(leaves, branching_factor):
   
    if len(leaves) <= branching_factor:
        return leaves  # Smallest group — base case

    tree = []
    for i in range(0, len(leaves), branching_factor):
        subtree = build_tree(leaves[i:i + branching_factor], branching_factor)
        tree.append(subtree)
    return tree

def alpha_beta(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or isinstance(node, int):
        return node

    if maximizing_player:
        max_eval = float('-inf')
        for child in node:
            eval = alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  
        return max_eval
    else:
        min_eval = float('inf')
        for child in node:
            eval = alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  
        return min_eval


def main():
    try:
        depth = int(input("Enter the depth of the tree (e.g. 2): "))
        branching_factor = int(input("Enter the branching factor (e.g. 3): "))
        num_leaves = branching_factor ** depth
        print(f"You need to enter {num_leaves} leaf node values (space separated):")
        leaves = list(map(int, input().split()))

        if len(leaves) != num_leaves:
            print(f"Error: You must enter exactly {num_leaves} integers.")
            return

        tree = build_tree(leaves, branching_factor)
        result = alpha_beta(tree, depth, float('-inf'), float('inf'), True)
        print("\nOptimal value using Alpha-Beta Pruning:", result)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
