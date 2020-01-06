import sys
from collections import deque

class Queue():
    def __init__(self):
        self.q = deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)
    
    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n" 
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"

class Node(object):
    def __init__(self, value = None, letter = None):
        self.value = value
        self.letter = letter
        self.left = None
        self.right = None
        
    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"

def huffman_encoding(data):
    #create frequency dictionary
    freq = {}
    
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    
    #create list of starting nodes
    nodes = []
    
    for letter, frequency in freq.items():
        node = Node(frequency, letter)
        nodes.append(node)
    
    #handle edge cases
    if len(nodes) == 0:
        return "Please encode data with content"
    
    #combine nodes from lowest to highest frequencies, until there is just one node left    
    while len(nodes) > 1:
        #sort list
        nodes.sort(key=lambda x: x.value)
        
        x = nodes.pop(0)
        y = nodes.pop(0)
                
        new_node = Node(x.value + y.value, None)
        new_node.set_left_child(x)
        new_node.set_right_child(y)
        
        nodes.append(new_node)
        
    root = nodes[0]

    #create final code dictionary
    codes = {}
    
    #if there is only one letter
    if root.letter != None:
        codes[root.letter] = "1"
        
    #if there are multiple letters to code
    else:
        #create queue and add root tuple with empty code
        q = Queue()
        q.enq((root, ""))
        
        #parse through tree, using BSF algorithm
        while(len(q) > 0):
            x = q.deq()
            
            node = x[0]
            code = x[1]
            
            if node.letter != None:
                codes[node.letter] = code
            
            if node.has_left_child():
                t = (node.get_left_child(), code + "0")
                q.enq(t)
                
            if node.has_right_child():
                t = (node.get_right_child(), code + "1")
                q.enq(t)
        
    #encode data
    output = ""
    
    for x in data:
        output = output + codes[x]
        
    return output, root

def huffman_decoding(data, node):
    
    output = ""
    
    current_node = node
    
    #if there is only one letter
    if current_node.letter != None:
        for x in data:
            output = output + current_node.letter
    
    #if there are multiple letters to decode
    else:
        for x in data:
            if x == "0":
                current_node = current_node.get_left_child()
            if x == "1":
                current_node = current_node.get_right_child()
                
            if current_node.letter != None:
                output = output + current_node.letter
                current_node = node
            
    return output

# test case 1    
    
a_great_sentence = "The bird is the word"

huffman_encoding(a_great_sentence)

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))

# test case 2

a_great_sentence = "AAAAAAA"

huffman_encoding(a_great_sentence)

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))