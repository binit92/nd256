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
