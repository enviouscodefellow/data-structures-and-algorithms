from data_structures.binary_tree import BinaryTree, Node
from data_structures.binary_tree import InvalidOperationError

def tree_intersection(tree_a, tree_b):
    values_a = tree_a.pre_order()
    values_b = tree_b.pre_order()

    values_a_dict = {}
    for value in values_a:
        if value in values_a_dict:
            values_a_dict[value] += 1
        else:
            values_a_dict[value] = 1

    common_values = []
    for value in values_b:
        if value in values_a_dict and values_a_dict[value] > 0:
            common_values.append(value)
            values_a_dict[value] -= 1

    return common_values
