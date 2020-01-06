## Represents a single node in the Trie
class TrieNode:
    def __init__(self, char):
        ## Initialize this node in the Trie
        self.char = char
        self.children = {} # dictionary of child characters and Trie Nodes
        self.word = False

    def insert(self, char):
        ## Add a child node in this Trie
        if self.children.get(char, "") == "":
            self.children[char] = TrieNode(char)

    def suffixes(self):
        ## Recursive function that collects the suffix for
        ## all complete words below this point

        l = []

        for n in self.children:
            l = l + suffix_recurse("", self.children[n])

        return l

def suffix_recurse(pre, node):
    l = []

    if node.word:
        l.append(pre + node.char)

    for n in node.children:
        l = l + suffix_recurse(pre + node.char, node.children[n])

    return l

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode("")

    def insert(self, word):
        ## Add a word to the Trie

        node = self.root

        for char in word:
            if node.children.get(char, "") == "":
                node.insert(char)

            node = node.children.get(char, "")

        node.word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix

        node = self.root

        for char in prefix:

            if node.children.get(char, "") == "":
                node.insert(char)

            node = node.children.get(char, "")

        return node

MyTrie = Trie()

wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]

for word in wordList:
    MyTrie.insert(word)

# test 1
x = MyTrie.find("an")
print('\n'.join(x.suffixes()))

# test 2
x = MyTrie.find("")
print('\n'.join(x.suffixes()))

# test 3
x = MyTrie.find("d")
print('\n'.join(x.suffixes()))
