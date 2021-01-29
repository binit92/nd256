class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def get_head(self):
        return self.head

def union(llist_1, llist_2):

    union_linked_list = LinkedList()

    # loop for llist_1
    head1 = llist_1.head
    while head1 is not None:
        # don't add duplicates
        value1 = head1.value
        if not check_if_exists(union_linked_list, value1):
            union_linked_list.append(value1)
        head1 = head1.next

    # loop for llist_2
    head2 = llist_2.head
    while head2 is not None:
        # don't add duplicates
        value2 = head2.value
        if not check_if_exists(union_linked_list, value2):
            union_linked_list.append(value2)
        head2 = head2.next

    # return union
    #print("head",union_linked_list.head)
    return union_linked_list

def intersection(llist_1, llist_2):
    # Your Solution Here
    intersection_linked_list = LinkedList()

    head1 = llist_1.head
    head2 = llist_2.head
    while head1 is not None:
        value = head1.value
        #print("head1.value",value)
        if check_if_exists(llist_2,value):

            #check if already added in intersection_linked_list
            if not check_if_exists(intersection_linked_list,value):
                intersection_linked_list.append(value)

        head1 = head1.next
    return intersection_linked_list


# gelper function to check if some value already exists .
def check_if_exists(llist, value):
    #print("llist",llist)
    #print("value",value)
    #print("size",llist.size())
    head3 = llist.get_head()
    while head3 is not None:
        if head3.value == value:
            #print("found")
            return True
        head3 = head3.next
    return False


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print ("union",union(linked_list_1,linked_list_2))
print ("intersection",intersection(linked_list_1,linked_list_2))

#output
#union 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->
#intersection 4 -> 6 -> 21 ->

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print ("union",union(linked_list_3,linked_list_4))
print ("intersection",intersection(linked_list_3,linked_list_4))
#output
#union 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
#intersection

# Test case 3

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print ("union",union(linked_list_3,linked_list_4))
print ("intersection",intersection(linked_list_3,linked_list_4))
#output
#union
#intersection
