from collections import deque

class Node:
    def __init__(self, value, frequency, code = None, parent = None, child0 = None, child1 = None):
        self.value = value
        self.frequency = frequency
        self.code = code
        self.parent = parent
        self.child0 = child0
        self.child1 = child1
        if child0 is not None:
            child0.parent = self
        if child1 is not None:
            child1.parent = self
    
    def __str__(self):
        return "Node {value: " + str(self.value) + ", frequency: " + str(self.frequency) + ", code: " + \
            str(self.code) + ", parent: " + str(self.get_short_description(self.parent)) + ", child0: " + \
                str(self.get_short_description(self.child0)) + ", child1: " + str(self.get_short_description(self.child1))

    def get_short_description(self, node):
        if node is not None:
            return "(value: " + str(node.value) + ", frequency: " + str(node.frequency) + ")"
        else:
            return None
    
    def get_child_by_code(self, code):
        if code == 0:
            return self.child0
        else:
            return self.child1

    def get_code(self):
        return "" if self.code is None else str(self.code)

    def get_full_code(self):
        if self.parent is None:
            return self.get_code()
        else:
            prefix = self.parent.get_full_code()
            return prefix + str(self.code)

class HuffmanTree:
    def __init__(self, source):
        primal_node_list = self.aggregate_chars(source)
        self.root_tree = self.get_root_tree(list(primal_node_list))
        self.code_table = self.create_code_table(primal_node_list)
        self.encoded = self.encode_string(source)

    def tuple_to_node(self, tpl, code, parent = None):
        return Node(tpl[0], tpl[1], code, parent)
    
    def aggregate_chars(self, source):
        d = dict()
        for c in source:
            d[c] = d.get(c, 0) + 1

        return list(map(lambda x: self.tuple_to_node(x, None), d.items()))
    
    def get_min(self, list):
        index_of_min = 0
        min = list[index_of_min]
        for i in range(1, len(list)):
            current = list[i]
            if current.frequency < min.frequency:
                min = current
                index_of_min = i
        return list.pop(index_of_min)
    
    def sort_two_nodes_by_frequency(self, node1, node2):
        if node1.frequency > node2.frequency:
            return [node1, node2]
        else:
            return [node2, node1]

    def sort_two_nodes(self, node1, node2):
        if node1.value is not None:
            if node2.value is None:
                return [node1, node2]
            else:
                return self.sort_two_nodes_by_frequency(node1, node2)
        elif node2.value is not None:
            return [node2, node1]
        else:
            return self.sort_two_nodes_by_frequency(node1, node2)

    def get_root_tree(self, node_list):
        n = len(node_list)
        if n == 1:
            node_list[0].code = 0
        for i in range(n + 1, 2 * n):
            a = self.get_min(node_list)
            b = self.get_min(node_list)
            child0, child1 = self.sort_two_nodes(a, b)
            child0.code = 0
            child1.code = 1
            result = Node(None, a.frequency + b.frequency, None, None, child0, child1)
            # print("child0: ", str(child0))
            # print("child1: ", str(child1))
            # print("result: ", result)
            # print("--------------------------------")
            node_list.append(result)
        return node_list[0]

    def create_code_table(self, primal_node_list):
        code_table = dict()
        for node in primal_node_list:
            code_table[node.value] = node.get_full_code()
        
        return code_table
    
    def encode_string(self, s):
        return "".join(list([self.code_table[c] for c in s]))
    
    def decode(self):
        for c in self.encoded:
            self.root_tree.get_child_by_code

s = input()

#region code    
# def tuple_to_item(tpl, code, parent = None):
#     return Node(tpl[0], tpl[1], code, parent)

# d = dict()
# for c in s:
#     d[c] = d.get(c, 0) + 1
# print(d)

# nodes_with_values = []

# node_list = list(map(lambda x: tuple_to_item(x, None), d.items()))
# # print(list(map(str, list)))

# def get_min(list):
#     index_of_min = 0
#     min = list[index_of_min]
#     for i in range(1, len(list)):
#         current = list[i]
#         if current.frequency < min.frequency:
#             min = current
#             index_of_min = i
#     return list.pop(index_of_min)

# def sort_two_nodes_by_frequency(node1, node2):
#     if node1.frequency > node2.frequency:
#         return [node1, node2]
#     else:
#         return [node2, node1]

# def sort_two_nodes(node1, node2):
#     if node1.value is not None:
#         if node2.value is None:
#             return [node1, node2]
#         else:
#             return sort_two_nodes_by_frequency(node1, node2)
#     elif node2.value is not None:
#         return [node2, node1]
#     else:
#         return sort_two_nodes_by_frequency(node1, node2)

# code_table = dict()

# def add_to_code_table(node, table):
#     if node.value is not None:
#         nodes_with_values.append(node)

# n = len(node_list)
# for i in range(n + 1, 2 * n):
#     a = get_min(node_list)
#     b = get_min(node_list)
#     child0, child1 = sort_two_nodes(a, b)
#     child0.code = 0
#     child1.code = 1
#     result = Node(None, a.frequency + b.frequency, None, None, child0, child1)
#     add_to_code_table(child0, code_table)
#     add_to_code_table(child1, code_table)
#     print("child0: ", str(child0))
#     print("child1: ", str(child1))
#     print("result: ", result)
#     print("--------------------------------")
#     node_list.append(result)

# print(list(map(str, node_list)))

# for node in nodes_with_values:
#     code_table[node.value] = node.get_full_code()

# tree = node_list[0]

# print(code_table)

# def encode_string(s):
#     return "".join(list([code_table[c] for c in s]))

# print(encode_string(s))
#endregion

h_tree = HuffmanTree(s)
print(len(h_tree.code_table.keys()), len(h_tree.encoded))
print('\n'.join([str(x[0]) + ": " + x[1] for x in h_tree.code_table.items()]))
print(h_tree.encoded)