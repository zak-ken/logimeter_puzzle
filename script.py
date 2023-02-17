from itertools import chain, combinations
def generate_combinations(original_list):
    """Generate all combinations of elements from the input list.
        Args:
            original_list (list): A list of elements to generate combinations from.

        Returns:
            An iterable object that generates tuples representing combinations of
            elements from the input list. Each tuple contains a subset of the elements
            from the input list, in the order they were originally given.

        Example:
            >>> list(generate_combinations([1, 2, 3]))
            [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
    """

    combination_iterables = []
    for subset_length in range(1, len(original_list)+1):
        combination_iterables.append(combinations(original_list, subset_length))
    return chain.from_iterable(combination_iterables)

population_target = 101000000
population_per_state = [18897109, 12828837, 9661105, 6371773, 5965343, 5926800, 5582170, 5564635, 5268860, 4552402, 4335391, 4296250, 4224851, 4192887, 3439809, 3279933, 3095213, 2812896, 2783243, 2710489, 2543482, 2356285, 2226009, 2149127, 2142508, 2134411]
subset_combinations = generate_combinations(population_per_state)
subsets_matching_target = [subset for subset in subset_combinations if sum(subset) == population_target]
print(subsets_matching_target)
print(len(subsets_matching_target))
