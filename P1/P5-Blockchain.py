import hashlib
#from time import gmtime
import time


class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        #hash_str = "We are going to encode this string of data!".encode('utf-8')
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class Node:

    def __init__(self,block):
        self.block = block
        self.next = None

block1 = Block(time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()),"Some Information",None)
node1 = Node(block1)

block2 = Block(time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()),"Some Information",block1.hash)
node2 = Node(block2)
node1.next = node2

block3 = Block(time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()),"Some Information",block2.hash)
node3 = Node(block3)
node2.next = node3

head = node1
i =1
while True:
    print("index: ", i ,"timestamp: ", head.block.timestamp, "data: ", head.block.data, " hash: ", head.block.hash,)
    if head.next == None:
        break
    else:
        head = head.next
        i+= 1
# output
#index:  1 timestamp:  Fri, 29 Jan 2021 07:44:35 AM India Standard Time data:  Some Information  hash:  6d8bf1eac14158e858b3a3a376c5dedeceb895ce5fc715324020eb0cfb2d4336
#index:  2 timestamp:  Fri, 29 Jan 2021 07:44:35 AM India Standard Time data:  Some Information  hash:  6d8bf1eac14158e858b3a3a376c5dedeceb895ce5fc715324020eb0cfb2d4336
#index:  3 timestamp:  Fri, 29 Jan 2021 07:44:35 AM India Standard Time data:  Some Information  hash:  6d8bf1eac14158e858b3a3a376c5dedeceb895ce5fc715324020eb0cfb2d4336


# test 2 :  empty data

block1 = Block(time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()),"",None)  # notice empty alue here and hence output is different
node1 = Node(block1)

# test 3 : non-empty data after empty data in head 
block2 = Block(time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()),"Block2",block1.hash)
node2 = Node(block2)
node1.next = node2

block3 = Block(time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()),"block3",block2.hash)
node3 = Node(block3)
node2.next = node3

head = node1
i =1
while True:
    print("index: ", i ,"timestamp: ", head.block.timestamp, "data: ", head.block.data, " hash: ", head.block.hash,)
    if head.next == None:
        break
    else:
        head = head.next
        i+= 1

#output
#index:  1 timestamp:  Fri, 29 Jan 2021 07:45:35 AM India Standard Time data:    hash:  e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
#index:  2 timestamp:  Fri, 29 Jan 2021 07:44:35 AM India Standard Time data:  Block2  hash:  61edd5d6b03c20f764aab3bc4291b162ff48958e316603d4c07548a37872e380
#index:  3 timestamp:  Fri, 29 Jan 2021 07:44:35 AM India Standard Time data:  block3  hash:  7e56ddaff5ff44d9e1732b1fd138a2057df045b163385068988554f72047e272
