import heapq
import sys

# Node in the tree, representing character, frequency, left-child and right-child
class Node(object):

    def __init__(self, character = None, frequency = None, left = None, right = None):
        self.character = character       # represents character
        self.frequency = frequency   # represents frequency
        self.left = left
        self.right = right
        self.binary = None

# Creating a Priority Queue for string character
class PriorityQueue:

    def __init__(self,text):
        self.priority_list = list()

        # find the frequency of the characters in the text
        frequency_table = dict()
        if len(text) >0:
            for val in text:
                if val in frequency_table:
                    frequency_table[val] +=1
                else:
                    frequency_table[val] =1

            for character in frequency_table:
                frequency = frequency_table[character]
                self.priority_list.append(Node(character,frequency))

            self.sort()
        else:
            self.priority_list = []


    # helper method to sort the priority_list based on frequency
    def sort(self):
        self.priority_list = sorted(self.priority_list, key=lambda x: x.frequency, reverse=True)

    # function to pop the smallest value from the priority queue
    def pop(self):
        return self.priority_list.pop()

    # function to insert the item in priority_list and sort it.
    def _insert(self,node):
        self.priority_list.append(node)
        self.sort()

    # function to take the two lowest value and add them to create new node in the tree
    def merge(self):
        new_node = Node()
        node1 = self.pop()  # remove smallest item
        node2 = self.pop()  # remove second smallest item

        sum = node1.frequency + node2.frequency
        new_node.frequency = sum
        new_node.left = node1
        new_node.right = node2
        self._insert(new_node)

class BinaryTree:

    def __init__(self,string):
        queue = PriorityQueue(string)

        # merge till the total length of queue is reduced to 1
        while len(queue.priority_list) != 1:
            queue.merge()

        if len(queue.priority_list) > 0:
            self.root = queue.priority_list[0]  # write the only value there ...
        else:
            self.root = None

    def create_binary_tree(self):
        node = self.root
        if node is not None:
            self.root = self._binarize(node)
            self.root.bin = 0

    # setting the value as either 0 or 1
    def _binarize(self,node):
        if node.left is None and node.right is None:
            return node

        if node.left:
            node.left.binary = 1
            node.left = self._binarize(node.left)  # recusive function

        if node.right:
            node.right.binary = 0
            node.right = self._binarize(node.right) #recursive function

        return node

class HuffmanCoding:
    def __init__(self, text):

        tree = BinaryTree(text)
        tree.create_binary_tree()

        self.root = tree.root
        self.encode_table = dict()
        self.decode_table = dict()

        self.visit_order_list = self._dfs()
        self.text = text


    #return the visit order for encoding table
    def _dfs(self):
        # depth first search
        root = self.root
        initial_code = ''  # random initial value, (we can keep it blank as well)
        visit_order = list() # In form of :  character, code, frequency
        def traverse(initial_code, node):
            if node:
                if node.frequency == -1:
                    current_code = ''
                else:
                    current_code = initial_code + str(node.binary)

                if node.character:
                    visit_order.append((node.character, current_code, node.frequency))
                if node.left:
                    traverse(current_code,node.left)
                if node.right:
                    traverse(current_code,node.right)

        traverse(initial_code,root)
        return visit_order

    def encode(self):
        code = ''
        # Based on the visit order, encode
        for character in self.visit_order_list:
            self.encode_table[character[0]] = character[1]  # 1 in 0

        # code each character in text
        for character in self.text:
            code += str(self.encode_table[character])
        return code

    def decode(self):
        decode = ''

        for character in self.visit_order_list:
            self.decode_table[character[1]] = character[0]   # 0 in 1
        return self.decode_table

def huffman_encoding(text):
    function = HuffmanCoding(text)
    return function.encode(), function

def huffman_decoding(encoded_text, function):
    #print("huffman_decoding",encoded_text)
    decode_table = function.decode()
    decoded_text = ''

    while len(encoded_text) > 0:
        index = 1
        while True:

            if encoded_text[:index] in decode_table:
                decoded_text += decode_table[encoded_text[:index]]
                encoded_text = encoded_text[index:]
                break
            index +=1
    #print("decoded text", decoded_text)
    return decoded_text


if __name__ == "__main__":
    codes = {}

    #test 1
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # The content of the encoded data is: None00010None110None111None01None00011None100None101None0010None01None100None00000None01None00001None110None111None01None00110None00111None101None0010


    encoded_data, tree = huffman_encoding(a_great_sentence)

    #print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 69
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    #The content of the encoded data is: The bird is the word


    #test2
    new_sentence = " this include integer 0"
    encoded_data, tree = huffman_encoding(new_sentence)
    print(encoded_data)
    #None11None101None1001None010None10000None11None010None0010None10001None00010None00011None00000None011None11None010None0010None101None011None00001None011None00110None11None00111

    decoded_data = huffman_decoding(encoded_data, tree)
    print(decoded_data)
    #this include integer 0


    #test3
    new_sentence = " "
    encoded_data, tree = huffman_encoding(new_sentence)
    print(encoded_data)
    #None
    decoded_data = huffman_decoding(encoded_data, tree)
    print(decoded_data)
    #
