class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, node):      
        if self.head is None:
            self.head = node
            self.tail = self.head
            return
            
        self.tail.next = node
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return
    
    def remove(self, node):        
        if node.previous:
            node.previous.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.previous = node.previous
        else:
            self.tail = node.previous            

class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.dictionary = {}
        self.list = LinkedList()
        pass

    def get(self, key):
        
        if self.capacity == 0:
            return -1
        
        node = self.dictionary.get(key, None)
        
        # if value is in D...
        if node != None:
            
            # move to the top of L
            self.list.remove(node)
            self.list.append(node)
            
            # return value
            print(node.value)
            return node.value
        
        # else...
        else:
        
            # if D is full
            if len(self.dictionary) == self.capacity:
                
                # find and remove last from D + L
                last_node = self.list.head
                
                del self.dictionary[last_node.key]
                self.list.remove(last_node)
                
                # add to D + L
                new_node = Node(key, None)
                
                self.dictionary[key] = new_node
                self.list.append(new_node)
                
            # else
            else:
            
                # add to D + L
                new_node = Node(key, None)
                
                self.dictionary[key] = new_node
                self.list.append(new_node)
            
            # return -1
            print(-1)
            return -1
        
    def set(self, key, value):
        
        if self.capacity == 0:
            print("Can't perform operations on 0 capacity cache")
            return
        
        node = self.dictionary.get(key, None)
        
        # if value is in D...
        if node != None:
            
            # move to the top of L
            self.list.remove(node)
            self.list.append(node)
            
            # return value
            node.value = value
        
        # else...
        else:
        
            # if D is full
            if len(self.dictionary) == self.capacity:
                
                # find and remove last from D + L
                last_node = self.list.head
                
                del self.dictionary[last_node.key]
                self.list.remove(last_node)
                
                # add to D + L
                new_node = Node(key, value)
                
                self.dictionary[key] = new_node
                self.list.append(new_node)
                
            # else
            else:
            
                # add to D + L
                new_node = Node(key, value)
                
                self.dictionary[key] = new_node
                self.list.append(new_node)

# test case 1

our_cache = LRU_Cache(5)
    
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache
our_cache.set(5, 5) 
our_cache.set(6, 6)
our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# test case 2

our_cache = LRU_Cache(0)
our_cache.set(1, 1) # should print "Can't perform operations on 0 capacity cache"
our_cache.get(1) # should return -1

# test case 3

our_cache = LRU_Cache(2)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(1, 10)
our_cache.get(1) # should return 10
our_cache.get(2) # should return 2