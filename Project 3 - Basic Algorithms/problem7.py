# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, extension):
        # Initialize the node with children as before, plus a handler
        self.extension = extension
        self.children = {}
        self.handler = None

    def insert(self, extension):
        # Insert the node as before
        if self.children.get(extension, "") == "":
            self.children[extension] = RouteTrieNode(extension)

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode("")

    def insert(self, routes, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root

        for extension in routes:
            if node.children.get(extension, "") == "":
                node.insert(extension)

            node = node.children.get(extension, "")

        node.handler = handler

    def find(self, routes):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root

        if (routes[0] == "" and len(routes) == 1):
            return "root handler"

        for extension in routes:
            if node.children.get(extension, "") == "":
                return "not found handler"

            node = node.children.get(extension, "")

        return node.handler

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router = RouteTrie()

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        routes = self.split_path(path)
        self.router.insert(routes, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        routes = self.split_path(path)

        return self.router.find(routes)

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if path[-1:] == "/":
            path = path[:-1]

        return path.split("/")

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router() # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# test 1
print(router.lookup("/")) # should print 'root handler'

# test 2
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one

# test 3
print(router.lookup("/home/about")) # should print 'about handler'

# test 4
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes

# test 5
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
