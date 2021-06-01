from heapq import *
from treelib import Node, Tree

class Huffman:
    """Class containig single element in Huffman coding"""
    def __init__(self, f, l):
        self.freq = f
        self.letter = l
        self.value = ""
        self.first_child = None
        self.second_child = None
    
    def __lt__(self, other):
        return self.freq < other.freq    

    def __str__(self):
        return f"{self.freq}, {self.letter}"


    def childs(self, h1, h2):
        """Append left and righ nodes"""
        self.first_child = h1
        self.second_child = h2

def show_child_nodes(node, str, tree, p):
    """Function recursively searches for leaves of coding tree"""
    if node[1] == None:
        return
    str = str+node[1].value
    if node[1].first_child:
        tree.create_node("0", f'{str}0', parent=p)
        show_child_nodes(node[1].first_child, str, tree, f'{str}0')
    if node[1].second_child:
        tree.create_node("1", f'{str}1', parent=p)
        show_child_nodes(node[1].second_child, str, tree, f'{str}1')

    if len(node[1].letter)==1:
        tree.create_node(node[1].letter, node[1].letter, parent=p)
        print(f"{node[1].letter} = {str}")

def count_in_file(filename, huffman):
    """Count how many times letter appears in given txt file"""
    try:
        with open(filename, encoding='utf-8') as read_from_file:
            content = read_from_file.read()
            content = content.lower()
    except FileNotFoundError:
        print('File not found')
    else:
        for i in range(26):
            freq_count = 0
            sign = chr(97+i)
            freq_count = content.count(sign)
            print(f"{sign} = {freq_count}")
            heappush(huffman, (freq_count, Huffman(freq_count, sign)))

def create_coding(huffman):
    """Create huffman coding for given letters and requencies"""
    while len(huffman) > 1:
        temp1 = heappop(huffman)
        temp2 = heappop(huffman)
        new_freq = temp1[0] + temp2[0]
        temp1[1].value = '0'
        temp2[1].value = '1'
        new_element = Huffman(new_freq, temp1[1].letter+temp2[1].letter)
        new_element.childs(temp1, temp2)
        heappush(huffman,(new_freq, new_element))

huffman = []
tree = Tree()
tree.create_node("root", "root")
count_in_file('tadek.txt', huffman)
create_coding(huffman)
show_child_nodes(huffman[0],"",tree,"root")
tree.show()

