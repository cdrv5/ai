def minimax_pairwise(numbers):
    if len(numbers) == 1:
        return numbers[0]

    min_values = []
    for i in range(0, len(numbers)-1, 2):
        pair_min = min(numbers[i], numbers[i + 1])
        min_values.append(pair_min)
    return max(min_values)
numbers = [3, 5, 1, 9, 2, 7]
print("Max value after pairwise min:", minimax_pairwise(numbers))
