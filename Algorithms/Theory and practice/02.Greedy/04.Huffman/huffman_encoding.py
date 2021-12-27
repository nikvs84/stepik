from collections import deque


class Node:
    def __init__(self, value, frequency, code=None, parent=None, child0=None, child1=None):
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
            str(self.get_short_description(self.child0)) + ", child1: " + \
            str(self.get_short_description(self.child1))

    def get_short_description(self, node):
        if node is not None:
            return "(value: " + str(node.value) + ", frequency: " + str(node.frequency) + ")"
        else:
            return None

    def get_child_by_code(self, code):
        if code == '0':
            return self.child0
        elif code == '1':
            return self.child1
        else:
            raise ValueError("Unknown code '" + str(code) + "'")

    def __create_empty_child_by_code(self, code):
        if code == '0':
            if self.child0 is not None:
                raise Exception("Node already has child0")
            else:
                self.child0 = Node(None, None, code)
                result = self.child0
        elif code == '1':
            if self.child1 is not None:
                raise Exception("Node already has child0")
            else:
                self.child1 = Node(None, None, code)
                result = self.child1
        else:
            raise ValueError("Unknown code '" + str(code) + "'")
        
        return result

    def get_code(self):
        return "" if self.code is None else str(self.code)

    def get_full_code(self):
        if self.parent is None:
            return self.get_code()
        else:
            prefix = self.parent.get_full_code()
            return prefix + str(self.code)

    def creaete_or_get_child_by_code(self, code):
        child = self.get_child_by_code(code)
        if child is not None:
            return child
        else:
            return self.__create_empty_child_by_code(code)

    def creaete_branch_by_path(self, path, value=None):
        if path is None or path == '':
            raise ValueError("path must not be None or empty")
        current = self
        for point in path:
            current = current.creaete_or_get_child_by_code(point)
        if current != self:
            current.value = value

        return current

    def get_node_by_path(self, path):
        current = self
        for point in path:
            current = current.get_child_by_code(point)

        return current

    def find_node_with_value_by_binary_sequence(self, sequence, offset):
        current = self
        while current.value is None:
            current = current.get_child_by_code(sequence[offset])
            offset += 1

        return (current, offset)


class HuffmanTree:
    def __init__(self, source, root_tree, code_table, encoded):
        self.source = source
        self.root_tree = root_tree
        self.code_table = code_table
        self.encoded = encoded

    @classmethod
    def from_source(cls, source: str):
        primal_node_list = cls.aggregate_chars(source)
        root_tree = cls.get_root_tree(list(primal_node_list))
        code_table = cls.create_code_table(primal_node_list)
        encoded = cls.encode_string(source, code_table)
        return cls(source, root_tree, code_table, encoded)

    @classmethod
    def from_code_table_and_encoded(cls, code_table: dict, encoded: str):
        root_tree = cls.root_tree_from_code_table(code_table)
        source = cls.decode(encoded, root_tree)
        return cls(source, root_tree, code_table, encoded)

    @classmethod
    def tuple_to_node(cls, tpl, code, parent=None):
        return Node(tpl[0], tpl[1], code, parent)

    @classmethod
    def aggregate_chars(cls, source):
        d = dict()
        for c in source:
            d[c] = d.get(c, 0) + 1

        return list(map(lambda x: cls.tuple_to_node(x, None), d.items()))

    @classmethod
    def get_min(cls, list):
        index_of_min = 0
        min = list[index_of_min]
        for i in range(1, len(list)):
            current = list[i]
            if current.frequency < min.frequency:
                min = current
                index_of_min = i
        return list.pop(index_of_min)

    @classmethod
    def sort_two_nodes_by_frequency(cls, node1, node2):
        if node1.frequency > node2.frequency:
            return [node1, node2]
        else:
            return [node2, node1]

    @classmethod
    def sort_two_nodes(cls, node1, node2):
        if node1.value is not None:
            if node2.value is None:
                return [node1, node2]
            else:
                return cls.sort_two_nodes_by_frequency(node1, node2)
        elif node2.value is not None:
            return [node2, node1]
        else:
            return cls.sort_two_nodes_by_frequency(node1, node2)

    @classmethod
    def get_root_tree(cls, node_list):
        n = len(node_list)
        if n == 1:
            node_list[0].code = 0
        for i in range(n + 1, 2 * n):
            a = cls.get_min(node_list)
            b = cls.get_min(node_list)
            child0, child1 = cls.sort_two_nodes(a, b)
            child0.code = 0
            child1.code = 1
            result = Node(None, a.frequency + b.frequency,
                          None, None, child0, child1)
            # print("child0: ", str(child0))
            # print("child1: ", str(child1))
            # print("result: ", result)
            # print("--------------------------------")
            node_list.append(result)
        return node_list[0]

    @classmethod
    def create_code_table(cls, primal_node_list):
        code_table = dict()
        for node in primal_node_list:
            code_table[node.value] = node.get_full_code()

        return code_table

    @classmethod
    def encode_string(cls, s, code_table):
        return "".join(list([code_table[c] for c in s]))

    @classmethod
    def decode(cls, encoded, root_tree):
        offset = 0
        result = ''
        while offset < len(encoded):
            tuple_and_offset = root_tree.find_node_with_value_by_binary_sequence(encoded, offset)
            result += tuple_and_offset[0].value
            offset = tuple_and_offset[1]
        
        return result

    @classmethod
    def root_tree_from_code_table(cls, code_table):
        sorted_tuples = sorted(code_table.items(), key=lambda i: i[1])
        root = Node(None, None, None, None, None)
        for tuple in sorted_tuples:
            root.creaete_branch_by_path(tuple[1], tuple[0])

        return root


# s = input()

# h_tree = HuffmanTree.from_source(s)
# print(len(h_tree.code_table.keys()), len(h_tree.encoded))
# print('\n'.join([str(x[0]) + ": " + x[1] for x in h_tree.code_table.items()]))
# print(h_tree.encoded)

# decoding_tree = HuffmanTree.from_code_table_and_encoded(h_tree.code_table, h_tree.encoded)
# print(decoding_tree.source)

k, l = map(int, input().split())

code_table = dict()
for i in range(k):
    letter, code = input().split(': ')
    code_table[letter] = code

# print(code_table)

encoded = input()

huffman_tree = HuffmanTree.from_code_table_and_encoded(code_table, encoded)
print(huffman_tree.source)