import hashlib
from datetime import datetime

class Block:
    def __init__(self, timestamp, data, previous_block):
      self.timestamp = timestamp
      self.data = data
      self.hash = self.calc_hash()
      self.previous_block = previous_block

    def calc_hash(self):
          sha = hashlib.sha256()
          timestamp_string = self.timestamp.strftime("%m/%d/%Y, %H:%M:%S")
          hash_str = (timestamp_string + self.data).encode('utf-8')
          sha.update(hash_str)
          return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.head = None

    def add_new_block(self, data):
        if self.head is None:
            block = Block(datetime.now(), data, None)
            self.head = block
        else:
            block = Block(datetime.now(), data, self.head)
            self.head = block

    def to_list(self):
        output = []
        output.append(self.head)

        previous = self.head.previous_block
        while previous:
            output.append(previous)
            previous = previous.previous_block

        return output

# test cases

test = Blockchain()
test.add_new_block("Head Block")
test.add_new_block("New Block 1")
test.add_new_block("New Block 2")
test.add_new_block("New Block 2")
test.add_new_block("New Block 1")

output = test.to_list()

counter = 1
for x in output:
    print("block number: " + str(counter))
    print("timestamp: " + str(x.timestamp))
    print("data: " + x.data)
    print("hash: " + x.hash)
    print("previous_hash: " + x.previous_block.hash)
    counter+= 1
